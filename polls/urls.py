from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('users/get_user', views.get_user),
    path('users/create_user', views.create_user),
    path('users/change_password', views.change_password),
    path('users/restore_password', views.restore_password),
    path('users/create_new_password', views.create_new_password),
    path('users/login', views.login),
    path('users/logout', views.logout),
    path('users/update_profile', views.update_profile),
    path('users/change_email', views.change_email),
    path('users/donate_history', views.donate_history),
    path('users/current_donations', views.current_donations),
    path('projects/get_projects', views.get_projects),
    path('projects/get_project', views.get_project),
    path('organisations/get_organisations', views.get_organisations),
    path('donaties/donate_organization', views.donate_organization),
    path('donaties/donate_project', views.donate_project),
    path('donaties/delete_donate', views.delete_donate),
    path('country/get_countries', views.get_countries),

]
