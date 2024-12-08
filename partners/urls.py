from django.urls import path,include
from rest_framework import routers
from .views import *
router = routers.DefaultRouter()
router.register('user',UserViewSet)
router.register('group',GroupViewSet)
router.register('commande',CommandeViewSet)
router.register('produitencommande',ProduitEnCommandeViewSet)
router.register('remise',RemiseViewSet)
router.register('FeedBack',FeedBackViewSet)



urlpatterns = [
    path('',include(router.urls)),
]