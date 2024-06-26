from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from .forms import CustomAuthenticationForm

# Create your views here.
def signin(request):
    next_page = request.GET.get('next', 'landing-page')

    if request.user.is_authenticated:
        return redirect(next_page)

    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Logged in as {email}")
                return redirect(next_page)
            else:
                form.add_error(None, "Invalid email or password!")
        else:
            messages.error(request, "Invalid input")
    else:
        form = CustomAuthenticationForm(request)

    return render(request, 'auth/login.html', {'form':form,'next': next_page})

def signup(request):
    if request.user.is_authenticated:
        return redirect('landing-page')

        if request.method =="POST":
            username = request.POST["username"]
            firstname= request.POST["firstname"]
            lastname= request.POST["lastname"]
            email = request.POST["email"]
            password = request.POST["password"]
            cpassword = request.POST["cpassword"]

            if User.objects.filter(username=username):
                messages.error(request,"Username already exist")
                return redirect('signup')
            if User.objects.filter(email=email):
                messages.error(request,"This email is in use. try logging in")
                return redirect('signup')
            if len(username) > 15:
                messages.error(request,"Max length of username should be 15 character")
                return redirect('signup')
            if not username.isalnum():
                messages.error(request,"username must be under 15 character")
                return redirect('signup')
            if password != cpassword:
                messages.error(request,"password didn't match")
                return redirect('signup')
            newuser= User.objects.create_user(username,email,password)
            newuser.first_name=firstname
            newuser.last_name=lastname
            if password == cpassword and username.isalnum():
                newuser.save()
                messages.success(request,'Your account has been Created /n check your email for activation')
                return redirect('login')
            else:
                messages.error(request,"Bad credential")
                return redirect('signup')
    return render(request,'auth/signup.html')

def signout(request):
    logout(request)
    messages.success(request,"Logged out")
    return redirect('login') #redicrect to home

def activate(request,uid,token):
    if request.method =="POST":
        user = User.object.filter(username=uid)
        if True:
            user["status"]=True
            messages.success(request,"Account activated,Login with your credentials")
            return redirect('login')
        else:
            messages.error(request,"Invalid User")
            return redirect()
    return render(request,'auth/activate.html')

def resetpassword(request,uid,token):
    if request.method=="POST":
        user = User.object.filter(username=uid)
        password = request.POST["password"]
        if True:
            user['password']=password
            messages.success(request,"Password Changed")
            return redirect('login')
        else:
            messages.error("Invalid Link")
            return redirect('landing-page')
    return render(request,'auth/reset_password.html')

def changepassword(request,uid,token):
    if request.method=="POST":
        user = User.object.filter(username=uid)
        oldpassword = request.POST["oldpassword"]
        password = request.POST["password"]
        if oldpassword == user['password']:
            user['password']=password
            messages.success(request,"Password Changed")
            return redirect('login')
        else:
            messages.error(request,"Invalid Link")
            return redirect('landing-page')
    return render(request,'auth/reset_password.html')