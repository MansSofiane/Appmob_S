from django.urls import path
from .views import UsersList, UsersDetail,  DepanneurList, DepanneurDetail, ServicesDeDepannageList


urlpatterns = [
    path('users/', UsersList.as_view(), name='users-list'),
    path('users/<int:pk>/', UsersDetail.as_view(), name='users-list'),
    path('depanneurs/', DepanneurList.as_view(), name='depanneur-list'),
    path('depanneurs/<int:pk>/', DepanneurDetail.as_view(), name='depanneur-detail'),
    path('services/', ServicesDeDepannageList.as_view(), name='service-depannage-list'),
    # Définir les autres URLs ici...
]