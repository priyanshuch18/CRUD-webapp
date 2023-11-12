from django.shortcuts import render
from .models import Student
from django.contrib import messages
from django.db.models import Q
# Create your views here.

def index(request):
    students = Student.objects.all()
    query = ""

    if request.method =="POST":
        if 'add' in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            Student.objects.create(
                name = name,
                email = email
            )
            messages.success(request,'student added successfully')
        elif 'update' in request.POST:
            id = request.POST.get('id')
            name = request.POST.get('name')
            email = request.POST.get('email')
 
            update_student = Student.objects.get(id=id)
            update_student.name = name
            update_student.email = email
            update_student.save()
            messages.success(request, 'Updated successfully')
        elif 'delete' in request.POST:
            id = request.POST.get('id')
            delete_student = Student.objects.get(id = id)
            delete_student.delete()

            messages.success(request, 'Deleted successfully')
        elif 'search' in request.POST:
            query = request.POST.get('searchquery') 
            students = Student.objects.filter(Q(name__icontains=query) | Q(email__icontains=query))
             

    context = {'students': students , "query": query}

    return render(request, 'index.html' , context)
