from  django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('news/', views.news, name='news'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/edit/<int:booking_id>/', views.edit_booking, name='edit_booking'),
    path('dashboard/delete/<int:booking_id>/', views.delete_booking, name='delete_booking'),
    path('news/<int:guide_id>/', views.guide_details, name='guide_details'),
    path('guide/', views.guide, name='guide'),  # Added forward slash
    
    path('destinations/', views.destinations, name='destinations'),
    path('contact_guide/<int:guide_id>/', views.contact_guide, name='contact_guide') # New URL
]
