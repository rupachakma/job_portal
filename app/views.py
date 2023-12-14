from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from app.forms import *
from app.models import JobApplication
from django.core.exceptions import ValidationError

# Create your views here.
def home(request):
    user = request.user
    if user.is_authenticated:
        print(f"User Type: {request.user.user_type}")
        if user.user_type == 'recruiter':
            templates_name = "recruiter/dashboard.html"

        elif user.user_type == 'jobseeker':
            templates_name = "jobseeker/dashboard.html"
        else:
            return HttpResponse("Invalid User")
    else:
        return HttpResponse("User is not Authenticated")

    return render(request,templates_name)

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("loginpage")
    else:
        form = RegisterForm()
    return render(request,"register.html",{'form':form})

def loginpage(request):
    if request.method == "POST":
        
        form = LoginForm(request=request,data=request.POST)
        print(form)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                user_type = user.user_type
                if user_type == 'recruiter':
                    return redirect("homepage")
                elif user_type == 'jobseeker':
                    return redirect("homepage")
                else:
                    return redirect("homepage")
    else:
        form = LoginForm()
    return render(request,"login.html",{'form':form})

def logoutpage(request):
    logout(request)
    return redirect("loginpage")


def job_post_list(request):
    job_posts = JobPost.objects.all()
    return render(request, 'job_post_list.html', {'job_posts': job_posts})

@login_required
def create_job_post(request):
    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            job_post = form.save(commit=False)
            job_post.recruiter = request.user
            job_post.save()
            return redirect('joblist') 
    else:
        form = JobPostForm()

    return render(request, 'recruiter/create_jobpost.html', {'form': form})

@login_required
def update_job_post(request, id):
    job_post = get_object_or_404(JobPost, id=id)
    
    if request.user == job_post.recruiter:
        if request.method == 'POST':
            form = JobPostForm(request.POST, instance=job_post)
            if form.is_valid():
                form.save()
                return redirect('joblist') 
        else:
            form = JobPostForm(instance=job_post)

        return render(request, 'recruiter/update_jobpost.html', {'form': form})
    else:
        return redirect('homepage')
    
@login_required
def delete_job_post(request, id):
    job_post = get_object_or_404(JobPost, id=id)

    if request.user == job_post.recruiter:
        job_post.delete()
        return redirect('joblist')
    else:
        return redirect('homepage')

def view_job(request):
    job_posts = JobPost.objects.all()
    return render(request,'jobseeker/viewjob.html',{'job_posts': job_posts})

  
# @login_required
# def apply_for_job(request, id):
#     job_post = get_object_or_404(JobPost, id=id)

#     if request.user.user_type == 'jobseeker':
#         if request.method == 'POST':
#             form = ApplyForm(request.POST, request.FILES)
#             if form.is_valid():
#                 form.save()
#                 # Process the form data (save to database, send emails, etc.)
#                 # For simplicity, let's just print the submitted data here
#                 print(f"Full Name: {form.cleaned_data['full_name']}")
#                 print(f"Resume: {request.FILES['resume'].name}")
#                 print(f"Cover Letter: {form.cleaned_data['cover_letter']}")
#                 # Add logic to save the form data to your database or perform other actions
#                 # For example, you could create a JobApplication model to store the applications
#                 # job_application = JobApplication.objects.create(
#                 #     job_post=job_post,
#                 #     applicant=request.user,
#                 #     full_name=form.cleaned_data['full_name'],
#                 #     resume=request.FILES['resume'],
#                 #     cover_letter=form.cleaned_data['cover_letter']
#                 # )
            
#                 return redirect('homepage')  # Change to the URL or view name for the job seeker dashboard
#         else:
#             form = ApplyForm()

#         return render(request, 'jobseeker/apply_job.html', {'form': form, 'job_post': job_post})
#     else:
#         # Redirect or handle the case where the user is not a job seeker
#         return redirect('homepage')

# @login_required
# def apply_for_job(request, id):
#     job_post = get_object_or_404(JobPost, id=id)

#     if request.user.user_type == 'jobseeker':
#         if request.method == 'POST':
#             form = ApplyForm(request.POST, request.FILES)
#             if form.is_valid():
#                 job_application = form.save(commit=False)
#                 job_application.job_post = job_post
#                 job_application.applicant = request.user
#                 job_application.save()
#                 return redirect('homepage') 
#         else:
#             form = ApplyForm()

#         return render(request, 'jobseeker/apply_job.html', {'form': form, 'job_post': job_post})
#     else:

#         return redirect('homepage')

@login_required
def apply_for_job(request, id):
    job = get_object_or_404(JobPost, id=id)

    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job_post = job  # Correct the attribute name to 'job_post'
            application.applicant = request.user
            application.save()
            return redirect('viewjob', id=job.id)
    else:
        form = ApplyForm()

    return render(request, 'jobseeker/apply_job.html', {'form': form, 'job': job})
