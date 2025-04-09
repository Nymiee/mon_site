from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from gestion_app import views  

urlpatterns = [
    path('', views.index, name='index'),  
    path('inscription', views.inscription, name='inscription'),
    path('apropos', views.apropos, name='apropos'), 
    path('contact', views.contact, name='contact'),
    path('nosactions', views.nosactions, name='nosactions'),  
    path('connexion/', views.connexion, name='connexion'),
    path('don/', views.don, name='don'),
    path('listedon/', views.listedon, name='listedon'),
    path('export/pdf/', views.export_pdf, name='export_pdf'),
    path('export_enfant/', views.export_enfant, name='export_enfant'),
    path('merci/', views.merci, name='merci'),
    path('doctor_dashboard/', views.doctor_dashboard, name='doctor_dashboard'), 
    path('ong_dashboard/', views.ong_dashboard, name='ong_dashboard'), 
    path('ong_dashboard/ajouter_enfant', views.ajouter_enfant, name='ajouter_enfant'),
    path('ong_dashboard/liste_enfant', views.liste_enfant, name='liste_enfant'), 
    path('ong_dashboard/rapport', views.rapport, name='rapport'), 
    path('deconnexion/', views.deconnexion, name='deconnexion'), 
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
