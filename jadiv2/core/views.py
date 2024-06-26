import re
from django.shortcuts import render
from django.template import context
from rest_framework import viewsets, generics, permissions
from .models import *
from .serializers import *
from .forms import notesUploadForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import cache_page

#DRF authentication modules
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# DRF authtoken
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


# django login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from rest_framework.views import APIView

#Create your views here.

# Register new user
class CreateUserView(generics.CreateAPIView):
    serializer_class = AuthUserSerializer
    permission_classes = [permissions.AllowAny]

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'login success')
            return redirect('index')  # Redirect to profile page after registration
    else:
        form = UserCreationForm()
        context = {"form":form, "error":form.errors}
    context = {"form":form}
    return render(request, 'accounts/register.html', context)

# Login user
def login_view(request):
    if request.method == 'POST':
        # Handle login form submission
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            # Redirect to a specific URL after login
            return redirect('index')  # Replace 'home' with your desired URL name
        else:
            # Handle invalid login
            # Add error message or other handling as needed
            messages.error(request,'invalid username or password')
            return redirect('login')
    else:
        # Display login form
        message = messages.get_messages(request)
        return render(request, 'accounts/login.html', {'messages':message})
# class CustomLoginView(LoginView):
#     template_name = 'accounts/login.html'
#     # success_url = reverse_lazy('index')
#     reverse_lazy('index')

# Get token
class GetTokenView(LoginRequiredMixin, TemplateView):
    template_name = 'get_token.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        token, created = Token.objects.get_or_create(user=self.request.user)
        context['token'] = token.key
        return context

@login_required
def get_token(request):
    token, created = Token.objects.get_or_create(user=request.user)
    return render(request, 'get_token.html', {'token': token.key})


# Profile
@login_required
def profile(request):
    user = request.user
    token = Token.objects.get(user=user)
    context = {
                'user':user,
                'token':token
            }
    return render(request, 'accounts/profile.html', context)

# Logout 
def logout_view(request):
    logout(request)
    # Redirect to a success page
    return redirect('index')  


def index(request):
    context = {
        'is_authenticated':request.user.is_authenticated
            }
    return render(request, 'index.html', context)

# django auth views
class MyProtectedView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Your view logic here
        return Response({"message": "Authenticated!"})



def upload(request):
    form = notesUploadForm()
    if request.method == 'POST':
        form = notesUploadForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect(index)
    return render(request, 'upload.html',{'form':form})



###################### API SECTION #########################
@method_decorator(csrf_exempt, name='dispatch')
@method_decorator(cache_page(60 * 60 * 0.2), name='dispatch')  # Cache for 1 day
class LearningInstitutionView(viewsets.ModelViewSet):
    queryset = LearningInstitution.objects.all()
    serializer_class = LearningInstitutionSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

@method_decorator(cache_page(60 * 60 * 0.2), name='dispatch')  # Cache for 1 day
class InterestView(viewsets.ModelViewSet):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

@method_decorator(cache_page(60 * 60 * 0.2), name='dispatch')  # Cache for 1 day
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

@method_decorator(cache_page(60 * 60 * 0.2), name='dispatch')  # Cache for 1 day
class MajorView(viewsets.ModelViewSet):
    queryset = Major.objects.all()
    serializer_class = MajorSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

@method_decorator(cache_page(60 * 60 * 0.2), name='dispatch')  # Cache for 1 day
class UserEducationDetailsView(viewsets.ModelViewSet):
    queryset = UserEducationDetails.objects.all()
    serializer_class = UserEducationDetailsSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

@method_decorator(cache_page(60 * 60 * 0.2), name='dispatch')  # Cache for 1 day
class WaitlistView(viewsets.ModelViewSet):
    queryset = Waitlist.objects.all()
    serializer_class = WaitlistSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

@method_decorator(cache_page(60 * 60 * 0.2), name='dispatch')  # Cache for 1 day
class NotesUploadView(viewsets.ModelViewSet):
    queryset = NotesUpload.objects.all()
    serializer_class = NotesUploadSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    
@method_decorator(cache_page(60 * 60 * 0.2), name='dispatch')  # Cache for 1 day
class ResourceTypeView(viewsets.ModelViewSet):
    queryset = ResourceType.objects.all()
    serializer_class = ResourceTypeSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

@method_decorator(cache_page(60 * 60 * 0.2), name='dispatch')  # Cache for 1 day
class ResourceView(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

@method_decorator(cache_page(60 * 60 * 0.2), name='dispatch')  # Cache for 1 day
class ResourceTagView(viewsets.ModelViewSet):
    queryset = ResourceTag.objects.all()
    serializer_class = ResourceTagSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]


###################### END API SECTION #########################
# Compare this snippet from urls.py:
