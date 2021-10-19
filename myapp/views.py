from django.shortcuts import render
from faunadb import query as q
from faunadb.objects import Ref
from faunadb.client import FaunaClient
from django.http import HttpResponse
from django.shortcuts import redirect

client = FaunaClient(secret="Fill ur own secret key")

# Create your views here.
def home(request):
    student_data=[]
    dat=client.query(q.paginate(q.match(q.index("id"))))
    for i in dat['data']:
        data=client.query(q.get(i))
        all_data={"id":data['ref'].id(),"info":data['data']}
        student_data.append(all_data)
    
    return render(request,"home.html",{"data":student_data})

  
def AddStudent(request):
    if request.method=="POST":
        fname,lname,standard,section,rollno=request.POST['first'],request.POST['last'],request.POST['standard'],request.POST['section'],request.POST['roll']
        created=client.query(q.create(q.collection("PersonalData"),{"data":{"fname":f"{fname}","lname":f"{lname}","class":f"{standard}","section":f"{section}","rollno":f"{rollno}"}}))
        return redirect("home")

def UpdateStudent(request,id):
    if request.method=="POST":
        fname,lname,standard,section,rollno=request.POST['first'],request.POST['last'],request.POST['standard'],request.POST['section'],request.POST['roll']
        data=client.query(q.update(q.ref(q.collection("PersonalData"),f'{id}'),{"data":{"fname":f"{fname}","lname":f"{lname}","class":f"{standard}","section":f"{section}","rollno":f"{rollno}"}}))
        return render(request,'update.html',{'url':f'{id}',"data":data['data']})
    
    student_data=client.query(q.get(q.ref(q.collection("PersonalData"),f"{id}")))
    return render(request,'update.html',{'url':f'{id}',"data":student_data['data']})

def DeleteStudent(request,id):
    data=client.query(q.delete(q.ref(q.collection("PersonalData"),f'{id}')))    
    return redirect('http://127.0.0.1:8000/')


    
