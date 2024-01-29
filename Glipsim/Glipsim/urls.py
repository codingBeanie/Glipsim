from django.contrib import admin
from django.urls import path
from server.views import *
from server.api import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', index, name='index'),
    path('', index, name='index'),
    path('restart', restart, name='restart'),
    path('run', run, name='run'),
    path('households', households, name='households'),
    path('probabilities', probabilities, name='probabilities'),

    # API
    path('api/get_stats', API_Stats.as_view(), name='api_stats'),
    path('api/get_households', API_Households.as_view(), name='api_households')
]
