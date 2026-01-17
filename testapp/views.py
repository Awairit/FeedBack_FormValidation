#Case - 1: Simple FeedBack Form

# from django.shortcuts import render
# from testapp.forms import *
#
# # Create your views here.
# def feedback_view(request):
#     submitted = False
#     name = ''
#     if request.method == 'POST':
#         form = FeedBackForm(request.POST)
#         if form.is_valid():
#             print('Form validation success and printing feedback information')
#             print('*'*50)
#             print('Name:',form.cleaned_data['name'])
#             print('RollNo:',form.cleaned_data['rollno'])
#             print('Email ID:',form.cleaned_data['email'])
#             print('Feedback:',form.cleaned_data['feedback'])
#             submitted = True
#             name = form.cleaned_data['name']
#     form = FeedBackForm()
#     return render(request,'testapp/feedback.html',
# 	{'form':form,'submitted':submitted,'name':name})

#=======================================================================================================================

#Case - 2:
##1) Form Validation :--> Explicitly by the programmer by using 'clean methods'

# from django.shortcuts import render
# from testapp.forms import *
#
# # Create your views here.
# def feedback_view(request):
#     form = FeedBackForm() # ------------------------------------>  # Case - 2
#     submitted = False
#     name = ''
#     if request.method == 'POST':
#         form = FeedBackForm(request.POST)
#         if form.is_valid():
#             print('Form validation success and printing feedback information')
#             print('*'*50)
#             print('Name:',form.cleaned_data['name'])
#             print('RollNo:',form.cleaned_data['rollno'])
#             print('Email ID:',form.cleaned_data['email'])
#             print('Feedback:',form.cleaned_data['feedback'])
#             submitted = True
#             name = form.cleaned_data['name']
#         else:                                                       # Case - 2:
#             print('Form validation failed try properly')            # Case - 2:
#             print('*'*50)
#                                                                     # Case - 2:empty form should be first
#     return render(request,'testapp/feedback.html',
# 	{'form':form,'submitted':submitted,'name':name})

#=======================================================================================================================

# Case - 3, 4, 5:
# 2). Form Validation :--> By using in-built validators:

from django.shortcuts import render
from testapp.forms import *

def feedback_view(request):
    form = FeedBackForm()
    submitted = False
    name = ''
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        if form.is_valid():
            print('Form validation success and printing feedback information')
            print('*'*50)
            print('Name:',form.cleaned_data['name'])
            print('RollNo:',form.cleaned_data['rollno'])
            print('Email ID:',form.cleaned_data['email'])
            print('Feedback:',form.cleaned_data['feedback'])
            submitted = True
            name = form.cleaned_data['name']
    return render(request,'testapp/feedback.html',
	{'form':form,'submitted':submitted,'name':name})