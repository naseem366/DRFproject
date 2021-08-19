"""jwtoken URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter
#from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView


#creating Router objects
router=DefaultRouter()

#register studentviewset wiht router
router.register('studentapi',views.StudentToken,basename='student'),
#router.register('studentapi',views.StudentReadOnlyModelViewSet,basename='student')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    #path('auth/',include('rest_framework.urls',namespace='rest_framework')),
    #path('gettoken/',obtain_auth_token)
    path('gettoken/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('refreshtoken/',TokenRefreshView.as_view(),name='token_refresh'),
    path('verifytoken/',TokenVerifyView.as_view(),name='token_verify'),
]
