from django.contrib import admin

from .models import Account
from knox.models import AuthToken

# Register your models here.
# pg 78 docs

class AuthTokenInline(admin.StackedInline):
	model = AuthToken
	extra = 0

class AccountAdmin(admin.ModelAdmin):

	fieldsets = [
		("Personal information", {"fields": [
			"username",
			"name",
			"surname",
			"gender",
			"email",
			"phone_number",
		]}),
	]
	list_display = ["username", "name", "surname"]

	inlines = [AuthTokenInline]


admin.site.register(Account, AccountAdmin)