from django.db.models.lookups import In
from rest_framework import fields, serializers
from .models import *


class LearningInstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningInstitution
        fields = '__all__'

class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class MajorView():
    class Meta:
        model = Major
        fields = '__all__'

class UserEducationDetailsView():
    class Meta:
        model = UserEducationDetails
        fields = '__all__'

class WaitlistView():
    class Meta:
        model = Waitlist
        fields = '__all__'


class NotesUploadView():
    class Meta:
        model = NotesUpload
        fields = '__all__'

class NotesUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotesUpload
        fields = '__all__'

class ResourceTypeView():
    class Meta:
        model = ResourceType
        fields = '__all__'


class ResourceView():
    class Meta:
        model = Resource
        fields = '__all__'

class ResourceTagView():
    class Meta:
        model = ResourceTag
        fields = '__all__'
# Compare this snippet from views.py:
