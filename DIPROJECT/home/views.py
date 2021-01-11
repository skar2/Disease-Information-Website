from django.shortcuts import render,redirect
from datetime import datetime
from home.models import Contact,Info,News
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from home.forms import CreateUserform
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
   return render(request,'home.html')

def welcome(request):
    allnewss = News.objects.all()
    param = {'allnewss': allnewss}
    return render(request, 'welcome.html', param)

def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def submitcontact(request):
    if request.method=='POST':
        gname = request.POST.get('name')
        gemail = request.POST.get('email')
        gmsg = request.POST.get('msg')
        if gname!='' and gemail!='' and gmsg!='':
            contact = Contact(name=gname, email=gemail, msg=gmsg, date=datetime.today())
            contact.save()
            messages.success(request,"Thanks for contacting us...")
            return render(request,'submitcontact.html')
        messages.success(request,"Something went wrong.Check whether you have filled all "
                               "information in the form and try again")
        return render(request,'submitcontact.html')

def disease(request):
    allInfos = Info.objects.all()
    context = {'allInfos': allInfos}
    return render(request,'disease.html',context)

def search(request):
    query=request.GET['query']
    allInfos=Info.objects.filter(name__icontains=query)
    params={'allInfos': allInfos }
    return render(request,'search.html', params)
    #disease_names= ["heart", "disease","cancer","typhoid",]

def home1(request):
    return render(request,"home1.html")

def whatisdisease(request):
    return render(request,"whatisdisease.html")

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('welcome')
    else:
        form=CreateUserform()

        if request.method=='POST':
            form=CreateUserform(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get('username')
                messages.success(request,'Account was created for '+ user)
                return redirect('login')

    context={'form':form}
    return render(request,'register.html',context)

def loginPage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        if username=='Admin1' and password=='akshay1234':
            # print(Contact.objects.all())
            recentcontacts={"recentcontacts":reversed(Contact.objects.all())}
            return render(request,'admin.html',recentcontacts)

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('welcome')
        else:
            messages.info(request,"Username OR Password is incorrect")
    context={}
    return render(request,'login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def addnews(request):
    gtitle=request.POST.get('title',"")
    gcontent= request.POST.get('content',"")
    news=News(title=gtitle, content=gcontent, date=datetime.today())
    news.save()
    messages.info(request, "News added successfully...")
    return render(request,'admin.html')

def adddisease(request):
    gname=request.POST.get('name',"")
    goverview= request.POST.get('overview',"")
    gsymptoms = request.POST.get('symptoms',"")
    grisk= request.POST.get('risk',"")
    gprev= request.POST.get('prev',"")
    gcauses = request.POST.get('causes',"")
    gimg = request.POST.get('img')
    info=Info(name=gname,overview=goverview,symptoms=gsymptoms,risk=grisk,prev=gprev,causes=gcauses,
              img=gimg,date=datetime.today())
    info.save()
    messages.info(request, "Disease Information added successfully...")
    return render(request,'admin.html')
