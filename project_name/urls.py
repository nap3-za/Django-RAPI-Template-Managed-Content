from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from core.apps.account import views as account_views


urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path('sign-up/', account_views.sign_up_view, name="sign-up"),

    path('account/', include('core.apps.account.urls', namespace="account")),

    # Password related views using 3rd party app
    path("password_reset/", auth_views.PasswordResetView.as_view(template_name="account/password-reset/reset.html"), name="password_reset"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(template_name="account/password-reset/reset_done.html"), name="password_reset_done"),
    path("password_reset/complete/", auth_views.PasswordResetCompleteView.as_view(template_name="account/password-reset/reset_complete.html"), name="password_reset_complete"),    
    path("password_reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="account/password-reset/reset_confirm.html"), name="password_reset_confirm"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)