from django.urls import path
from . import views

urlpatterns =[
#    path('',views.members,name='members'),
   path('members/main/',views.main,name='main'),
    path('members/',views.members,name='members'),
    # path('members/main',views.main,name='main'),
    path('members/imformation/<int:id>',views.imformation,name='imformation'),
]