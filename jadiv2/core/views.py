from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from .forms import notesUploadForm
#Create your views here.


def index(request):
    return render(request, 'index.html')

def notesUpload(request):
    form = notesUploadForm()
    if request.method == 'POST':
        form = notesUploadForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'upload.html',{'form':form})

# class UserView(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        institution = self.request.query_params.get('institution', None)
        interest = self.request.query_params.get('interest', None)
        
        if institution is not None:
            queryset = queryset.filter(institution__id=institution)
        if interest is not None:
            queryset = queryset.filter(interests__id=interest)
        
        return queryset

class LearningInstitutionView(viewsets.ModelViewSet):
    queryset = LearningInstitution.objects.all()
    serializer_class = LearningInstitutionSerializer


class InterestView(viewsets.ModelViewSet):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer

# Compare this snippet from urls.py:
