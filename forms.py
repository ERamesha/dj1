# from django import forms

# class Rollnoform(forms.Form):
#     rollno = forms.CharField(label='RollNo', max_length=30)
#     name = forms.CharField(label='Name', max_length=100)
#     fathername = forms.CharField(label='FatherName', max_length=100)
#     dob = forms.CharField(label='DOB', max_length=100)
#     gender = forms.CharField(label='Gender', max_length=20)
#     bib_r1= forms.CharField(label='bib_r1', max_length=100)
#     chipno_1_R1 = forms.CharField(label='chipno_1_R1', max_length=100)
#     chipno_1_R2 = forms.CharField(label='chipno_1_R2', max_length=20)

from django.db import models  
from django.forms import fields  
  
from django import forms  
  
  
class UserImage(forms.ModelForm):  
    class meta:  
        # To specify the model to be used to create form  
        models = 'UploadImage'  
        # It includes all the fields of model  
        fields = '__all__'  