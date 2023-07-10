from django.contrib import admin
from django.urls import path,include
from app1.views import *
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register("planlar",PlanModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', obtain_auth_token),
    path('', include(router.urls)),
]
