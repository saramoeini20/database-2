from django.shortcuts import render

from user.models import UserAccount
from user.forms import CreateUserAccountForm, UpdateUserAccountForm

def create_user_view(request):

	context = {}

	user = request.user

	form = CreateUserAccountForm(request.POST or None)
	if form.is_valid():
		obj = form.save(commit=False)
		obj.save()
		form = CreateUserAccountForm()

	context['form'] = form

	return render(request, 'user/create_user.html', context)
#find and show detail
def find_view(request):
	return render(request, 'user/find_user.html', {})

def detail_user_view(request):
	
	context = {}
	# user_account = get_object_or_404(UserAccount,slug=phonenumber)
	query = request.GET.get('q')
	user_account=UserAccount.objects.filter(phonenumber=query)
	context['user_account'] = user_account

	return render(request, 'user/detail_user.html', context)


#show all user
def all_user_view(request):
    context={}
    users=UserAccount.objects.all()
    context['allusers']=users
    return render(request, 'user/all_user.html',context)


#find user and update
def findedit_view(request):
	return render(request, 'user/findedit_user.html', {})

def editform_user_view(request):

	context = {}
	query = request.GET.get('q')
	user_account=UserAccount.objects.filter(phonenumber=query)

	_initial=[]
	for u in user_account:
		_initial.append(u)

	if request.POST:
		form = UpdateUserAccountForm(request.POST or None,instance=user_account[0])
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			context['success_message'] = "Updated"
			user_account = obj	

	if  len(_initial) != 0 :
		form = UpdateUserAccountForm(
			initial={
					"name": _initial[0].name,
					"family":  _initial[0].family,
					"phonenumber":  _initial[0].phonenumber,
					"birthdate": _initial[0].birthdate,
					"gender": _initial[0].gender,
					"address": _initial[0].address

			}
		)
		context['form'] = form

	else:
		context['success_message'] = "Failed"
		return render(request, 'user/findedit_user.html', context)

	return render(request, 'user/editform_user.html', context)