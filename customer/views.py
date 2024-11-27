from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
from django.contrib import messages
from customer.forms import *
from customer.models import *
from manager.models import *
import random
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
import datetime
from django.core.mail import send_mail
from tea_shop import settings

# Create your views here.

def index(request):
    global form
    global form2
    # Signup code
    if request.method=='POST':
        if request.POST.get("signup")=="signup":
            form=CustomuserForm(request.POST)
            form2=CustomerForm(request.POST)
            if form.is_valid():  
                # otp mail send
                global otp
                cartorder_id,otp=GenerateOrderId()
                u_mail=request.POST['full_name']
                sub='Your OTP Verification Code'
                msg=f'Dear {u_mail}\nThank you for signing up with us. To verify your email, please enter the following\nOne Time Password (OTP): {otp}\n\nBest regards,Tea Cozy'
                from_mail=settings.EMAIL_HOST
                to_mail=[request.POST['email']]
                request.session['u_mail']=u_mail
                send_mail(subject=sub,message=msg,from_email=from_mail,recipient_list=to_mail)
                return redirect('otpverify')
            else:
                print(form.errors)
                print(form2.errors)
        else:
        # login code
            mail=request.POST.get('email')
            pas=request.POST.get('password')
            customer=authenticate(request, email=mail, password=pas)
            u_id=CustomerModel.objects.get(email=mail)
            cu_id=CustomUser.objects.get(email=mail)
            print('u_id:',u_id.id)
            print('cu_id:',cu_id)
            print(customer)
            if customer is not None: 
                if customer.is_customer and customer.is_active and not customer.is_superuser and not customer.is_staff and not customer.is_admin:
                    login(request,customer)
                    request.session['username']=customer.email
                    request.session['u_id']=u_id.id
                    request.session['cu_id']=cu_id.id
                    print('login successfully')
                    return redirect('customerIndex')
                else:
                    print('Error...!Please enter valid emial or password')
            else:
                    print('Error...!Please enter valid emial or password')

    username=request.session.get('username')
    cart=request.session.get('cart', {})
    cart_total=len(cart.keys())
    return render(request,'customer/index.html',{'username':username,'cart_total':cart_total})

def userlogout(request):
    logout(request)
    return redirect('customerIndex')


def about(request):
    global form
    global form2
    # Signup code
    if request.method=='POST':
        if request.POST.get("signup")=="signup":
            form=CustomuserForm(request.POST)
            form2=CustomerForm(request.POST)
            if form.is_valid():
                # otp mail send
                global otp
                cartorder_id,otp=GenerateOrderId()
                u_mail=request.POST['full_name']
                sub='Your OTP Verification Code'
                msg=f'Dear {u_mail}\nThank you for signing up with us. To verify your email, please enter the following\nOne Time Password (OTP): {otp}\n\nBest regards,Tea Cozy'
                from_mail=settings.EMAIL_HOST
                to_mail=[request.POST['email']]
                request.session['u_mail']=u_mail
                send_mail(subject=sub,message=msg,from_email=from_mail,recipient_list=to_mail)
                return redirect('otpverify')
                
            else:
                print(form.errors)
                print(form2.errors)
        else:
        # login code
            mail=request.POST.get('email')
            pas=request.POST.get('password')
            customer=authenticate(request, email=mail, password=pas)
            u_id=CustomerModel.objects.get(email=mail)
            cu_id=CustomUser.objects.get(email=mail)
            print(customer)
            if customer is not None: 
                if customer.is_customer and customer.is_active and not customer.is_superuser and not customer.is_staff and not customer.is_admin:
                    login(request,customer)
                    request.session['username']=customer.email
                    request.session['u_id']=u_id.id
                    request.session['cu_id']=cu_id.id
                    print('login successfully')
                    return redirect('customerIndex')
                else:
                    print('Error...!Please enter valid emial or password')
            else:
                    print('Error...!Please enter valid emial or password')

    ############################
    cart=request.session.get('cart', {})
    cart_total=len(cart.keys())
    username=request.session.get('username')
    return render(request, 'customer/about.html',{'cart_total':cart_total,'username':username})


