# Django import
from django import forms
# Third-Party import
from django_otp.admin import AdminAuthenticationForm, AdminSite, OTPAuthenticationFormMixin
# Local import
from otp_auth.utils import verify_token


class __OTPAuthenticationFormMixin(OTPAuthenticationFormMixin):
    def _verify_token(self, user, token, device=None):
        return verify_token(user, token, device)


class OTPAdminAuthenticationForm(AdminAuthenticationForm, __OTPAuthenticationFormMixin):
    otp_device = forms.CharField(required=False, widget=forms.Select)
    otp_token = forms.CharField(required=False)
    otp_challenge = forms.CharField(required=False)

    def clean(self):
        self.cleaned_data = super().clean()
        self.clean_otp(self.get_user())
        return self.cleaned_data


class OTPAdminSite(AdminSite):
    name = 'otpadmin'
    login_template = 'otp/admin111/login.html'
    login_form = OTPAdminAuthenticationForm

    def __init__(self, name='otpadmin'):
        super().__init__(name)

    def has_permission(self, request):
        return super().has_permission(request) and request.user.is_verified()