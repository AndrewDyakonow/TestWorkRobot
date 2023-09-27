from django.urls import path

from robots.apps import RobotsConfig
from robots.views import add_robo

app_name = RobotsConfig.name

urlpatterns = [
    path('', add_robo, name='robot_create'),
]
