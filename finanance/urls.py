from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('index', views.index, name='index'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),

# FactFr
    path('factsFr/<int:pk>/update/', views.FactFrUpdateView.as_view(), name='factFr_update'),
    path('factFr/<int:pk>/delete/', views.FactFrDeleteView.as_view(), name='delete_factFr'),
    path('factFr/', views.factFr, name='factFr'),
    path('create_factFr/', views.FactFrCreateView.as_view(), name='create_factFr'),
    
# FactCl
    path('factCl/<int:pk>/update/', views.FactClUpdateView.as_view(), name='factCl_update'),
    path('factCl/<int:pk>/delete/', views.FactClDeleteView.as_view(), name='delete_factCl'),
    path('factCl/', views.factCl, name='factCl'),
    path('create_fact/', views.FactClCreateView.as_view(), name='create_factCl'),
   
    path('client/<int:pk>/update/', views.ClientUpdateView.as_view(), name='client_update'),
    path('client/<int:pk>/delete/', views.ClientDeleteView.as_view(), name='delete_client'),
    path('clientList/', views.clientList, name='clientList'),
    path('create_client/', views.ClientCreateView.as_view(), name='create_client'),
   
    path('fourn/<int:pk>/update/', views.FournUpdateView.as_view(), name='fourn_update'),
    path('fours/<int:pk>/delete/', views.FournDeleteView.as_view(), name='delete_fourn'),
    path('foursList/', views.foursList, name='foursList'),
    path('create_fours/', views.FoursCreateView.as_view(), name='create_fours'),

] 
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
