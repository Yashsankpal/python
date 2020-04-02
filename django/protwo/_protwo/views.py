from django.shortcuts import render
from _protwo.models import User
from _protwo.form import Nameform
# Create your views here.

def index(request):
    return render(request, 'protwo/index.html')

def user(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'user':user_list}
    return render(request, 'protwo/user.html', context=user_dict)

def form(request):
    form_ = Nameform()
    if request.method == "POST":
        form_ = Nameform(request.POST)
        if form_.is_valid():
            form_.save(commit=True)
            return user(request)
        else:
            print("Error yes !!")
    return render(request,'protwo/form.html',{'form':form_})   