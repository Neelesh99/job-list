from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name="list"),
    path('applications', views.applicationPage, name='applicationsDash'),
    path('applications/create', views.addApplication, name='createApplication'),
    path('applications/delete/<str:pk>', views.deleteApplication, name='deleteApplication'),
    path("update_task/<str:pk>/", views.updateTask, name="update_task"),
    path("delete/<str:pk>/", views.deleteTask, name="delete"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/newUser", views.createUserPage, name="createUser")
]