def blog(request):
    # Signup code
    global form
    global form2
    if request.method=='POST':
        if request.POST.get("signup")=="signup":
            form=CustomuserForm(request.POST)
            form2=CustomerForm(request.POST)
            if form.is_valid():
                # otp mail send
                global otp
                cartorder_id,otp=GenerateOrderId()
                u_mail=request.POST['full_name']
                sub='Your OTP Verification Code'
                msg=f'Dear {u_mail}\nThank you for signing up with us. To verify your email, please enter the following\nOne Time Password (OTP): {otp}\n\nBest regards,Tea Cozy'
                from_mail=settings.EMAIL_HOST
                to_mail=[request.POST['email']]
                request.session['u_mail']=u_mail
                send_mail(subject=sub,message=msg,from_email=from_mail,recipient_list=to_mail)
                return redirect('otpverify')
            else:
                print(form.errors)
                print(form2.errors)
        else:
        # login code
            mail=request.POST.get('email')
            pas=request.POST.get('password')
            customer=authenticate(request, email=mail, password=pas)
            u_id=CustomerModel.objects.get(email=mail)
            cu_id=CustomUser.objects.get(email=mail)
            print(customer)
            if customer is not None: 
                if customer.is_customer and customer.is_active and not customer.is_superuser and not customer.is_staff and not customer.is_admin:
                    login(request,customer)
                    request.session['username']=customer.email
                    request.session['u_id']=u_id.id
                    request.session['cu_id']=cu_id.id
                    print('login successfully')
                    return redirect('customerIndex')
                else:
                    print('Error...!Please enter valid emial or password')
            else:
                    print('Error...!Please enter valid emial or password')

    ############################
    cart=request.session.get('cart', {})
    cart_total=len(cart.keys())
    username=request.session.get('username')
    return render(request, 'customer/blog.html',{'cart_total':cart_total,'username':username})

def contact(request):
    # Signup code
    global form
    global form2
    if request.method=='POST':
        if request.POST.get("signup")=="signup":
            form=CustomuserForm(request.POST)
            form2=CustomerForm(request.POST)
            if form.is_valid():
                # otp mail send
                global otp
                cartorder_id,otp=GenerateOrderId()
                u_mail=request.POST['full_name']
                sub='Your OTP Verification Code'
                msg=f'Dear {u_mail}\nThank you for signing up with us. To verify your email, please enter the following\nOne Time Password (OTP): {otp}\n\nBest regards,Tea Cozy'
                from_mail=settings.EMAIL_HOST
                to_mail=[request.POST['email']]
                request.session['u_mail']=u_mail
                send_mail(subject=sub,message=msg,from_email=from_mail,recipient_list=to_mail)
                return redirect('otpverify')
            else:
                print(form.errors)
                print(form2.errors)
        else:
        # login code
            mail=request.POST.get('email')
            pas=request.POST.get('password')
            customer=authenticate(request, email=mail, password=pas)
            u_id=CustomerModel.objects.get(email=mail)
            cu_id=CustomUser.objects.get(email=mail)
            print(customer)
            if customer is not None: 
                if customer.is_customer and customer.is_active and not customer.is_superuser and not customer.is_staff and not customer.is_admin:
                    login(request,customer)
                    request.session['username']=customer.email
                    request.session['u_id']=u_id.id
                    request.session['cu_id']=cu_id.id
                    print('login successfully')
                    return redirect('customerIndex')
                else:
                    print('Error...!Please enter valid emial or password')
            else:
                    print('Error...!Please enter valid emial or password')

    ############################
    cart=request.session.get('cart', {})
    cart_total=len(cart.keys())
    username=request.session.get('username')
    return render(request,'customer/contact.html',{'cart_total':cart_total,'username':username})

