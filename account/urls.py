from . import views
from django.urls import path

urlpatterns = [
    path("home/",views.home, name='home'),
    path("signup/", views.signup, name='signup'),
    path('edit_entry/cint:entry_id>/', views.edit_entry, name='edit_entry'),
]
