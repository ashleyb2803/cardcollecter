from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    
    # Card URLs
    path('cards/', views.card_index, name='card_index'),  
    path('cards/<int:card_id>/', views.card_detail, name='card-detail'), 
    path('cards/create/', views.CardCreate.as_view(), name='card_create'), 
    path('cards/<int:pk>/update/', views.CardUpdate.as_view(), name='card-update'),
    path('cards/<int:pk>/delete/', views.CardDelete.as_view(), name='card-delete'),
    path('cards/<int:card_id>/add-wrestler/', views.add_wrestler, name='add-wrestler'),
    
    # Wrestler URLs
    path('wrestlers/', views.wrestler_index, name='wrestler_index'),
    path('wrestlers/<int:wrestler_id>/', views.wrestler_detail, name='wrestler-detail'),
    path('wrestler/<int:wrestler_id>/edit/', views.wrestler_update, name='wrestler-update'),
    path('wrestler/<int:wrestler_id>/delete/', views.wrestler_delete, name='wrestler-delete'),
    
    # Pack URLs
    path('open-pack/', views.open_pack, name='open-pack'),
    path('my-packs/', views.my_packs, name='my-packs'),
    path('packs/<int:pack_id>/', views.pack_detail, name='pack-detail'),
]