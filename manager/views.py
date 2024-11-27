from django.shortcuts import render,redirect
from manager.forms import *
from manager.models import *
from customer.forms import *
from customer.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import datetime
from django.db.models import Sum
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form=CustomuserForm(request.POST)
        if form.is_valid():
            form.save()
            print('Staff record inserted...')
        else:
            print(form.errors)
    return render(request,'shop/shopregister.html')

def shoplogin(request):
    if request.method == 'POST':
        mail=request.POST.get('email')
        pas=request.POST.get('password')
        shopuser=authenticate(request,email=mail,password=pas)
        if shopuser is not None: 
            if shopuser.is_staff and shopuser.is_active and not shopuser.is_superuser and not shopuser.is_customer and not shopuser.is_admin:
                login(request,shopuser)
                request.session['user']=mail
                print('Login Successfully...')
                return redirect('index')
            else:
                print('Error!Please Enter Valid id or password...')
        else:
                print('Error!Please Enter Valid id or password...')

    return render(request,'shop/shoplogin.html')

@login_required(login_url='/manager')
def index(request):
    user=request.session.get('user')
    cart_data=cart_order.objects.aggregate(total=Sum('total'),total_order=Sum('product_quantity'))
    print(cart_data)
    order_data=cart_order.objects.all()
    return render(request,'shop/index.html',{'user':user,'cart_data':cart_data,'order_data':order_data})

@login_required(login_url='/manager')
def menu(request):
    user=request.session.get('user')
    data=ProductModel.objects.all()
    return render(request,'shop/menu.html',{'data':data,'user':user})

@login_required(login_url='/manager')
def order(request):
    user=request.session.get('user')
    order=cart_order.objects.all()
    return render(request,'shop/order.html',{'user':user,'order':order})

def confirmOrder(request,id):
    order_id=cart_order.objects.get(id=id)
    order_id.order_status=True
    order_id.save()
    return redirect('order')

@login_required(login_url='/manager')
def addproduct(request):
    user=request.session.get('user')
    category=ProductCategoryModel.objects.all()
    if request.method=='POST':
        form=ProductModelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print('Product added..')
        else:
            print(form.errors)

    return render(request,'shop/addproduct.html',{'category':category,'user':user})

def deleteproduct(request,id):
    product_id=ProductModel.objects.get(id=id)
    try:
        ProductModel.delete(product_id)
        print('Product Deleted....')
    except Exception as e:
        print(e)
    return redirect('menu')

@login_required(login_url='/manager')
def updatedata(request,id):
    product_id=ProductModel.objects.get(id=id)
    category=ProductCategoryModel.objects.all()

    if request.method=='POST':
        form=UpdateProductForm(request.POST,request.FILES,instance=product_id)
        if form.is_valid():
            form.save()
            print('Product added..')
            return redirect('menu')
        else:   
            print(form.errors)
    return render(request,'shop/updatedata.html',{'data':product_id,'category':category})

@login_required(login_url='/manager')
def staffattendance(request):
    staff_name=staff.objects.all()
    if request.method == 'POST':
        form=staffAttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            print('record inserted...')
        else:
            print(form.errors)

    attendance_data=StaffAttendance.objects.all()
    for i in attendance_data:
        print(i.date.day)
    today=datetime.datetime.now()
    print(today.day)
    return render(request,'shop/staffattendance.html',{'staff_name':staff_name,'attendance_data':attendance_data,'today':today})

@login_required(login_url='/manager')
def viewattendance(request):
    data=StaffAttendance.objects.all()
    return render(request,'shop/viewattendance.html',{'data':data})

@login_required(login_url='/manager')
def addstaff(request):
    if request.method=='POST':
        form=staffModelForm(request.POST)
        if form.is_valid():
            form.save()
            print('Record Inserted...')
            return redirect('addstaff')
        else:
            print(form.errors)

    return render(request,'shop/addstaff.html')

@login_required(login_url='/manager')
def deliveryStatus(request,id):
    order_id=cart_order.objects.get(id=id)
    order_id.delivery_status=True
    order_id.save()
    return redirect('order')

def shoplogout(request):
    logout(request)
    return redirect('/manager')