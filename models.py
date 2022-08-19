from asyncio.windows_events import NULL
from unittest.mock import DEFAULT
import uuid
from django.db import models

# Create your models here.
from pickle import TRUE
from django.db import models

# Create your models here.
class Result1(models.Model):
    rollno = models.CharField(db_column='RollNo', primary_key=True, max_length=30)
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fathername = models.CharField(db_column='FatherName', max_length=100, blank=True, null=True)
    dob = models.CharField(db_column='', max_length=20, blank=True, null=True)
    bib_r1 = models.CharField(db_column='Bib_R1', blank=True, null=True,max_length=20)
    chipno_1_R1 = models.CharField(db_column='chipno_1_R1', max_length=10, blank=True, null=True)
    chipno_1_R2 = models.CharField(db_column='chipno_1_R2', max_length=10, blank=True, null=True)
    gender = models.CharField(db_column='Gender', max_length=20, blank=True, null=True)
    

    class Meta:
        db_table = 'Result1'
        managed = TRUE
        
class Imagedata(models.Model):
    # id = models.AutoField()
    uuid=models.UUIDField(primary_key=TRUE,default=uuid.uuid4,editable=False)
    rollno = models.CharField(max_length=50, blank=True, null=True)
    candidate_photo = models.TextField(blank=True, null=True)
    imagedata = models.TextField(blank=True, null=True)
    ltiimagedata = models.TextField(blank=True, null=True)  # This field type is a guess.
    rtiimagedata = models.TextField(blank=True, null=True)  # This field type is a guess.
    lti_iso = models.TextField(blank=True, null=True)
    rti_iso = models.TextField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = TRUE
        db_table = 'ImageData'