from .models import *
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

class LeaveForm(ModelForm):
    
    class Meta:
        model = Leave
        fields = ['cause_of_leave',
                    'start_date',
                    'end_date',]

        widgets = {
            'cause_of_leave':forms.TextInput(attrs = 
            {'class':'form-control bg-light badge-pill p-2', 
            'placeholder':'Enter Cause of Leave'}),
            
            'start_date':forms.DateInput(format=('%d/%m/%y'), attrs=
            {'class':'form-control bg-light badge-pill p-2','type':'date'}),

            'end_date':forms.DateInput(format=('%d/%m/%y'), attrs=
            {'class':'form-control bg-light badge-pill p-2','type':'date'})
        
        }
        

class TaskForm(ModelForm):
    class Meta:
        model = DailyTask
        fields = ['title',
                    'description',]
        
        widgets = {
            'title':forms.TextInput(attrs = 
            {'class':'form-control bg-light badge-pill p-2', 
            'placeholder':'Enter Your Task Title'}),

            'description':forms.TextInput(attrs = 
            {'class':'form-control bg-light badge-pill p-2', 
            'placeholder':'Enter Your Task Description '}),

        }


class EmployeeForm(ModelForm):
    department=forms.ModelChoiceField(widget=forms.Select(attrs = 
                {'class':'form-control bg-light badge-pill ' 
                }),queryset = Department.objects.all(),empty_label='Select Department')

    district=forms.ModelChoiceField(widget=forms.Select(attrs = 
                {'class':'form-control bg-light badge-pill'
                
                }),queryset = District.objects.all(),empty_label='Select District')
                
    username=forms.ModelChoiceField(widget=forms.Select(attrs = 
                {'class':'form-control bg-light badge-pill ',
                'placeholder':'Select User Name'}),queryset = User.objects.all(),empty_label='Select User Name')

    post=forms.ModelChoiceField(widget=forms.Select(attrs = 
                {'class':'form-control bg-light badge-pill ',
                'placeholder':'Select Post'}),queryset = Post.objects.all(),empty_label='Select User Name')

    class Meta:
        model = Employee
        fields = ['username',
                    'employee_id',
                    'department',
                    'district',
                    'post',
                    'selary',
                    'full_name',
                    'email',
                    'ssc',
                    'hsc',
                    'honors',
                    'masters',
                    'nid',
                    'image',
                    'phone',
                    'father_name',
                    'mother_name']
        
        widgets = {
            

            'employee_id':forms.TextInput(attrs = 
            {'class':'form-control bg-light badge-pill p-2', 
            'placeholder':'Enter Employee Id'}),

            'ssc':forms.TextInput(attrs = 
            {'class':'form-control bg-light badge-pill p-2', 
            'placeholder':'Enter S.S.C Result'}),

            'hsc':forms.TextInput(attrs = 
            {'class':'form-control bg-light badge-pill p-2', 
            'placeholder':'Enter H.S.C Result'}),

            'honors':forms.TextInput(attrs = 
            {'class':'form-control bg-light badge-pill p-2', 
            'placeholder':"Enter Honor's Result"}),

            'masters':forms.TextInput(attrs = 
            {'class':'form-control bg-light badge-pill p-2', 
            'placeholder':"Enter Master's Result"}),

            'selary':forms.TextInput(attrs = 
            {'class':'form-control bg-light badge-pill p-2', 
            'placeholder':"Enter Selary"}),

            'nid':forms.TextInput(attrs = 
            {'class':'form-control bg-light badge-pill p-2', 
            'placeholder':"Enter NID Number"}),

            'full_name':forms.TextInput(attrs = 
            {'class':'form-control bg-light badge-pill p-2', 
            'placeholder':'Enter Full Name'}),

            'email':forms.TextInput(attrs = 
            {'class':'form-control bg-light badge-pill p-2', 
            'placeholder':'Enter Email'}),

            'phone':forms.TextInput(attrs = 
            {'class':'form-control bg-light badge-pill p-2', 
            'placeholder':'Enter Your Phone Number'}),

            'father_name':forms.TextInput(attrs = 
            {'class':'form-control bg-light badge-pill p-2', 
            'placeholder':'Enter Father Name'}),

            'mother_name':forms.TextInput(attrs = 
            {'class':'form-control bg-light badge-pill p-2', 
            'placeholder':'Enter Mother Name'}),

            

        }
