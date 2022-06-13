from django.shortcuts import render, HttpResponse, Http404, HttpResponseRedirect
from django.views.generic import View

# Create your views here.
# def index_page(request):
#     return render(request, 'trade/index.html')


class IndexPageView(View):
    template_name = 'trade/index.html'

    def get(self, request):
        context ={}
        return render(request, template_name=self.template_name, context=context)

    def post(self):
        pass


class PrivacyPolicyView(View):
    template_name = 'trade/extra/privacy-policy.html'

    def get(self, request):
        return render(request, template_name=self.template_name)