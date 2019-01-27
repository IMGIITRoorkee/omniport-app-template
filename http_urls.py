from django.urls import path

from [[app_name]].views.hello_world import HelloWorld

app_name = '[[app_name]]'

urlpatterns = [
    path('', HelloWorld.as_view(), name='hello_world'),
]