def menu(request):
    # Signup code
    global form
    global form2
    if request.method=='POST':
        if request.POST.get("signup")=="signup":
            form=CustomuserForm(request.POST)
            form2=CustomerForm(request.POST)
            if form.is_valid():
                # otp mail send
                global otp
                cartorder_id,otp=GenerateOrderId()
                u_mail=request.POST['full_name']
                sub='Your OTP Verification Code'
                msg=f'Dear {u_mail}\nThank you for signing up with us. To verify your email, please enter the following\nOne Time Password (OTP): {otp}\n\nBest regards,Tea Cozy'
                from_mail=settings.EMAIL_HOST
                to_mail=[request.POST['email']]
                request.session['u_mail']=u_mail
                send_mail(subject=sub,message=msg,from_email=from_mail,recipient_list=to_mail)
                return redirect('otpverify')
            else:
                print(form.errors)
                print(form2.errors)
        else:
        # login code
            mail=request.POST.get('email')
            pas=request.POST.get('password')
            customer=authenticate(request, email=mail, password=pas)
            u_id=CustomerModel.objects.get(email=mail)
            cu_id=CustomUser.objects.get(email=mail)
            print(customer)
            if customer is not None: 
                if customer.is_customer and customer.is_active and not customer.is_superuser and not customer.is_staff and not customer.is_admin:
                    login(request,customer)
                    request.session['username']=customer.email
                    request.session['u_id']=u_id.id
                    request.session['cu_id']=cu_id.id
                    print('login successfully')
                    return redirect('customerIndex')
                else:
                    print('Error...!Please enter valid emial or password')
            else:
                    print('Error...!Please enter valid emial or password')

    ############################
    cart=request.session.get('cart', {})
    cart_total=len(cart.keys())
    product_data=ProductModel.objects.all()
    username=request.session.get('username')
    return render(request, 'customer/menu.html',{'product':product_data,'cart_total':cart_total,'username':username})

@login_required(login_url='/')
def cart(request):
    global form
    global form2
    # Signup code
    if request.method=='POST':
        if request.POST.get("signup")=="signup":
            form=CustomuserForm(request.POST)
            form2=CustomerForm(request.POST)
            if form.is_valid():
                # otp mail send
                global otp
                cartorder_id,otp=GenerateOrderId()
                u_mail=request.POST['full_name']
                sub='Your OTP Verification Code'
                msg=f'Dear {u_mail}\nThank you for signing up with us. To verify your email, please enter the following\nOne Time Password (OTP): {otp}\n\nBest regards,Tea Cozy'
                from_mail=settings.EMAIL_HOST
                to_mail=[request.POST['email']]
                request.session['u_mail']=u_mail
                send_mail(subject=sub,message=msg,from_email=from_mail,recipient_list=to_mail)
                return redirect('otpverify')
            else:
                print(form.errors)
                print(form2.errors)
        else:
        # login code
            mail=request.POST.get('email')
            pas=request.POST.get('password')
            customer=authenticate(request, email=mail, password=pas)
            u_id=CustomerModel.objects.get(email=mail)
            cu_id=CustomUser.objects.get(email=mail)
            print(customer)
            if customer is not None: 
                if customer.is_customer and customer.is_active and not customer.is_superuser and not customer.is_staff and not customer.is_admin:
                    login(request,customer)
                    request.session['username']=customer.email
                    request.session['u_id']=u_id.id
                    request.session['cu_id']=cu_id.id
                    print('login successfully')
                    return redirect('customerIndex')
                else:
                    print('Error...!Please enter valid emial or password')
            else:
                    print('Error...!Please enter valid emial or password')

    ############################
    cart = request.session.get('cart', {})  
    cart_total=len(cart.keys())
    total_price = sum(float(item['price']) * item['quantity'] for item in cart.values())
    username=request.session.get('username')
    return render(request, 'customer/cart.html',{'cart':cart,'total_price':total_price,'cart_total':cart_total,'username':username})