class EditEmployeeForm(ModelForm):
    department=forms.ModelChoiceField(widget=forms.Select(attrs = 
                {'class':'form-control bg-light badge-pill ' 
                }),queryset = Department.objects.all(),empty_label='Select Department')

    district=forms.ModelChoiceField(widget=forms.Select(attrs = 
                {'class':'form-control bg-light badge-pill'
                
                }),queryset = District.objects.all(),empty_label='Select District')
                
    
    post=forms.ModelChoiceField(widget=forms.Select(attrs = 
                {'class':'form-control bg-light badge-pill ',
                'placeholder':'Select Post'}),queryset = Post.objects.all(),empty_label='Select User Name')

    class Meta:
        model = Employee
        fields = [
                    'employee_id',
                    'department',
                    'district',
                    'post',
                    'selary',
                    'full_name',
                    'email',
                    'ssc',
                    'hsc',
                    'honors',
                    'masters',
                    'nid',
                    'image',
                    'phone',
                    'father_name',
                    'mother_name']
        
        widgets = {
            

            'employee_id':forms.TextInput(attrs = 
            {'class':'form-control bg-light badge-pill p-2', 
            'placeholder':'Enter Employee Id'}),

            'ssc':forms.TextInput(attrs = 
            {'class':'form-control bg-light badge-pill p-2', 
            'placeholder':'Enter S.S.C Result'}),

            'hsc':forms.TextInput(attrs = 
            {'class':'form-control bg-light badge-pill p-2', 
            'placeholder':'Enter H.S.C Result'}),

            'honors':forms.TextInput(attrs = 
            {'class':'form-control bg-light badge-pill p-2', 
            'placeholder':"Enter Honor's Result"}),

            'masters':forms.TextInput(attrs = 
            {'class':'form-control bg-light badge-pill p-2', 
            'placeholder':"Enter Master's Result"}),

            'selary':forms.TextInput(attrs = 
            {'class':'form-control bg-light badge-pill p-2', 
            'placeholder':"Enter Selary"}),

            'nid':forms.TextInput(attrs = 
            {'class':'form-control bg-light badge-pill p-2', 
            'placeholder':"Enter NID Number"}),

            'full_name':forms.TextInput(attrs = 
            {'class':'form-control bg-light badge-pill p-2', 
            'placeholder':'Enter Full Name'}),

            'email':forms.TextInput(attrs = 
            {'class':'form-control bg-light badge-pill p-2', 
            'placeholder':'Enter Email'}),

            'phone':forms.TextInput(attrs = 
            {'class':'form-control bg-light badge-pill p-2', 
            'placeholder':'Enter Your Phone Number'}),

            'father_name':forms.TextInput(attrs = 
            {'class':'form-control bg-light badge-pill p-2', 
            'placeholder':'Enter Father Name'}),

            'mother_name':forms.TextInput(attrs = 
            {'class':'form-control bg-light badge-pill p-2', 
            'placeholder':'Enter Mother Name'}),

            

        }


class MeetingForm(ModelForm):
    
    class Meta:
        model = Meeting
        fields = ['name',
                    'meeting_date',
                    'meeting_time',]

        widgets = {
            'name':forms.TextInput(attrs = 
            {'class':'form-control bg-light badge-pill p-2', 
            'placeholder':'Enter Name'}),
            
            'meeting_date':forms.DateInput(format=('%d/%m/%y'), attrs=
            {'class':'form-control bg-light badge-pill p-2','type':'date'}),

            'meeting_time':forms.TimeInput(format=('%H:%M'), attrs={'type': 'time',
            'class':'form-control bg-light badge-pill'})
        
        }


class ClientForm(ModelForm):

    class Meta:
        model = Client
        fields = ['client_name',
                'client_id',
                'company_name',
                'email',
                'nid',
                'phone',
                'image',
                ]

        widgets = {
            'client_name': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2',
            'placeholder': 'Enter Client Name'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2',
            'placeholder': 'Enter Client Name'}),

            'client_id': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2',
            'placeholder': 'Enter Client Id'}),
            'nid': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2',
                                        'placeholder': "Enter NID Number"}),

            'email': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2',
                                            'placeholder': 'Enter Email'}),

            'phone': forms.TextInput(attrs={'class': 'form-control bg-light badge-pill p-2',
                                            'placeholder': 'Enter Your Phone Number'}),
        }