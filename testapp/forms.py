# from django import forms
# class FeedBackForm(forms.Form):
#     name = forms.CharField()
#     rollno = forms.IntegerField()
#     email = forms.EmailField()
#     feedback = forms.CharField(widget=forms.Textarea)
#
# # 1) Form Validation :--> Explicitly by the programmer by using 'clean methods'
# # Case - 2
#
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
#
# #=======================================================================================================================
# # 2). Form Validation :--> By using in-built validators:
# # Case - 3:
#
# from django.core import validators
#     validators=[validators.MaxLengthValidator(40),validators.MinLengthValidator(10)]
#
# from django.core import validators
# from django import forms
# class FeedBackForm(forms.Form):
#     name = forms.CharField()
#     rollno = forms.IntegerField()
#     email = forms.EmailField()
#     feedback = forms.CharField(widget=forms.Textarea, validators=[validators.MaxLengthValidator(40), validators.MinLengthValidator(10)]) #--> Case - 3: Validating by inbuilt Validator(from django.core import Validator)
#
# #=======================================================================================================================
# #Case - 4:
# #How to implement custom validators by using validators parameter?
# #The name should be starts with 's' or 'S'
#
# from django.core import validators
# from django import forms
#
# def starts_with_s(value):
#     print('starts_with_s function execution')
#     if value[0].lower() != 's':
#         raise forms.ValidationError('Name should be starts with s or S')
#
# class FeedBackForm(forms.Form):
#     name = forms.CharField(validators=[starts_with_s])
#     rollno = forms.IntegerField()
#     email = forms.EmailField()
#     feedback = forms.CharField(widget=forms.Textarea)
#
# #----------------------------------------------------------------------------
#
# #The name should be starts with 's' or 'S'
# # mail should contain @gmail.com
#
# from django.core import validators
# from django import forms
#
# def starts_with_s(value):
#     print('starts_with_s function execution')
#     if value[0].lower() != 's':
#         raise forms.ValidationError('Name should be starts with s or S')
#
# def gmail_validator(value):
#     print('Checking for gmail validation')
#     if value[-10:] != '@gmail.com':
#         raise forms.ValidationError('Mail extension should be gmail')
#
# class FeedBackForm(forms.Form):
#     name = forms.CharField(validators=[starts_with_s])
#     rollno = forms.IntegerField()
#     email = forms.EmailField(validators=[gmail_validator])
#     feedback = forms.CharField(widget=forms.Textarea)
#
#
# #=======================================================================================================================
#
# # Case - 5:
# # Validation of total form directly by using single clean() method
#
# from django.core import validators
# from django import forms
#
# class FeedBackForm(forms.Form):
#     name = forms.CharField()
#     rollno = forms.IntegerField()
#     email = forms.EmailField()
#     feedback = forms.CharField(widget=forms.Textarea)
#
#     def clean(self):
#         print('Total form validation.....')
#         total_cleaned_data = super().clean()
#         print('Validating Name')
#         inputname = total_cleaned_data['name']
#         if inputname[0].lower() != 's':
#             raise forms.ValidationError('Name should starts with s')
#         print('Validating Rollno')
#         inputrollno = total_cleaned_data['rollno']
#         if inputrollno <= 0:
#             raise forms.ValidationError('Rollno should be > 0')
#         print('Validating Email')
#         inputemail = total_cleaned_data['email']
#         if inputemail[-10:] != '@gmail.com':
#             raise forms.ValidationError('Email extension should be gmail')
#
# # =======================================================================================================================
#
# # Case - 6:
# # How to check original pwd and re-entered pwd are same or not?
#
# from django.core import validators
# from django import forms
#
# class FeedBackForm(forms.Form):
#     name = forms.CharField()
#     password = forms.CharField(label='Enter Password', widget=forms.PasswordInput) # widget=forms.PasswordInput: secure the password characters
#     rpassword = forms.CharField(label='Password(Again)', widget=forms.PasswordInput)
#     email = forms.EmailField()
#
#     def clean(self):
#         cleaned_data = super().clean() # Django removes a field from cleaned_data if that field is invalid or empty.
#         pwd = cleaned_data.get('password') # ALWAYS use .get() inside clean(): Returns value if key exists . Returns None if key does NOT exist .Does NOT crash
#         rpwd = cleaned_data.get('rpassword')
#
#         if pwd and rpwd and pwd != rpwd:
#             raise forms.ValidationError('Both passwords must be same.....')
#
#         return cleaned_data
#
# # ===================================================================================================================

"""How to prevent request from BOT:
----------------------------------------------------
-->Generally form requests can be send by end user. Sometimes we can write automated programming script which is responsible to fill the form and submit. This automated script is nothing but BOT.

The main objective of BOT requests are:
	1).To create unneccessary heavy trafic to the website, which may crash our application.
	2).To spread malware(viruses)
-->Being a developer compulsory we have to think about BOT request and we have to prevent these request.

How to prevent?
------------------------
-->In the form we will place one hidden field, which is not visible to the end user, hence there is no chance of providing value to this hidden field.
-->But BOT will send the value for this hidden field also. If hidden field got some value means it is the request from BOT and prevent that submission."""

from django import forms

class FeedBackForm(forms.Form):
    name = forms.CharField()
    rollno = forms.IntegerField()
    email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea)
    bot_handler = forms.CharField(required=False, widget=forms.HiddenInput)

    def clean(self):
        total_cleaned_data = super().clean()
        bot_handler_value = total_cleaned_data['bot_handler']
        if len(bot_handler_value) > 0:
            raise forms.ValidationError("Request from BOT.....Can't be submitted")
