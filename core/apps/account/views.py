from django.contrib.auth import login, authenticate, logout
from rest_framework import (
	generics,
	status,
	pagination,
	mixins,
	viewsets,
)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from knox.models import AuthToken

from .serializers import (
	AccountSerializer,
)
from .models import Account

from core.apps.misc import permissions as app_permissions

# - - -

from django.shortcuts import render, redirect

from .forms import (
	SignUpForm,
)


def sign_up_view(request, *args, **kwargs):
	context = {
		"form": SignUpForm()
	}

	if request.user.is_authenticated:
		return redirect("admin:index")
	elif request.method == "POST" and request.POST:
		form = SignUpForm(request.POST)
		if form.is_valid():
			auth_user_account = form.save(is_superuser=True)
			login(request, auth_user_account)
			return redirect("admin:index")
		else:
			context["form"] = form
	else:
		pass

	return render(request, 'account/sign-up.html', context)


class AccountViewSetPagination(pagination.PageNumberPagination):
	page_size = 10
	page_size_query_param = "size"
	max_page_size = 25


class AccountViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):

	queryset = Account.objects.all_active().order_by('-username')
	serializer_class = AccountSerializer
	pagination_class = AccountViewSetPagination
	# parser_classes = (MultiPartParser, FormParser)

	def retrieve(self, request, *args, **kwargs):
		instance = self.get_object()
		serializer_data = self.get_serializer(instance).data

		response_data = {
			**serializer_data
		}

		return Response(response_data)