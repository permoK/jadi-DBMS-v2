from http.client import NOT_EXTENDED
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from .models import NotesUpload
from . import views

from rest_framework.authtoken.views import obtain_auth_token

# from . import views

# router = DefaultRouter()
# router.register('user-profile', UserView)
# router.register('learning-institutions', LearningInstitutionView)
# router.register('interests', InterestView)
router = DefaultRouter()
router.register(r'user-profiles', UserView, basename='userprofile')
router.register(r'learning-institutions', LearningInstitutionView, basename='learninginstitution')
router.register(r'interests', InterestView, basename='interest')
router.register(r'notes-upload', NotesUploadView, basename='upload')
router.register(r'major', MajorView, basename='major')
router.register(r'UserEducationDetails', UserEducationDetailsView, basename='UserEducationDetails')
router.register(r'waitlist', WaitlistView, basename='waitlist')
router.register(r'resource-type', ResourceTypeView, basename='resource-type')
router.register(r'resource', ResourceView, basename='resource')
router.register(r'resource-tag', ResourceTagView, basename='resource-tag')

urlpatterns = [
    path('',index),
    path('upload', upload),
    path('api/v1/user/', include(router.urls)),
    path('api/v2/user/<int:pk>/', include(router.urls)),

    # Register user
    path('register/', views.CreateUserView.as_view(), name='register'),

    # Login user
    path('login/', views.CustomLoginView.as_view(), name='login'),
    
    # Get token
    path('token/', views.ObtainAuthTokenView.as_view(), name='token'),


    #api authentication
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
