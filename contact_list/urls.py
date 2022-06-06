# We have created this file by our own
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/<int:id>', views.contact, name='contact'),  #For showing contact list
    path('new_contact/', views.new_contact, name='new-contact'),  #For adding new contacts
    path('delete/<int:id>', views.delete, name='delete'),  #For delete a contact
    path('edit/<int:id>', views.edit, name='edit'),  #For edit a contact
    path('edited_contact/<int:id>', views.edited_contact, name='edited-contact'),  #For savinng a edit contact
]
