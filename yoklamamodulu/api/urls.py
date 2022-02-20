from django.urls import path

from yoklamamodulu.api.views import DersView

urlpatterns = [
    path('list/',DersView.as_view(),name='list'),

]
