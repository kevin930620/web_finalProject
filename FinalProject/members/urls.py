from django.urls import path
from django.views.generic import RedirectView
from . import views

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


LOGIN_REDIRECT_URL = reverse_lazy('models')

class CustomLoginView(LoginView):
    success_url = reverse_lazy('models')

    
urlpatterns =[
    path('',RedirectView.as_view(url='/members/',permanent = True)),
    path('members/main/',views.main,name='main'),
    path('members/',views.members,name='members'),
    path('members/imformation/<int:id>',views.imformation,name='imformation'),
    path('members/filter/',views.filter_view,name='filter'),

    path('members/wish/',views.wishlist,name='view_wishlist'),
    path('add_wish/',views.add_to_wishlist,name='add_to_wishlist'),
    
    # path('homepage/',views.TEST,name='test'),
# 
    path('login/',views.login,name='login'),
    # path('login/',CustomLoginView.as_view(), {'template_name': 'login.html'}, name='login'),
    path('logout/',views.logout,name='logout'),
    
]

