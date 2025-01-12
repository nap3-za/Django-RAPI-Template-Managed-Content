from django.conf import settings
from django.contrib.auth import authenticate
from rest_framework import serializers
from dj_rest_auth.serializers import PasswordResetSerializer
from phonenumber_field.serializerfields import PhoneNumberField

from .models import Account


class SignUpSerializer(serializers.ModelSerializer):
	password2   					= serializers.CharField(style={"input_type":"password"}, allow_blank=False, write_only=True)

	class Meta:
		model = Account
		fields = [
			"username",
			"name",
			"surname",
			"gender",

			"email",
			"phone_number",

			"accept",

			"password",
			"password2"
		]
		extra_kwargs = {
			"password":{"write_only":True},
			"password2":{"write_only":True},
		}

	def create(self, validated_data):
		password = validated_data["password"]
		confirm_password = validated_data["password2"]

		if password != confirm_password:
			raise serializers.ValidationError("Passwords do not match")
		else:
			del validated_data["password2"]
			return Account.objects.create_superuser(**validated_data)


class AccountSerializer(serializers.ModelSerializer):

	class Meta:
		model = Account
		fields = (
			"id",
			"username",
			"name",
			"surname",
			"gender",
			"profile_image",

			"email",
			"phone_number",
		)
		read_only_fields = (
			"id",
		)

	def update(self, instance, validated_data):
		pass

	def create(self, validated_data):
		pass

