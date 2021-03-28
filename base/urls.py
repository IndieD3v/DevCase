from django.urls import path
from .views import *

urlpatterns = [
    path('', Home , name='home'),
    path('add/',Add , name='add'),

    path('delete/<int:pk>/',Delete,name='delete'),
    path('update/<int:pk>/',Update,name='update'),

    path('logout/',Logout,name='logout'),
    path('like/',LikeProject, name='like_project')
]