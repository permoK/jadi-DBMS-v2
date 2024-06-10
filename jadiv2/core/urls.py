from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from .models import NotesUpload

# from . import views

# router = DefaultRouter()
# router.register('user-profile', UserView)
# router.register('learning-institutions', LearningInstitutionView)
# router.register('interests', InterestView)
router = DefaultRouter()
router.register(r'user-profiles', UserView, basename='userprofile')
router.register(r'learning-institutions', LearningInstitutionView, basename='learninginstitution')
router.register(r'interests', InterestView, basename='interest')

urlpatterns = [
    path('', index),
    path('upload', notesUpload),
    path('api/v1/user/', include(router.urls)),
    path('api/v2/user/<int:pk>/', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
