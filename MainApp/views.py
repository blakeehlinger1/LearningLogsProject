from django.shortcuts import render
from .models import Topic 
# Create your views here.

def index(request):
    return render(request, 'MainApp/index.html')

def topics(request):
    topics = Topic.objects.all()

    context = {'topics':topics}

    return render(request,'MainApp/topics.html', context)
    # key value on line 11: what we use on key is what we use in html and the value is what we use in the view file