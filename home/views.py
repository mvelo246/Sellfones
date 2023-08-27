from django.shortcuts import render
from phone.models import Category,Phone

# Create your views here.
def index(request):
    phones=Phone.objects.filter(is_sold=False)[0:12]
    categories=Category.objects.all()


    return render(request,'home/index.html',{'categories':categories,'phones':phones})
def contact(request):
    return render(request,'home/contact.html')