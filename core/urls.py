from django.urls import path
from . import views

urlpatterns = [
    path('', views.home2, name='home2'),  # Second homepage
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('skills/', views.skills, name='skills'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)