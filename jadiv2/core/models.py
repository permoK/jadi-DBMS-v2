from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models import CharField, ManyToManyField, constraints
from django.core.exceptions import ValidationError

# Create your models here.

#################### LearningInstitution ##############################
class LearningInstitution(models.Model):
    institution_id = models.AutoField(primary_key=True, blank=True)
    institution_name = models.CharField(max_length=100, blank=True)

    class Meta:
        db_table = 'learning_institution'

    def __str__(self):
        return self.institution_name
#################### End LearningInstitution ##############################

#################### Interests ##############################
class Interest(models.Model):
    interest_id = models.AutoField(primary_key=True)
    interest_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'interests'

    def __str__(self):
        return self.interest_name
#################### End Interests ##############################

#################### User ##############################
class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    full_name = models.CharField(unique=True, max_length=255)
    email = models.EmailField(unique=True)
    interests = models.ManyToManyField(Interest)
    is_student = models.BooleanField(default=False)
    is_lecturer = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    clerk_id = models.CharField(max_length=255, blank=True, null=True)
    
    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.username

#################### End User ##############################


#################### Course ##############################
class Major(models.Model):
    major_name = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'major'

    def __str__(self):
        return self.major_name
#################### End Course ##############################

#################### UserEducationDetails ##############################
class UserEducationDetails(models.Model):
    oto_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    oto_full_name = models.OneToOneField(User, to_field='full_name', on_delete=models.CASCADE)
    fx_learning_institution = models.ForeignKey(LearningInstitution, on_delete=models.CASCADE)
    fx_student_major = models.ForeignKey(Major, on_delete=models.SET_NULL, null=True, blank=True)
    units = models.JSONField()

    class Meta:
        db_table = 'user_education_details'

    def __str__(self):
        return f'{self.oto_user.username} - {self.fx_learning_institution.institution_name}'

    def clean(self):
        # Ensure oto_full_name matches the full_name of the related User
        if self.oto_full_name != self.oto_user.full_name:
            raise ValidationError({'oto_full_name': 'oto_full_name must match the full_name of the related user.'})

    def save(self, *args, **kwargs):
        # Ensure oto_full_name matches the full_name of the related User
        self.oto_full_name = self.oto_user.full_name
        super().save(*args, **kwargs)

#################### End UserEducationDetails ##############################

#################### Waitlist ##############################
class Waitlist(models.Model):
    # fx_name = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    # fx_major = models.ForeignKey('Major', on_delete=models.CASCADE)
    # created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'waitlist'

    def __str__(self):
        return f'{self.user.username} - {self.course.course_name}'

#################### End Waitlist ##############################


#################### uploads ##################################
class NotesUpload(models.Model):
    title = models.CharField(max_length=100)
    note = models.FileField(upload_to='assets/',)
    
    class Meta:
        db_table = 'notes'

    def __str__(self):
        return f'{self.title }'
################### endUploads #################################

################### resources #################################
class ResourceType(models.Model):
    resource_type_name = models.CharField(max_length=256)

    class Meta:
        db_table = 'resource_types'

    def __str__(self):
        return self.resource_type_name

class Resource(models.Model):
    download_url = models.TextField()
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField(null=True, blank=True)
    size = models.IntegerField()
    cms_id = models.CharField(max_length=256)
    category = models.ForeignKey(Major, on_delete=models.CASCADE)
    resource_type = models.ForeignKey(ResourceType, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'resources'
    # def __str__(self):
    #     return self.uploaded_by

class ResourceTag(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    interest = models.ForeignKey(Interest, on_delete=models.CASCADE)

    class Meta:
        db_table = 'resource_tags'
        unique_together = ('resource', 'interest')

    def __str__(self):
        num = str(self.resource)
        return f"resource - {num}" 

################### end resources #################################

################### Folder ###################################
class Folder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    resources = models.ManyToManyField(Resource)
    
    class Meta:
        db_table = 'folders'

################ End Folder #######################################