def add_to_cart(request,product_id):
    product = ProductModel.objects.get(id=product_id)
    cart = request.session.get('cart', {})

    if str(product.id) not in cart:
        cart[str(product.id)] = {
            'name': product.product_name,
            'price': str(product.price),
            'description':product.description,
            'img':product.product_img.url,
            'quantity': 1,
            'total': str(product.price)
        }
    else:
        cart[str(product.id)]['quantity'] += 1
        cart[str(product.id)]['total'] = int(cart[str(product.id)]['quantity']) * int(cart[str(product.id)]['price'])

    request.session['cart'] = cart
    messages.success(request, f'{product.product_name} added to cart.')
    return redirect('customermenu')

def update_cart(request):
    if request.method == 'POST':
        print("Received request:", request.POST)
        product_id = request.POST.get('product_id')
        action = request.POST.get('action')
        cart = request.session.get('cart', {})

        print("Current cart:", cart)  # Debugging line
        print("Product ID received:", product_id)  # Debugging line

        # Check if the product exists in the cart
        if product_id in cart:
            if action == 'increase':
                cart[product_id]['quantity'] += 1
                cart[product_id]['total'] =  int(cart[product_id]['price']) * int(cart[product_id]['quantity'])
                print(cart[product_id]['total'])
            elif action == 'decrease':
                if cart[product_id]['quantity'] > 1:
                    cart[product_id]['quantity'] -= 1
                    cart[product_id]['total'] =  int(cart[product_id]['price']) * int(cart[product_id]['quantity'])
                    print(cart[product_id]['total'])
                else:
                    del cart[product_id]  # Remove item if quantity is 0

            request.session['cart'] = cart
            total_price = sum(float(item['price']) * item['quantity'] for item in cart.values())
           
            # cart_total=len(cart.keys())
            return JsonResponse({'cart': cart,'total_price':total_price})
        else:
            return JsonResponse({'error': 'Product not found in cart.'}, status=404)

    return JsonResponse({'error': 'Invalid request method.'}, status=400)


def GenerateOrderId():
    global otp
    cartorder_id=random.randint(11111,99999)
    otp=random.randint(111111,999999)
    return cartorder_id,otp

@login_required(login_url='/')
def updateProfile(request):
    # Signup code
    global form
    global form2
    if request.method=='POST':
        if request.POST.get("signup")=="signup":
            form=CustomuserForm(request.POST)
            form2=CustomerForm(request.POST)
            if form.is_valid():
                # otp mail send
                global otp
                cartorder_id,otp=GenerateOrderId()
                u_mail=request.POST['full_name']
                sub='Your OTP Verification Code'
                msg=f'Dear {u_mail}\nThank you for signing up with us. To verify your email, please enter the following\nOne Time Password (OTP): {otp}\n\nBest regards,Tea Cozy'
                from_mail=settings.EMAIL_HOST
                to_mail=[request.POST['email']]
                request.session['u_mail']=u_mail
                send_mail(subject=sub,message=msg,from_email=from_mail,recipient_list=to_mail)
                return redirect('otpverify')
            else:
                print(form.errors)
                print(form2.errors)
        else:
        # login code
            mail=request.POST.get('email')
            pas=request.POST.get('password')
            customer=authenticate(request, email=mail, password=pas)
            u_id=CustomerModel.objects.get(email=mail)
            cu_id=CustomUser.objects.get(email=mail)
            print(customer)
            if customer is not None: 
                if customer.is_customer and customer.is_active and not customer.is_superuser and not customer.is_staff and not customer.is_admin:
                    login(request,customer)
                    request.session['username']=customer.email
                    request.session['u_id']=u_id.id
                    request.session['cu_id']=cu_id.id
                    print('login successfully')
                    return redirect('customerIndex')
                else:
                    print('Error...!Please enter valid emial or password')
            else:
                    print('Error...!Please enter valid emial or password')

    ############################
    username=request.session.get('username')
    c_id=CustomerModel.objects.get(email=username)
    cm_id=CustomUser.objects.get(email=username)
    print('customer model id: ',c_id)
    print('custom user model id: ',cm_id)
    if request.method == 'POST':        
        updateForm=CustomerUpdateForm(request.POST,instance=c_id)
        updateForm1=CustomUserUpdateForm(request.POST,instance=cm_id)
        if updateForm.is_valid() and updateForm1.is_valid():
            updateForm.save()
            updateForm1.save()
            print('Record Updated Successfully..')
            return redirect('/')
        else:
            print(updateForm.errors)
            
            
        
    username=request.session.get('username')
    return render(request,'customer/updateprofile.html',{'user':c_id,'username':username})

