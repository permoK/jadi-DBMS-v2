from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from .forms import notesUploadForm
from django.shortcuts import redirect

#Create your views here.


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

class LearningInstitutionView(viewsets.ModelViewSet):
    queryset = LearningInstitution.objects.all()
    serializer_class = LearningInstitutionSerializer

class InterestView(viewsets.ModelViewSet):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MajorView(viewsets.ModelViewSet):
    pass

class UserEducationDetailsView(viewsets.ModelViewSet):
    pass

class WaitlistView(viewsets.ModelViewSet):
    pass

class NotesUploadView(viewsets.ModelViewSet):
    queryset = NotesUpload.objects.all()
    serializer_class = NotesUploadSerializer
    
class ResourceTypeView(viewsets.ModelViewSet):
    pass

class ResourceView(viewsets.ModelViewSet):
    pass

class ResourceTagView(viewsets.ModelViewSet):
    pass


###################### END API SECTION #########################
# Compare this snippet from urls.py:
