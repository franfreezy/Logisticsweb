from django.urls import path
from .views import login,register,TruckCreateView,refresh_access_token,create_order,get_order_coordinates,forgot_password


urlpatterns = [
    path('login/', login, name="homepage"),
    path('register/', register, name="location"),
    path('trucks/', TruckCreateView.as_view(), name='truck-create'),
    path("token/refresh/", refresh_access_token, name="token_refresh"),
    path('create-order/', create_order, name='create_order'),
    path('order/<str:order_id>/coordinates/', get_order_coordinates, name='get_order_coordinates'),
    path('forgot-password/', forgot_password, name='forgot_password'),

    
    
]