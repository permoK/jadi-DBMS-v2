from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from .forms import notesUploadForm
from django.shortcuts import redirect

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

#DRF authentication modules
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

#Create your views here.

# django auth views
class MyProtectedView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Your view logic here
        return Response({"message": "Authenticated!"})


def index(request):
    return render(request, 'index.html')

def upload(request):
    form = notesUploadForm()
    if request.method == 'POST':
        form = notesUploadForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect(index)
    return render(request, 'upload.html',{'form':form})

###################### API SECTION #########################

@method_decorator(cache_page(60 * 60 * 0.2), name='dispatch')  # Cache for 1 day
class LearningInstitutionView(viewsets.ModelViewSet):
    queryset = LearningInstitution.objects.all()
    serializer_class = LearningInstitutionSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

@method_decorator(cache_page(60 * 60 * 0.2), name='dispatch')  # Cache for 1 day
class InterestView(viewsets.ModelViewSet):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer

@method_decorator(cache_page(60 * 60 * 0.2), name='dispatch')  # Cache for 1 day
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@method_decorator(cache_page(60 * 60 * 0.2), name='dispatch')  # Cache for 1 day
class MajorView(viewsets.ModelViewSet):
    queryset = Major.objects.all()
    serializer_class = MajorSerializer

@method_decorator(cache_page(60 * 60 * 0.2), name='dispatch')  # Cache for 1 day
class UserEducationDetailsView(viewsets.ModelViewSet):
    queryset = UserEducationDetails.objects.all()
    serializer_class = UserEducationDetailsSerializer

@method_decorator(cache_page(60 * 60 * 0.2), name='dispatch')  # Cache for 1 day
class WaitlistView(viewsets.ModelViewSet):
    queryset = Waitlist.objects.all()
    serializer_class = WaitlistSerializer

@method_decorator(cache_page(60 * 60 * 0.2), name='dispatch')  # Cache for 1 day
class NotesUploadView(viewsets.ModelViewSet):
    queryset = NotesUpload.objects.all()
    serializer_class = NotesUploadSerializer
    
@method_decorator(cache_page(60 * 60 * 0.2), name='dispatch')  # Cache for 1 day
class ResourceTypeView(viewsets.ModelViewSet):
    queryset = ResourceType.objects.all()
    serializer_class = ResourceTypeSerializer

@method_decorator(cache_page(60 * 60 * 0.2), name='dispatch')  # Cache for 1 day
class ResourceView(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

@method_decorator(cache_page(60 * 60 * 0.2), name='dispatch')  # Cache for 1 day
class ResourceTagView(viewsets.ModelViewSet):
    queryset = ResourceTag.objects.all()
    serializer_class = ResourceTagSerializer


###################### END API SECTION #########################
# Compare this snippet from urls.py:
