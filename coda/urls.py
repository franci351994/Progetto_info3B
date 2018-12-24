from django.urls import path
from coda import views


urlpatterns = [
    path('', views.access, name='access'),
    path('priority/<int:pk>', views.PriorityDetailView.as_view(), name='priority-detail'),
    path('scheda/', views.pazientescheda, name='paziente-scheda'),
    path('paziente/create/', views.PazienteCreate.as_view(), name='paziente_create'),
    path('scheda/time_tot', views.time_tot, name='time_total'),
]
