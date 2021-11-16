from django.shortcuts import render
from user.models import UserAccount
# Create your views here.
def home_screen_view(request):
    context={}
    users=UserAccount.objects.all()
    context['users']=users
    return render(request,"personal/home.html",context)
