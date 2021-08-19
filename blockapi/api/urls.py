from django.urls import path,include
from . import views
from .views import BlockUserAPIView UnblockUserAPIView,UserProfileDetailsAPIView,DeleteUserAPIView


urlpatterns = [
    path('blockapi/<int:pk>',BlockUserAPIView.as_view(),name="blockapi"),
    path('unblockapi/',UnblockUserAPIView.as_view(),name="unblockapi"),
    path('userapi/',UserProfileDetailsAPIView.as_view(),name="userapi"),
    path('deleteapi/',DeleteUserAPIView.as_view(),name="deleteapi"),

]
