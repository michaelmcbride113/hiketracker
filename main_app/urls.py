from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('hikes/', views.hike_index, name='hike-index'),
    path('hikes/<int:hike_id>/', views.hike_detail, name='hike-detail'),
    path('hikes/create/', views.HikeCreate.as_view(), name='hike-create'),
    path('hikes/<int:pk>/update/', views.HikeUpdate.as_view(), name='hike-update'),
    path('hikes/<int:pk>/delete/', views.HikeDelete.as_view(), name='hike-delete'),
    path('accounts/signup', views.signup, name='signup'),
]