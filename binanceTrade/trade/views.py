from django.shortcuts import render, HttpResponse, Http404, HttpResponseRedirect
from django.views.generic import View

# Create your views here.
# def index_page(request):
#     return render(request, 'trade/index.html')


class IndexPageView(View):
    template_name = 'trade/index.html'

    def get(self, request):
        context = {}
        return render(request, template_name=self.template_name, context=context)

    def post(self):
        pass


class PrivacyPolicyView(View):
    template_name = 'trade/extra/privacy-policy.html'

    def get(self, request):
        return render(request, template_name=self.template_name)


class TermsOfServiceView(View):
    template_name = 'trade/extra/terms-of-service.html'

    def get(self, request):
        return render(request, template_name=self.template_name)


# User profile chapter
class UserProfileView(View):
    template_name = 'trade/app/user-profile.html'

    def get(self, request):
        return render(request, template_name=self.template_name)


class UserPrivacySettingsView(View):
    template_name = 'trade/app/user-privacy-setting.html'

    def get(self, request):
        return render(request, template_name=self.template_name)


class UserAccountSettingsView(View):
    template_name = 'trade/app/user-account-setting.html'

    def get(self, request):
        return render(request, template_name=self.template_name)


# Authentication chapter
class SigninView(View):
    template_name = 'trade/auth/sign-in.html'

    def get(self, request):
        return render(request, template_name=self.template_name)


class RecoverPWView(View):
    templates = 'trade/auth/recoverpw.html'


class MapView(View):
    templates = 'trade/map/google.html'


class IconsView(View):
    templates = 'trade/icons/outline.html'


class ErrorsView(View):
    templates = 'trade/errors/error404.html'