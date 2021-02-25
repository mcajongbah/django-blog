from django.urls import path
from django.views.generic import TemplateView

app_name = 'users'

urlpatterns = [
    path('', TemplateView.as_view(template_name = 'home/homepage.html'), name='home' )
]
