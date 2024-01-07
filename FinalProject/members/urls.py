from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns =[
    path('',RedirectView.as_view(url='/members/',permanent = True)),
    path('members/main/',views.main,name='main'),
    path('members/',views.members,name='members'),
    path('members/imformation/<int:id>',views.imformation,name='imformation'),
    path('members/filter/',views.filter,name='filter'),
    path('members/wish/',views.wish,name='wish'),
]