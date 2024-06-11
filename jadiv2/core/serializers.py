from django.db.models.lookups import In
from rest_framework import fields, serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class LearningInstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningInstitution
        fields = '__all__'


class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = '__all__'

class NotesUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotesUpload
        fields = '__all__'

# Compare this snippet from views.py:
