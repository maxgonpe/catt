from django.urls import path, include

from rest_framework.routers import DefaultRouter
#from res_framework import viewsets
from profiles_api import views
from .views import *  #DetalleListApiView

router = DefaultRouter()
router.register('profile',views.UserProfileViewSet)

urlpatterns = [
    path('',include(router.urls)),

]
