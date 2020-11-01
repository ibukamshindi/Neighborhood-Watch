from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register (request):
    if request.method=='POST':
      form=UserCreationForm(request.POST)
      if form.is_valid():
          form.save()
      return redirect('login')
    else:
      form=UserCreationForm()
    return render(request,'register.html',locals())
        
def home (request):
    current_user=request.User
    all_areas=Area.objects.all()
    return render(request,'index.html', locals())