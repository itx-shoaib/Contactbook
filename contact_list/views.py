from django.shortcuts import render, redirect
from .models import People

# Create your views here.

# '''In home,we retrieve people data by ordering it by name'''
def home(request):
    contact = People.objects.order_by('name')
    return render(request, 'contact_list/home.html', {'contact': contact})


# In Contact, we get people data by id
def contact(request,id):
    contact = People.objects.get(people_id=id)
    return render(request, 'contact_list/contact.html', {'contact': contact})


# In new_contact, we get data from new_contact.html form and save it
def new_contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        mobile_number = request.POST['mobile_number']
        phone_number = request.POST['phone_number']
        note = request.POST['note']
        contact = People(name=name, email=email, mobile_number=mobile_number, phone_number=phone_number, note=note)
        contact.save()

    return render(request, 'contact_list/new_contact.html')


# In delete, we get data by id and delete it
def delete(request,id):
    contact = People.objects.get(people_id=id)
    contact.delete()
    return redirect('home')


# In edit,we get data by id and these name , email etc variables are used as a value in edit.html for edit purpose
def edit(request, id):
    edit_contact = People.objects.get(people_id=id)
    name = edit_contact.name
    email = edit_contact.email
    mobile_number = edit_contact.mobile_number
    phone_number = edit_contact.phone_number
    note = edit_contact.note
    edit_data = {'id': id,
                 'name': name,
                 'email': email,
                 'mobile_number': mobile_number,
                 'phone_number': phone_number,
                 'note': note}
    return render(request, 'contact_list/edit.html', edit_data)


# In edited_contact,we simply get form data from edit.html and update it.
def edited_contact(request, id):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        mobile_number = request.POST['mobile_number']
        phone_number = request.POST['phone_number']
        note = request.POST['note']

        # Updating the data
        People.objects.filter(people_id=id).update(name=name, email=email, mobile_number=mobile_number, phone_number=phone_number, note=note)
        return redirect('home')

    return render(request, 'contact_list/edit.html')

