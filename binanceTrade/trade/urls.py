from django.urls import path
from . import views

app_name = "trade"
urlpatterns = [
    path('', views.IndexPageView.as_view(), name='home'),
    path('extra/privacy-policy', views.PrivacyPolicyView.as_view(), name='privacy'),
    path('extra/terms-of-service', views.TermsOfServiceView.as_view(), name='terms'),
]
