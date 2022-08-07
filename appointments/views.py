from typing import Type
from django.http.response import HttpResponseRedirect, HttpResponseRedirectBase
from django.shortcuts import redirect, render
from django.contrib import messages
from appointments.models import Doctable
import json
from django.http import HttpResponse
from appointments.forms import addAppointments,addLogin,addUser,addQuery
from datetime import datetime
from appointments.models import Patienttable,Logintable,Appointmenttable,Querytable

# Create your views here.


def showadminhome(request):
    return render(request,'adminhome.html')


def showapphome(request):
    return render(request,'apphome.html')
def showgame(request):
    return render(request,'game.html')


def showappointments(request):
    return render(request,'appointments.html')

def showblog(request):
    return render(request,'blog.html')

def showcontact(request):
    return render(request,'contact.html')

def showdoctorhome(request):
    return render(request,'doctorhome.html')

def showlogin(request):
    return render(request,'login.html')


def showsearch(request):
    return render(request,'search.html')



def cusShow(request):
    messages=Doctable.objects.order_by("id")
    print(messages)
    return render(request, "show.html", {"message_list": messages})


# Dynamically populate the search dropdowns with deparments and doctors list
def fillSearchpage(request,depname,docname):
    try:
        res=''
        que=''
        message=[]
        if (depname=='All' and docname=='All'):
            message=Doctable.objects.all()
        else:
            if(depname=='All'):
                message=Doctable.objects.raw('select * from appointments_doctable where name="'+docname+'"')
            else:
                if(docname=='All'):
                    message=Doctable.objects.raw('select * from appointments_doctable where department="'+depname+'"')
                else:
                    message=Doctable.objects.raw('select * from appointments_doctable where name="'+docname+'" AND department="'+depname+'"')
        out=[]
        for i in message:
            out.append({ 'id':i.id,'department': i.department, 'name': i.name,'descr':i.descr,'img':i.img})
            res=json.dumps(out)
    except:
         res=json.dumps([{ 'error' : 'no customer found'}])
    return HttpResponse(res, content_type='application/json')


def fillDocdiv(request,docid):
    try:
        res=''
        que=''
        message=[]
        message=Doctable.objects.raw('select * from appointments_doctable where id="'+docid+'"')
        out=[]
        for i in message:
            out.append({ 'id':i.id,'department': i.department, 'name': i.name,'descr':i.descr,'img':i.img})
            res=json.dumps(out)
    except:
         res=json.dumps([{ 'error' : 'no record found'}])
    return HttpResponse(res, content_type='application/json')


def getLogin(request,uname):
    print('in login')
    try:
        res=''
        que=''
        message=[]
        message=Doctable.objects.raw('select * from appointments_Logintable where uname="'+uname+'"')
        out=[]
        if len(message)>0 :
            for i in message:
                out.append({ 'id':i.givenid,'department': i.department, 'name': i.name,'uname':i.uname,'password':i.psswd})
                res=json.dumps(out)
        else:
          res=json.dumps([{ 'error' : 'wrong username or password'}])  
    except:
         res=json.dumps([{ 'error' : 'no record found'}])
    print(res)
    return HttpResponse(res, content_type='application/json')


def addPatient(request):
    form = addUser(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.save()
            messages.success(request, 'New patient added. Now we can create a login for them.')
            return redirect("newpatient")
        else:
            return render(request, "newpatient.html", {"form": form})
    else:
        return render(request, "newpatient.html", {"form": form})


def addAppt(request):
    form = addAppointments(request.POST or None)
    print(request.POST)
    if request.method == "POST":
        if form.is_valid():
            print('here')
            message = form.save(commit=False)
            message.save()
            messages.success(request, 'Appointment Booked..')
            return redirect("appointments")
        else:
            return render(request, "appointments.html")
    else:
        return render(request, "appointments.html")


def addQue(request):
    form = addQuery(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.save()
            messages.success(request, 'Query submited successfully. Our representative will call you within 24hours.')
            return redirect("contact")
        else:
            return render(request, "contact.html")
    else:
        return render(request, "contact.html", {"form": form})


def addLogins(request):
    form = addLogin(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.save()
            messages.success(request, 'New Login created successfully..')
            return redirect("adminhome")
        else:
            return render(request, "adminhome.html")
    else:
        return render(request, "adminhome.html", {"form": form})


def showdocAppt(request,q):
    try:
        res=''
        que=''
        message=[]
        # message=Appointmenttable.objects.filter(id__contains=q)
        message=Doctable.objects.raw('select * from appointments_appointmenttable where doctid = '+q)
        print(len(message))
        out=[]
        if len(message)>0 :
            for i in message:
                print(i)
                t=i.date.strftime('%d/%m/%y')
                out.append({ 'patientname':i.patientname,'doctid': i.doctid,'date':t,'time':i.time})
                print(out)
                res=json.dumps(out)
        else:
           res=json.dumps([{ 'error' : 'no appointments'}]) 
    except:
         res=json.dumps([{ 'error' : 'no record found'}])
    return HttpResponse(res, content_type='application/json')


def getdocapp(request,id,dat):
    try:
        res=''
        que='select * from appointments_appointmenttable where doctid = '+id+' AND date ="'+dat+'"'
        message=[]
        print('in getdocapp')
        print(que)
        # message=Appointmenttable.objects.filter(id__contains=q)
        message=Doctable.objects.raw(que)
        print(len(message))
        out=[]
        if len(message)>0 :
            for i in message: 
                t=i.date.strftime('%d/%m/%y')
                out.append({ 'patientname':i.patientname,'doctid': i.doctid,'date':t,'time':i.time})
                res=json.dumps(out)
        else:
           res=json.dumps([{ 'error' : 'no appointments'}]) 
    except:
         res=json.dumps([{ 'error' : 'no record found'}])
    return HttpResponse(res, content_type='application/json')



