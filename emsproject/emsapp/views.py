from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import *
from .filters import*
from django.db.models import Sum,Q
import datetime
from datetime import date
# Create your views here.
def create_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        try:
            user=User.objects.get(username=username)
            
            if user:
                msg = "This username already taken"
                context = {'msg':msg}
                return render (request,'signup.html',context)
            
        except:
            
            if password == cpassword:
                    user = User.objects.create_user(username = username,password = password)
                    if user:
                        return redirect ('/add-employee')
            
            else:
                msg = "Password doesn't matched"
                context = {'msg':msg}
                return render (request,'signup.html',context)
        
    return render (request,'signup.html')
def add_employee(request):
    form = EmployeeForm()
    if request.method =='POST':
        form = EmployeeForm(request.POST,request.FILES)
        if form.is_valid():
            form = form.save()
            context = {'form':form} 
            return redirect ('/add-employee')
    form = EmployeeForm()
    
    context ={'form':form}
    return render(request,'add-employee.html',context)



def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            # login_status = login_time>
            return redirect('/home')
        else:
            msg = "Username of Password is Incorrect"
            context = {'msg':msg}
            return render(request,'login.html',context)
    return render(request,'login.html')

@login_required(login_url='/')
def user_logout(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/')
def home(request):
    
    total=Employee.objects.all().count()
    l_app=Leave.objects.filter(check_status=False)
    l_app=l_app.count()
    leave= Leave.objects.filter(approve_status=True)
    leave=leave.count()
    user = request.user
    meeting = Meeting.objects.filter(user=request.user,meeting_date=datetime.datetime.now())
    meet=meeting.count()
    leave=Leave.objects.filter(user=request.user).count()
    context={'total':total,'l_app':l_app,'leave':leave,'meeting':meeting,'meet':meet}
    return render (request,'home.html',context)

@login_required(login_url='/')
def all_employee(request):
    all_employee = Employee.objects.all()
    myfilter = EmployeeFilter(request.GET,queryset=all_employee)
    all_employee = myfilter.qs
    context = {'all_employee':all_employee,'myfilter':myfilter}
    return render (request,'all-employee.html',context)

@login_required(login_url='/')
def leave_form(request):
    if request.method=='POST':
        form=LeaveForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user=request.user
            form =form.save()
            msg = "Application Submitted Wait For Permission"
            form =LeaveForm()
            context = {'form':form,'msg':msg}
            
            return render (request,'leave_form.html',context)
            
    form =LeaveForm()

    context = {'form':form}
    return render (request,'leave_form.html',context)

@login_required(login_url='/')
def new_application(request):
    application = Leave.objects.filter(check_status=False)
    context = {'application':application}
    return render (request,'new_application.html',context)

@login_required(login_url='/')
def process_application(request,id,sts):
    leave = Leave.objects.get(id=id)
    leave.check_status =True
    if sts ==1:
        leave.approve_status =True
        leave = leave.save()
        return redirect ('/new-application')
    else:
        leave.approve_status = False
        leave = leave.save()
        return redirect ('/new-application')
    return redirect ('/new-application')

@login_required(login_url='/')
def my_application(request):
    application = Leave.objects.filter(user=request.user)
    context = {'application':application}
    return render(request,'my_application.html',context)

@login_required(login_url='/')
def holiday(request):
    holiday = Holiday.objects.all()
    context={'holiday':holiday}
    return render (request,'holiday.html',context)

def details(request,id):
    detail = Employee.objects.filter(id=id)
    context={'detail':detail}
    return render(request,'details.html',context)

def daily_task(request):
    
    user=request.user
    do_task=DailyTask.objects.filter(user=user,do_status=True)
    working_task=DailyTask.objects.filter(user=user,working_status=True)
    done_task=DailyTask.objects.filter(user=user,done_status=True)
    context={'do_task':do_task,'working_task':working_task,'done_task':done_task }
    return render(request,'daily-task.html',context)

def move_task(request,id,sts):
    
    task=DailyTask.objects.get(id=id)
    
    if sts=='move working':
        task.working_status=True
        task.do_status=False
        task = task.save()
        return redirect('/daily-task')

    if sts=='move done':
        task.done_status=True
        task.working_status=False
        task.do_status=False
        task = task.save()
        return redirect('/daily-task')

    if sts=='done':
        task.done_status=False
        task.working_status=False
        task.do_status=False
        task = task.save()
        return redirect('/daily-task')
    return redirect('/daily-task')

def add_task(request):
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user=request.user
            form.do_status=True
            form =form.save()
            msg = " Submitted "
            form =TaskForm()
            context = {'form':form,'msg':msg}
            
            return render (request,'add_task.html',context)
            
    form =TaskForm()

    context = {'form':form}
    return render (request,'add_task.html',context)

def profile(request):
    user=request.user
    profile=Employee.objects.get(username=user)
    department=profile.department
    dept =Employee.objects.filter(department=department)
    context={'profile':profile,'dept':dept}
    return render(request,'profile.html',context)

def edit_profile(request):
    employee=Employee.objects.get(username=request.user)
    form = EditEmployeeForm(instance=employee)
    if request.method =='POST':
        form = EditEmployeeForm(request.POST,request.FILES,instance=employee)
        if form.is_valid():
            form.save()  
            return redirect('/profile')
    context = {'form':form}
    return render (request,'profile-edit.html',context)
def edit_employee(request,id):
    employee = Employee.objects.get(id=id)
    form = EditEmployeeForm(instance=employee)
    if request.method =='POST':
        form = EditEmployeeForm(request.POST,request.FILES, instance=employee)
        if form.is_valid():
            form.save()  
            return redirect('/all-employee')
    context = {'form':form}
    return render(request, 'edit.html', context)

def abc (request):
    return render (request,'base2.html')

def delete (requst,id):
    expence = Employee.objects.get(id=id)
    expence = expence.delete()
    return redirect('/all-employee')

def profile_detail(request):
    details = Employee.objects.filter(username=request.user)
    context={'details':details}
    return render(request,'profile-details.html',context)

def create_meeting(request):
    if request.method=='POST':
        form=MeetingForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user=request.user
            form =form.save()
            msg = "Create Meeting Successfully"
            form =MeetingForm()
            context = {'form':form,'msg':msg}
            
            return render (request,'create-meeting.html',context)
            
    form =MeetingForm()

    context = {'form':form}
    return render (request,'create-meeting.html',context)

def meeting(request):
    user = request.user
    meeting = Meeting.objects.filter(meeting_date=datetime.datetime.now())
    context={'meeting':meeting}
    return render (request,'meeting.html',context)



# def attendence(request):
#     username = request.user
#     attend = Attendence.objects.filter(username=request.user)
#     context = {'attend': attend}
#     return render (request,'attendence.html',context)

def create_client(request):
    form = ClientForm()
    if request.method =='POST':
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save()
            context = {'form':form} 
            return redirect ('/client')
    form = ClientForm()
    
    context ={'form':form}
    return render(request,'create_client.html',context)
def client(request):
    all_client = Client.objects.all()
    clientfilter = ClientFilter(request.GET, queryset=all_client)
    all_client = clientfilter.qs
    context = {'all_client': all_client, 'clientfilter': clientfilter}
    return render (request,'client.html',context)


def client_delete(requst, id):
    client = Client.objects.get(id=id)
    client = client.delete()
    return redirect('/client')

def client_details(request,id):
    c_detail = Client.objects.filter(id=id)
    context={'c_detail':c_detail}
    return render(request,'client_details.html',context)