from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns =[
    path('',RedirectView.as_view(url='/members/',permanent = True)),
    path('members/main/',views.main,name='main'),
    path('members/',views.members,name='members'),
    path('members/imformation/<int:id>',views.imformation,name='imformation'),
    path('members/filter/',views.filter_view,name='filter'),

    path('wish/',views.wishlist,name='view_wishlist'),
    path('add_wish/',views.add_to_wishlist,name='add_to_wishlist'),
    
    path('homepage/',views.TEST,name='test'),
# 
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    
]