from django.urls import path
from . import views

# app_name = "trade"
from .views import monitor

urlpatterns = [
    path('', views.IndexPageView.as_view(), name='home'),
    path('ws/monitor', monitor),
    path('auth/signin', views.SigninView.as_view(), name='signin'),
    path('auth/recoverpw', views.RecoverPWView.as_view(), name='recoverpw'),
    path('extra/privacy-policy', views.PrivacyPolicyView.as_view(), name='policy'),
    path('extra/terms-of-service', views.TermsOfServiceView.as_view(), name='terms'),
    path('icons/', views.IconsView.as_view(), name='icons'),
    path('error/<int:error>', views.ErrorsView.as_view(), name='error'),
    path('map/', views.MapView.as_view(), name='map'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('profile/policy-settings', views.UserPrivacySettingsView.as_view(), name='privacy_setting'),

]
