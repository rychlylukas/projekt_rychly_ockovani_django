from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('seznamvakcin/', views.seznamvakcin, name='seznam_vakcin'),
    path('ockovani/', views.OckovaniListView.as_view(), name='ockovani'),
    path('ockovani/vakciny/<str:vakcina_nazev_firmy>/', views.OckovaniListView.as_view(), name='vakcina_genre'),
    path('ockovani/<int:pk>/', views.OckovaniDetailView.as_view(), name='osoba_detail'),
    path('ockovani/<int:pk>/', views.OckovaniDetailView.as_view(), name='ockovani-detail'),
    path('ockovani/<int:pk>/update/', views.OckovaniUpdateView.as_view(), name='osoba_update'),
    path('ockovani/<int:pk>/delete/', views.OckovaniDeleteView.as_view(), name='osoba_delete'),
    path('ockovani/create/', views.OckovaniCreateView.as_view(), name='osoba_create'),

]