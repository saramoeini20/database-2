from django import forms

from user.models import UserAccount 


class CreateUserAccountForm(forms.ModelForm):

	class Meta:
		model = UserAccount
		fields = ['name', 'family','phonenumber','birthdate','gender','address']

class UpdateUserAccountForm(forms.ModelForm):

	class Meta:
		model = UserAccount
		fields = ['name', 'family','phonenumber','birthdate','gender','address']

	def save(self, commit=True):
		user_account = self.instance
		user_account.name = self.cleaned_data['name']
		user_account.family = self.cleaned_data['family']
		user_account.phonenumber = self.cleaned_data['phonenumber']
		user_account.birthdate = self.cleaned_data['birthdate']
		user_account.gender = self.cleaned_data['gender']
		user_account.address = self.cleaned_data['address']

		if commit:
			user_account.save()
		return user_account