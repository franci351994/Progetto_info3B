from django.shortcuts import render, redirect
from django.urls import reverse
from coda.models import Paziente, Priority
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from coda.forms import ChangePazientePriorityModelForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from datetime import timedelta

class PriorityDetailView(generic.DetailView):

    model = Priority

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['time_str'] = str(self.object.time)

        return context

@login_required
def pazientescheda(request):
    if Paziente.objects.filter(rif=request.user):
        paziente = Paziente.objects.get(rif=request.user)
    else:
        paziente = None

    context = {
        'paziente': paziente,
    }
    return render(request, 'paziente_scheda.html', context=context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('paziente_create')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

class PazienteCreate(CreateView):

    model = Paziente
    fields = ['first_name', 'last_name', 'priority_code']
    initial = {'priority_val': 1}

    def form_valid(self, form):
         user = self.request.user
         form.instance.rif = user
         form.instance.priority_val = form.instance.priority_code.val

         return super(PazienteCreate, self).form_valid(form)

    def post(self,request,*args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.form_valid(form)

            lista_pazienti_min = Paziente.objects.filter(priority_val__lt = self.object.priority_val)

            for paziente in lista_pazienti_min:
                if paziente.priority_val<6:
                    if paziente.priority_val<(paziente.priority_code.val+3):
                        paziente.priority_val=paziente.priority_val+1
                        paziente.save()

            return HttpResponseRedirect(self.get_success_url())
        self.object = None
        return self.form_invalid(form)

def access(request):
    if request.user.is_authenticated:
        return redirect('paziente-scheda')

    return render(request, 'access.html')

def time_tot(request):
    t = timedelta()
    paz = Paziente.objects.get(rif=request.user)
    lista = Paziente.objects.filter(priority_val__gte = paz.priority_val).order_by('-priority_val', 't_arrival')

    for paziente in lista:
        if paziente == paz:
            break
        t=t+paziente.priority_code.time

    context = {
        'time_tot': str(t),
    }

    return render(request, 'time_tot.html', context=context)
