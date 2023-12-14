from django.urls import path

from app import views 

urlpatterns = [
    path('',views.home,name="homepage"),
    path('register',views.register,name="register"),
    path('viewjob',views.view_job,name="viewjob"),
    path('login',views.loginpage,name="loginpage"),
    path('logout',views.logoutpage,name="logoutpage"),
    path('joblist',views.job_post_list,name="joblist"),
    path('createjob',views.create_job_post,name="createjob"),
    path('updatejob/<int:id>',views.update_job_post,name="updatejob"),
    path('deletejob/<int:id>',views.delete_job_post,name="deletejob"),
    path('job/<int:id>/apply/', views.apply_for_job, name='applyjob'),
  
]
