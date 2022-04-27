from django.shortcuts import redirect, render
from .models import Topic 
from .forms import TopicForm
# Create your views here.

def index(request):
    return render(request, 'MainApp/index.html')

def topics(request):
    topics = Topic.objects.all()

    context = {'topics':topics}

    return render(request,'MainApp/topics.html', context)
    # key value on line 11: what we use on key is what we use in html and the value is what we use in the view file
#be consistent in view how we used topic_id in the urls.py
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    #variable on url page is what we use for key
    context = {'topic':topic,'entries':entries}
    # context is a dictionary
    return render(request, 'MainApp/topic.html', context)
    #get and post 

def new_topic(request):
    if request.method != 'POST':
        form = TopicForm
    else:
        form = TopicForm(data=request.POST)

        if form.is_valid():
            new_topic = form.save()

            return redirect('MainApp:topics')

    context = {'form':form}
    return render(request, 'MainApp/new_topic.html', context)