from django.shortcuts import render,redirect
<<<<<<< HEAD
from . models import Contact,User,Product,Wishlist,Cart,Reviews
import random
import requests
import stripe
from django.conf import settings
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils import timezone
from django.http import JsonResponse
=======
from . models import Contact,User,Product,Wishlist,Cart
import random
import requests
>>>>>>> 0cb652cfbb66f39b836544c05dd964d24044c638
# Create your views here.

stripe.api_key=settings.STRIPE_PRIVATE_KEY
YOUR_DOMAIN='http://localhost:8000' 

@csrf_exempt
def create_checkout_session(request):
    amount=int(json.load(request)['post_data'])
    final_amount=amount*100

    session=stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data':{
                'currency':'inr',
                'product_data':{
                    'name':'Checkout Session Data',
                },
                'unit_amount':final_amount,
            },
            'quantity':1,

        }],
        mode='payment',
        success_url=YOUR_DOMAIN + '/success.html',
        cancel_url=YOUR_DOMAIN + '/cancel.html',)
    return JsonResponse({'id':session.id})

def success(request):
    # user=User.objects.get(email=request.session['email'])
    carts=Cart.objects.filter(payment_status=False)
    for i in carts:
        i.payment_status=True
        i.save()

    carts=Cart.objects.filter(payment_status=False)
    request.session['cart_count']=len(carts)
    return render(request,'success.html')

def cancel(request):
    return render(request,'cancel.html')
def index(request):
    products=Product.objects.all()
    return render(request,'index.html',{'products':products})