@login_required(login_url='/')
def revieworder(request):
    # Signup code
    global form
    global form2
    if request.method=='POST':
        if request.POST.get("signup")=="signup":
            form=CustomuserForm(request.POST)
            form2=CustomerForm(request.POST)
            if form.is_valid():
                # otp mail send
                global otp
                cartorder_id,otp=GenerateOrderId()
                u_mail=request.POST['full_name']
                sub='Your OTP Verification Code'
                msg=f'Dear {u_mail}\nThank you for signing up with us. To verify your email, please enter the following\nOne Time Password (OTP): {otp}\n\nBest regards,Tea Cozy'
                from_mail=settings.EMAIL_HOST
                to_mail=[request.POST['email']]
                request.session['u_mail']=u_mail
                send_mail(subject=sub,message=msg,from_email=from_mail,recipient_list=to_mail)
                return redirect('otpverify')
            else:
                print(form.errors)
                print(form2.errors)
        else:
        # login code
            mail=request.POST.get('email')
            pas=request.POST.get('password')
            customer=authenticate(request, email=mail, password=pas)
            u_id=CustomerModel.objects.get(email=mail)
            cu_id=CustomUser.objects.get(email=mail)
            print(customer)
            if customer is not None: 
                if customer.is_customer and customer.is_active and not customer.is_superuser and not customer.is_staff and not customer.is_admin:
                    login(request,customer)
                    request.session['username']=customer.email
                    request.session['u_id']=u_id.id
                    request.session['cu_id']=cu_id.id
                    print('login successfully')
                    return redirect('customerIndex')
                else:
                    print('Error...!Please enter valid emial or password')
            else:
                    print('Error...!Please enter valid emial or password')

    ############################
    username=request.session.get('username')   
    if username is None:
        return redirect('/') 
    else:
        cart = request.session.get('cart', {})
        cartorder_id,otp=GenerateOrderId()
        print(cartorder_id)
        final_total=0
        p_name=''
        for key,value in cart.items():
            final_total+=(int(value['total']))
        
        if request.method == 'POST':
            cartForm=OrderForm(request.POST)       
            if cartForm.is_valid():
                customer_name = cartForm.cleaned_data['customer_name']
                email = cartForm.cleaned_data['email']
                mobile = cartForm.cleaned_data['mobile']
                city = cartForm.cleaned_data['city']
                street = cartForm.cleaned_data['street']
                society = cartForm.cleaned_data['society']
                apartment_number = cartForm.cleaned_data['apartment_number']
                card_payment = cartForm.cleaned_data['card_payment']
                upi_payment = cartForm.cleaned_data['upi_payment']
                cash_payment = cartForm.cleaned_data['cash_payment']
                company_name=cartForm.cleaned_data['company_name']
                company_id=cartForm.cleaned_data['company_id']
                order_id=cartForm.cleaned_data['order_id']
                # Debug: Print cart contents
                print("Cart contents:", cart)


                for key, value in cart.items():
                    product_instance = get_object_or_404(ProductModel, id=key)
                    cart_order_instance = cart_order(
                        order_id=order_id,
                        customer_name=customer_name,
                        email=email,
                        mobile=mobile,
                        product_id=product_instance,  # Ensure this is correct
                        product_quantity=value['quantity'],  # Ensure this is correct
                        total=value['total'],  # Ensure this is correct
                        city=city,
                        street=street,
                        society=society,
                        apartment_number=apartment_number,
                        card_payment=card_payment,
                        upi_payment=upi_payment,
                        cash_payment=cash_payment,
                        company_name=company_name,
                        company_id=company_id
                    )
                    cart_order_instance.save()
                    print('Order Placed...')
                del request.session['cart']
                return redirect('customermenu')
            else:
                print(cartForm.errors)
        u_mail=request.session.get('username')
        u_id=CustomerModel.objects.get(email=u_mail)

    return render(request,'customer/revieworder.html',{'cart':cart,'final_total':final_total,'cartorder_id':cartorder_id,'u_id':u_id.id,'username':username})

