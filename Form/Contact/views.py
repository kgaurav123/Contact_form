from django.shortcuts import render
from Contact.models import Contact
# Create your views here.

def index(request):
    return render(request,'index.html')

def submit(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content=request.POST['content']
        print(name, email, phone, content)
        contact=Contact(name=name, email=email, phone=phone, content=content)
        contact.save()
    return render(request,'submit.html')