def contact(request):
    if request.method=="POST":
        Contact.objects.create(
            fname=request.POST['fname'],
            lname=request.POST['lname'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            message=request.POST['message'],
            )
        msg="Contact Saved Successfully"
        return render(request,'contact.html',{'msg':msg})
    else:
        return render(request,'contact.html')
    
def login(request):
    if request.method=="POST":
      try:  
        user=User.objects.get(
                    email=request.POST['email'],
                    password=request.POST['password']
                )
        if user.usertype=='user':
                    request.session['email']=user.email
                    request.session['fname']=user.fname
                    request.session['profile_pic']=user.profile_pic.url
                    return render(request,'index.html')
        elif user.usertype=='seller':
                    request.session['email']=user.email
                    request.session['fname']=user.fname
                    request.session['profile_pic']=user.profile_pic.url
                    return render(request,'seller_index.html')
      except:
        msg="Email Or Password Is Incorrect!"
        return render(request,'login.html',{'msg':msg})
    else:
        return render(request,'login.html')
    
def logout(request):
    try:
        del request.session['email']
        del request.session['fname']
        return render(request,'login.html')
    
    except:
        return render(request,'login.html')
    
def registration(request):
    if request.method=='POST':
        try:
            User.objects.get(email=request.POST['email'])
            msg="Email Is Already Registered"
            return render(request,'registration.html',{'msg':msg})

        except:
            if request.POST['password']==request.POST['cpassword']:   
            
                User.objects.create(
                    fname=request.POST['fname'],
                    lname=request.POST['lname'],
                    email=request.POST['email'],
                    phone=request.POST['phone'],
                    address=request.POST['address'],
                    password=request.POST['password'],
                    cpassword=request.POST['cpassword'],
                    usertype=request.POST['usertype'],
                    profile_pic=request.POST['profile_pic'],
                )
                msg="User Sign Up Successfully"
                return render(request,'login.html',{"msg":msg})
            
            else:
                msg="Password And Confirm Password Does Not Match!Please Try Again"
                return render(request,'registration.html',{'msg':msg})
    else:
        return render(request,'registration.html')

def change_password(request):
    if request.method=="POST":
        oldpassword=request.POST['oldpassword']
        newpassword=request.POST['newpassword']
        cnewpassword=request.POST['cnewpassword']
        user=User.objects.get(email=request.session['email'])
        if user.password==oldpassword:
            if newpassword==cnewpassword:
                user.password=cnewpassword
                user.save()
                try:
                    del request.session['email']
                    del request.session['fname']
                    msg="Password Changed Successfully.Please Login Again"
                    return render(request,'login.html',{'msg':msg})
                except:
                    return render(request,'login.html')
            else:
                msg="New Password And Confirm New Password Does Not Match!"
                return render(request,'change_password.html',{'msg':msg})
        else:
            msg="Old Password Does Not Match!"
            return render(request,'change_password.html',{'msg':msg})
    else:
        return render(request,'change_password.html')
    

def seller_index(request):
    return render(request,'seller_index.html')


def seller_change_password(request):
    if request.method=="POST":
        oldpassword=request.POST['oldpassword']
        newpassword=request.POST['newpassword']
        cnewpassword=request.POST['cnewpassword']
        user=User.objects.get(email=request.session['email'])
        if user.password==oldpassword:
            if newpassword==cnewpassword:
                user.password=cnewpassword
                user.save()
                try:
                    del request.session['email']
                    del request.session['fname']
                    msg="Password Changed Successfully.Please Login Again"
                    return render(request,'login.html',{'msg':msg})
                except:
                    return render(request,'login.html')
            else:
                msg="New Password And Confirm New Password Does Not Match!"
                return render(request,'seller_change_password.html',{'msg':msg})
        else:
            msg="Old Password Does Not Match!"
            return render(request,'seller_change_password.html',{'msg':msg})
    else:
        return render(request,'seller_change_password.html')
    
def seller_add_product(request):
    if request.method=="POST":
        seller=User.objects.get(email=request.session['email'])
        Product.objects.create(
            seller=seller,
            product_name=request.POST['product_name'],
            product_price=request.POST['product_price'],
            product_image=request.FILES['product_image'],
            product_description=request.POST['product_description'],
        )
        msg="Product Added Successfully"
        products=Product.objects.filter(seller=seller)
        request.session['product_count']=len(products)
        return render(request,'seller_add_product.html',{'msg':msg})
    else:
        return render(request,'seller_add_product.html')
    
def seller_view_product(request):
    seller=User.objects.get(email=request.session['email'])
    products=Product.objects.filter(seller=seller)
    return render(request,'seller_view_product.html',{'products':products})

def seller_product_details(request,pk):
    product=Product.objects.get(pk=pk)
    return render(request,'seller_product_details.html',{'product':product})

def seller_edit_product(request,pk):
    product=Product.objects.get(pk=pk)
    if request.method=='POST':
        product.product_name=request.POST['product_name']
        product.product_price=request.POST['product_price']
        product.product_description=request.POST['product_description']
        try:
            product.product_image=request.FILES['product_image']
        except:
            pass
        product.save()
        msg="Product Edited Successfuly"
        return render(request,'seller_edit_product.html',{'msg':msg, 'product':product})
    else:
        return render(request,'seller_edit_product.html',{'product':product})
    
def seller_delete_product(request,pk):
    seller=User.objects.get(email=request.session['email'])
    product=Product.objects.get(pk=pk)
    product.delete()
    product=Product.objects.filter(seller=seller)
    return redirect('seller_view_product')


def category(request):
    products=Product.objects.all()
    return render(request,'category.html',{'products':products})
   

def single_product(request,pk):
    product=Product.objects.get(pk=pk)
    return render(request,'single_product.html',{'product':product})

def checkout(request):
    return render(request,'checkout.html')

def cart(request):
    net_price=0
    user=User.objects.get(email=request.session['email'])
    carts=Cart.objects.filter(user=user,payment_status=False)
    for i in carts:
        net_price=net_price+i.total_price

    return render(request,'cart.html',{'carts':carts,'net_price':net_price})

def wishlist(request):
    user=User.objects.get(email=request.session['email'])
    wishlists=Wishlist.objects.filter(user=user,payment_status=False)
    return render(request,'Wishlist.html',{'wishlists':wishlists})

def add_to_wishlist(request,pk):
    product=Product.objects.get(pk=pk)
    user=User.objects.get(email=request.session['email'])
    Wishlist.objects.create(
        user=user,
        product=product
    )
    return redirect('wishlist')


def remove_from_wishlist(request,pk):
    product=Product.objects.get(pk=pk)
    user=User.objects.get(email=request.session['email'])
    wishlist=Wishlist.objects.get(user=user,product=product)
    wishlist.delete()
    return redirect('wishlist')

def add_to_cart(request,pk):
    product=Product.objects.get(pk=pk)
    user=User.objects.get(email=request.session['email'])
    Cart.objects.create(
        user=user,
        product=product,
        product_price=product.product_price,
        total_price=product.product_price,
    )
    return redirect('cart')  

def remove_from_cart(request,pk):
    product=Product.objects.get(pk=pk)
    user=User.objects.get(email=request.session['email'])
    cart=Cart.objects.get(user=user,product=product)
    cart.delete()
    return redirect('cart')

def confirmation(request):
    return render(request,'confirmation.html')

def blog(request):
    return render(request,'blog.html')

def single_blog(request):
    return render(request,'single_blog.html')

def tracking(request):
    return render(request,'tracking.html')

def profile(request):
    user=User.objects.get(email=request.session['email'])
    if request.method=="POST":
        user.fname=request.POST['fname']
        user.lname=request.POST['lname']
        user.email=request.POST['email']
        user.phone=request.POST['phone']
        user.address=request.POST['address']
        try:
            user.profile_pic=request.FILES['profile_pic']
        except:
            pass
        user.save()
        request.session['profile_pic']=user.profile_pic.url
        msg="Profile Uploaded Successfuly"
        return render(request,'profile.html',{'user':user,'msg':msg})
    else:
        return render(request,'profile.html',{'user':user})
    
def forgot_password(request):
    if request.method=="POST":
        phone=request.POST['phone']
        try:
            user=User.objects.get(phone=phone)
            otp=random.randint(1000,9999)
            url = "https://www.fast2sms.com/dev/voice"

            querystring = {"authorization":"eYLHjNJ923XdpuOB7gqnTlVPD5FzEUwQ6abGAkR0McrKSIvWimqiMTAY02jxVCHLf8rUQ5BnsJ4PX3Nb","variables_values":str(otp),"route":"otp","numbers":user.phone}

            headers = {
                'cache-control': "no-cache"
                }

            response = requests.request("GET", url, headers=headers, params=querystring)
            return render(request,'otp.html',{'phone':phone,'otp':otp})
        except:
            msg="Mobile Not Registered"
            return render(request,'forgot_password.html',{'msg':msg})
            
    else:
        return render(request,'forgot_password.html')
    
def verify_otp(request):
    phone=request.POST['phone']
    otp=request.POST['otp']
    uotp=request.POST['uotp']

    if otp==uotp:
        return render(request,'new_password.html',{'phone':phone,'otp':otp})
    else:
        msg="Incorrect OTP"
        return render(request,'otp.html',{'phone':phone,'otp':otp,'msg':msg})
    
def new_password(request):
    phone=request.POST['phone']
    np=request.POST['new_password']
    cnp=request.POST['cnew_password']

    if np==cnp:
        user=User.objects.get(phone=phone)
        user.password=np
        user.save()
        msg="Password Updated Successfully"
        return render(request,'login.html',{'msg':msg})
    else:
        msg="New Password and Confirm New Password Does not matched!"
        return render(request,'new_password.html',{'phone':phone})
<<<<<<< HEAD

def change_qty(request):

    pk=int(request.POST['pk'])
    cart=Cart.objects.get(pk=pk)
    product_qty=int(request.POST['product_qty'])
    cart.product_qty=product_qty
    cart.total_price=cart.product_price*product_qty
    cart.save()
    return redirect('cart')

def review(request):
    if request.method=="POST":
            Reviews.objects.create(
            rname=request.POST['rname'],
            remail=request.POST['remail'],
            rmobile=request.POST['rmobile'],
            rmessage=request.POST['rmessage']
        )
            msg="Review Submitted Successfully!Thank you for using our webiste."
            return render(request,'single_product.html',{'msg':msg})
    else:
            return render(request,'single_product.html')
=======
    

def change_qty(request):
    return render (request,'cart.html')
>>>>>>> 0cb652cfbb66f39b836544c05dd964d24044c638
