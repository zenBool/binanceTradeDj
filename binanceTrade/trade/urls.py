from django.urls import path
from . import views

# app_name = "trade"
urlpatterns = [
    path('', views.IndexPageView.as_view(), name='home'),
    path('extra/privacy-policy', views.PrivacyPolicyView.as_view(), name='policy'),
    path('extra/terms-of-service', views.TermsOfServiceView.as_view(), name='terms'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('profile/policy-settings', views.UserPrivacySettingsView.as_view(), name='privacy_setting'),
    path('auth/signin', views.SigninView.as_view(), name='signin'),
    path('extra/privacy-policy', views.PrivacyPolicyView.as_view(), name='privacy'),
    path('extra/terms-of-service', views.TermsOfServiceView.as_view(), name='terms'),
]
