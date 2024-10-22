from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from gestion_app import views  

urlpatterns = [

    path('admin/' ,admin.site.urls),
    path('', views.inscription, name='inscription'),  # Page d'inscription
    path('connexion/', views.connexion, name='connexion'),  # Page de connexion
    path('doctor_dashboard/', views.doctor_dashboard, name='doctor_dashboard'),  # Page pour médecins
    path('ong_dashboard/', views.ong_dashboard, name='ong_dashboard'),  # Page pour ONG
    path('deconnexion/', views.deconnexion, name='deconnexion'),  # Page de déconnexion
]



# Si tu utilises des fichiers statiques, assure-toi de les servir en mode développement
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



