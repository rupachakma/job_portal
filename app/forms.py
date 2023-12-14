from django import forms 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from app.models import CustomUser, JobApplication, JobPost

class RegisterForm(UserCreationForm):
    username = forms.CharField(label="Username",widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    display_name = forms.CharField(max_length=255, required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    user_type = forms.ChoiceField(choices=CustomUser.User_type_choices, required=True)

    class Meta:
        model = CustomUser
        fields = ['username','email','display_name', 'user_type']
        label = {'email':'Email'}
        widgets = {
            'email':forms.EmailInput(attrs={'class':'form-control'})
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username",widget=forms.TextInput(attrs={'class':'form-control'}))
    password = UsernameField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))


class JobPostForm(forms.ModelForm):
    class Meta:
        model = JobPost
        fields = ['title', 'number_of_openings', 'job_description', 'category']
        labels= {'title':'Title','number_of_openings':'Number of Openings','job_description':'Description','category':'Category'}
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'number_of_openings':forms.NumberInput(attrs={'class':'form-control'}),
            'job_description':forms.Textarea(attrs={'class':'form-control'}),
           
        }

class ApplyForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['full_name', 'resume', 'cover_letter']
        labels = {'full_name':'Full Name','resume':'Resume','cover_letter':'Cover Letter'}
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'resume': forms.FileInput(attrs={'class': 'form-control'}), 
            'cover_letter': forms.Textarea(attrs={'class': 'form-control'}),  
        }
        help_texts = {
            'resume': 'Upload your resume (PDF, Word, etc.)',
            'cover_letter':'Write a cover letter explaining your interest in the job',
        }
    
    