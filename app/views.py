from django.shortcuts import render
from app.models import *
# Create your views here.
from django.http import HttpResponse
from django.db.models.functions import Length
from django.db.models import Q



# def insert_topic(request):
#     tn=input("Enter Topic Name:- ")
#     TO=Topic.objects.get_or_create(topic_name=tn)[0]
#     TO.save()
#     return HttpResponse("topic is created")

def insert_topic(request):
    tn = input('Enter Topic Name:- ')  # Prompt user to enter a topic name

    TTO = Topic.objects.get_or_create(topic_name=tn)  # Retrieve or create the topic
    bl = TTO[1]  # Extract the boolean value indicating creation status
    if bl:
        TO = TTO[0]  # Extract the Topic object
        TO.save()  # Save the object (though this is unnecessary if it was just created)
        # return HttpResponse(f'{tn} Topic is created')
        d={'topics':Topic.objects.all()}
        return render(request,'retrieve_topics.html',d)
    else:
        return HttpResponse(f'{tn} Topic is already present')


def insert_webpage(request):
    tn = input('Enter Topic Name:- ')
    QLTO=Topic.objects.filter(topic_name=tn)
    if QLTO:
        TO=QLTO[0]
        na=input('Enter Name')
        url=input('Enter URL')
        email=input('Enter Email')

        WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=url,email=email)[0]
        WO.save()
        return HttpResponse('Webpage is created')
    else:
        return HttpResponse('Topic is not there so i cant create ur webepage object')
    
def insert_access(request):
    ID=input('Enter ID:- ')
    QLIO = Webpage.objects.filter(id=ID)
    if QLIO:
        IO=QLIO[1]
        au=input('Enter Author Name:- ')
        dt=input('Enter the Date:- ')

        AO=AccessRecord.objects.get_or_create(name=IO,author=au,date=dt)[0]
        AO.save()
        return HttpResponse('Record is created')
    else:
        return HttpResponse('NO matching Id found, so i cant create access record')

def retrieve_topics(request):
    d={'topics':Topic.objects.all()}
    return render(request,'retrieve_topics.html',d)

def retrieve_webpages(request):
    QLWO=Webpage.objects.all()  # all objects
    # QLWO=Webpage.objects.values('') # give the values we want to display based on column name
    QLWO=Webpage.objects.filter(topic_name='cricket') # it will give cricket satisfying condition
    QLWO=Webpage.objects.exclude(topic_name='cricket') # it will not give cricket satisfying condition
    QLWO=Webpage.objects.all()[::-1] # performing slicing to get the data in desc order
    QLWO=Webpage.objects.all().order_by('name') #sorts name based on asceinding order of ASCII Values
    QLWO=Webpage.objects.filter(topic_name='cricket').order_by('name') #display on cricket data and sorts by name in ascending order
    QLWO=Webpage.objects.all().order_by('-name') # sorts name in descending order of ASCII Values
    QLWO=Webpage.objects.all().order_by(Length('name')) # sorts name based on length of the string
    QLWO=Webpage.objects.all().order_by(Length('name').desc()) # sorts name in descending order based on length of the string
    QLWO=Webpage.objects.filter(name__startswith='ro') # checks if string is starting with given substring
    QLWO=Webpage.objects.filter(email__endswith='com') # checks if string is ending with given substring
    QLWO=Webpage.objects.filter(url__in=('https://rohit.com','https://messi.com')) # checks for multiple condition 
    QLWO=Webpage.objects.filter(name__regex=r't$') # checks if the substring ends with t
    QLWO=Webpage.objects.filter(name__regex=r'^r') # checks if the substring starts with r
    QLWO=Webpage.objects.filter(Q(name='soumya')|Q(name='rohit')) # writing multiple values
    
    d={'webpages':QLWO}
    return render(request,'retrieve_webpages.html',d)

def retrieve_access(request):
    QLAO=AccessRecord.objects.all()
    QLAO=AccessRecord.objects.filter(author='B')
    QLAO=AccessRecord.objects.exclude(author='B')
    QLAO=AccessRecord.objects.all()[::-1]
    QLAO=AccessRecord.objects.all().order_by('author')
    QLAO=AccessRecord.objects.all().order_by('-name')
    QLAO=AccessRecord.objects.filter(name=3).order_by('author')
    QLAO=AccessRecord.objects.filter(date__gte='2024-7-1')
    QLAO=AccessRecord.objects.filter(date__lte='2024-7-1')
    QLAO=AccessRecord.objects.filter(date__day='22')
    d={'access_record':QLAO}
    return render(request,'retrieve_access.html',d)



    







