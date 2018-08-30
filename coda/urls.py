from django.urls import path
from coda import views


urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.access, name='access'), 
    path('pazienti/', views.PazienteListView.as_view(), name='pazienti'),
    path('paziente/<int:pk>', views.PazienteDetailView.as_view(), name='paziente-detail'),
    path('priority/', views.PriorityListView.as_view(), name='priority'),
    path('priority/<int:pk>', views.PriorityDetailView.as_view(), name='priority-detail'),
    path('scheda', views.pazientescheda, name='paziente-scheda'),
    path('paziente/<int:pk>/change-priority', views.change_paziente_priority, name='change_paziente_priority'),
    path('paziente/create/', views.PazienteCreate.as_view(), name='paziente_create'),
]
