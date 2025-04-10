from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.
def index(request):
        return render(request, 'index.html')
#    return HttpResponse('<h1>Hey, welcome</h1>')
    # context = {
    #     'name': 'Kaustav',
    #     'age': 21,
    #     'nationality': 'Indian',
    # }
    # return render(request, 'index.html', context)

#return render(request, 'index.html', 'name': name)

def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())   #gives no of words
    return render(request, 'counter.html', {'amount': amount_of_words})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2'] 
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already used")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
            
        else:
            messages.info(request, "Password Not Mathching")
            return redirect('register')
    else:
        return render(request, 'register.html')
    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')
    
def logout(request):
    user = auth.logout(request, user)
    return redirect('/')

def post(request, pk):
    return render(request, 'post.html', {'pk':pk})

def cnt(request):
    posts = [1, 2, 3, 4, 5, 'tim', 'kaustav', 'john']
    return render(request, 'cnt.html', {'posts': posts})
    
    