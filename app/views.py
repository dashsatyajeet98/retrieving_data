import webbrowser
from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q
# Create your views here.  
def display_topic(request):
    T=Topic.objects.all()
    d={'topics':T}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    W=Webpage.objects.all()
    #W=Webpage.objects.filter(topic_name='Cricket')
    #W=Webpage.objects.exclude(topic_name='Cricket')
    #W=Webpage.objects.all().order_by('name')
    #W=Webpage.objects.all().order_by('-name')
    #W=Webpage.objects.filter(topic_name='cricket').order_by('name')
    #W=Webpage.objects.filter(topic_name='Cricket')
    #W=Webpage.objects.order_by(Length('name'))
    #W=Webpage.objects.order_by(Length('name').desc())
    #W=Webpage.objects.all()[:4:]
    W=Webpage.objects.filter(name__startswith='b')
    W=Webpage.objects.filter(name__endswith='a')
    W=Webpage.objects.filter(name__contains='b')
    W=Webpage.objects.filter(name__in=('satya','biswa'))
    W=Webpage.objects.filter(name__regex='\w{5}')
    W=Webpage.objects.filter(Q(topic_name='cricket') | Q(topic_name='kabadi'))

    d={'webpages':W}
    return render(request,'display_webpage.html',d)

def display_accessRecords(request):
    A=AccessRecords.objects.all()
    A=AccessRecords.objects.filter(date__year=2022)
    A=AccessRecords.objects.filter(date__month=10)
    A=AccessRecords.objects.filter(date__day=5)
    A=AccessRecords.objects.filter(date='2021-10-3')
    A=AccessRecords.objects.filter(date__gt='2021-10-3')
    A=AccessRecords.objects.filter(date__gte='2021-10-3')
    A=AccessRecords.objects.filter(date__lte='2019-11-5')
    A=AccessRecords.objects.filter(date__year__gt='2019')
    d={'accessRecords':A}
    return render(request,'display_accessRecords.html',d)