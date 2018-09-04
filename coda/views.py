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

def index(request):
    num_Pazienti = Paziente.objects.all().count
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    context = {
        'num_Pazienti': num_Pazienti,
        'num_visits' : num_visits,
    }

    return render(request, 'index.html', context=context)


class PazienteListView(generic.ListView):

    model = Paziente

class PazienteDetailView(generic.DetailView):

    model = Paziente

class PriorityListView(generic.ListView):

    model = Priority

class PriorityDetailView(generic.DetailView):

    model = Priority

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

@permission_required('coda.can_change_priority')
def change_paziente_priority(request, pk):
    paziente = get_object_or_404(Paziente, pk=pk)

    if request.method == 'POST':

        change_paziente_priority_form = ChangePazientePriorityModelForm(request.POST)

        if change_paziente_priority_form.is_valid():
            paziente.priority_code = change_paziente_priority_form.cleaned_data['priority_code']
            paziente.save()

            return HttpResponseRedirect(reverse('pazienti'))

    else:
        proposed_priority_code = paziente.priority_code
        change_paziente_priority_form = ChangePazientePriorityModelForm(initial={'priority_code': proposed_priority_code})

    context= {
        'form': change_paziente_priority_form,
        'paziente': paziente,
    }

    return render(request, 'coda/change_paziente_priority.html', context)

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

def access(request):
    if request.user.is_authenticated:
        return redirect('index')

    return render(request, 'access.html')
