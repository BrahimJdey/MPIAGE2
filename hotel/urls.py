from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('book/', views.book, name='book'),
    path('book/<int:id>', views.bookRoom, name='bookRoom'),
    #path('book/cancel/<str:id>', views.book, name='book'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
