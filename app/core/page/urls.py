from django.urls import path
from core.page.views import *


urlpatterns = [
    # user
    path('', search, name='search'),


]