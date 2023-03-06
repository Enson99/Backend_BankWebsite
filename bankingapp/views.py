from django.shortcuts import render,redirect 
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import HttpResponseRedirect,HttpResponse
from .models import Account
from .forms import ApplicationForm




# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password'] 
        confirm_password = request.POST['confirm_password'] 
        if password==confirm_password:
             if User.objects.filter(username=username).exists(): 
                messages.info(request, 'username already exists ') 
                return redirect(register)
             else:
                 user = User.objects.create_user(username=username,password=password) 
                 user.set_password(password)
                 user.save()
                 
                 return redirect('login')
            
    else:
        print("no post method")
        return render(request,'register.html')


def login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		check_user = User.objects.filter(username=username, password=password)
		if check_user:
			request.session['user'] = username
			return redirect('newpage')
		else:
			return HttpResponse('Please enter valid Username or Password.')

	return render(request, 'login.html')
    
def newpage(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            dob = form.cleaned_data['dob']
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            address = form.cleaned_data['address']
            district = form.cleaned_data['district']
            branch = form.cleaned_data['branch']
            account_type = form.cleaned_data['account_type']
            materials_provided = form.cleaned_data['materials_provided']

        Account.objects.create(
            name=name,
            dob=dob,
            age=age,
            gender=gender,
            phone=phone,
            email=email,
            address=address,
            district=district,
            branch=branch,
            account_type=account_type,
            materials_provided=materials_provided   
        )
             
        Account.save()
            
        return HttpResponseRedirect('home')
    else:
        form = ApplicationForm()
    return render(request, 'newpage.html', {'form': form})
         
        
def success(request):
    if request.method == 'POST':
     return redirect('')
    return render(request,"success.html")
