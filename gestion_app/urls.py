from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from gestion_app import views  

urlpatterns = [

    path('', views.inscription, name='inscription'), 
    path('connexion/', views.connexion, name='connexion'),  
    path('doctor_dashboard/', views.doctor_dashboard, name='doctor_dashboard'), 
    path('ong_dashboard/', views.ong_dashboard, name='ong_dashboard'), 
    path('ong_dashboard/ajouter_enfant', views.ajouter_enfant, name='ajouter_enfant'),
    path('ong_dashboard/liste_enfant', views.liste_enfant, name='liste_enfant'),  
    path('deconnexion/', views.deconnexion, name='deconnexion'), 
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
