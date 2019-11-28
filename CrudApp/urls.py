from django.urls import path
from . import views

urlpatterns = [
    path('razerblade15', views.IndexView.as_view(), name='index'),
    path('', views.index, name='index'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('facebook/<int:pk>/384994151644862', views.edit, name='edit'),
    path('post/', views.postview, name='post'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]