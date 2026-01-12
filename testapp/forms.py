# from django import forms
# class FeedBackForm(forms.Form):
#     name = forms.CharField()
#     rollno = forms.IntegerField()
#     email = forms.EmailField()
#     feedback = forms.CharField(widget=forms.Textarea)

# 1) Form Validation :--> Explicitly by the programmer by using 'clean methods'
# Case - 2

# from django import forms
# class FeedBackForm(forms.Form):
#     name = forms.CharField()
#     rollno = forms.IntegerField()
#     email = forms.EmailField()
#     feedback = forms.CharField(widget=forms.Textarea)
#
#     def clean_name(self):
#         print('Validating name field')
#         inputname = self.cleaned_data['name']
#         if len(inputname) < 4:
#             raise forms.ValidationError('The minimum number of character in the name field should be 4')
#         return inputname
#
#     def clean_rollno(self):
#         print('Validating rollno field')
#         inputrollno = self.cleaned_data['rollno']
#         return inputrollno
#
#     def clean_email(self):
#         print('Validating email field')
#         inputemail = self.cleaned_data['email']
#         return inputemail
#
#     def clean_feedback(self):
#         print('Validating feedback field')
#         inputfeedback = self.cleaned_data['feedback']
#         return inputfeedback

#=======================================================================================================================
# 2). Form Validation :--> By using in-built validators:
# Case - 3:

# from django.core import validators
#     validators=[validators.MaxLengthValidator(40),validators.MinLengthValidator(10)]

from django.core import validators
from django import forms
class FeedBackForm(forms.Form):
    name = forms.CharField()
    rollno = forms.IntegerField()
    email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea, validators=[validators.MaxLengthValidator(40), validators.MinLengthValidator(10)]) #--> Case - 3: Validating by inbuilt Validator(from django.core import Validator)