@login_required(login_url='/')
def ordertracking(request,order_id):
    # Signup code
    global form
    global form2
    if request.method=='POST':
        if request.POST.get("signup")=="signup":
            form=CustomuserForm(request.POST)
            form2=CustomerForm(request.POST)
            if form.is_valid():
                # otp mail send
                global otp
                cartorder_id,otp=GenerateOrderId()
                u_mail=request.POST['full_name']
                sub='Your OTP Verification Code'
                msg=f'Dear {u_mail}\nThank you for signing up with us. To verify your email, please enter the following\nOne Time Password (OTP): {otp}\n\nBest regards,Tea Cozy'
                from_mail=settings.EMAIL_HOST
                to_mail=[request.POST['email']]
                request.session['u_mail']=u_mail
                send_mail(subject=sub,message=msg,from_email=from_mail,recipient_list=to_mail)
                return redirect('otpverify')
            else:
                print(form.errors)
                print(form2.errors)
        else:
        # login code
            mail=request.POST.get('email')
            pas=request.POST.get('password')
            customer=authenticate(request, email=mail, password=pas)
            u_id=CustomerModel.objects.get(email=mail)
            cu_id=CustomUser.objects.get(email=mail)
            print(customer)
            if customer is not None: 
                if customer.is_customer and customer.is_active and not customer.is_superuser and not customer.is_staff and not customer.is_admin:
                    login(request,customer)
                    request.session['username']=customer.email
                    request.session['u_id']=u_id.id
                    request.session['cu_id']=cu_id.id
                    print('login successfully')
                    return redirect('customerIndex')
                else:
                    print('Error...!Please enter valid emial or password')
            else:
                    print('Error...!Please enter valid emial or password')

    ############################
    u_mail=request.session.get('username')
    order_id=cart_order.objects.values('order_id','order_status').distinct().filter(order_id=order_id)
    for i in order_id:
        o_id=i['order_id']
    order_date=cart_order.objects.values('order_date').distinct().filter(order_id=o_id)
    print(order_date)
    order_track=cart_order.objects.all().filter(email=u_mail)
    
    return render(request,'customer/ordertracking.html',{'order_track':order_track,'username':u_mail,'order_id':order_id,'order_date':order_date})

@login_required(login_url='/')
def vieworder(request):
    u_mail=request.session.get('username')
    order_data=cart_order.objects.values('order_date','order_id','delivery_status','email','order_status').annotate(total_quantity=Sum('product_quantity')).filter(email=u_mail)  
    date=datetime.datetime.now()
    return render(request,'customer/vieworder.html',{'order_data':order_data,'username':u_mail})

def otpverify(request):
    global otp
    print('otp: ',otp)
    if request.method=='POST':
        if request.POST['otp'] == str(otp):
            print("Verification Successfull!")
            form.save()
            form2.save()
            print('Signup Successfully...')
            return redirect('/')
        else:
            print('Please Enter Valid Otp.')
    u_mail=request.session.get('u_mail')
    return render(request,'customer/otpverify.html',{'user':u_mail})