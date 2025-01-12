from django import forms
from django.contrib.auth.forms import UserCreationForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Row, Column, Submit, HTML, Div

from .models import Account


class SignUpForm(UserCreationForm):

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			Row(
				Column("name", css_class="form-group col-sm-6"),
				Column("surname", css_class="form-group col-sm-6"),
			),
			
			"gender",
			Row(
				Column("email", css_class="form-group col-sm-6"),
				Column("phone_number", css_class="form-group col-sm-6"),
			),
			"username",
			Row(
				Column("password1", css_class="form-group col-sm-6"),
				Column("password2", css_class="form-group col-sm-6"),
			),
			"accept",
			Submit("submit", "Sign up", css_class="btn btn-primary btn-block")
		)


	class Meta:
		model = Account
		fields = (
			"username",
			"name",
			"surname",
			"gender",
			"password1",
			"password2",

			"email",
			"phone_number",

			"accept",
		)

	def clean_accept(self):
		accept = self.cleaned_data["accept"]
		if not accept:
			raise forms.ValidationError(f"You must accept the privacy policy and terms of use to continue")
		return accept

	def save(self, is_superuser=False, commit=False):
		account = None

		del self.cleaned_data["password1"]
		self.cleaned_data["password"] = self.cleaned_data["password2"]
		del self.cleaned_data["password2"]

		if is_superuser:
			account = Account.objects.create_superuser(**self.cleaned_data)
		else:
			account = Account.objects.create_user(**self.cleaned_data)

		return account
