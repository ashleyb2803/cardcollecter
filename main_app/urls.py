from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cards/', views.card_index, name='card_index'),  
    path('cards/<int:card_id>/', views.card_detail, name='card-detail'), 
    path('cards/create/', views.CardCreate.as_view(), name='card_create'), 
    path('cards/<int:pk>/update/', views.CardUpdate.as_view(), name='card-update'),
    path('cards/<int:pk>/delete/', views.CardDelete.as_view(), name='card-delete'),
    path('cards/<int:card_id>/add-wrestler/', views.add_wrestler, name='add-wrestler'),
    path('wrestler/<int:wrestler_id>/edit/', views.wrestler_update, name='wrestler-update'),
    path('wrestler/<int:wrestler_id>/delete/', views.wrestler_delete, name='wrestler-delete'),

]

