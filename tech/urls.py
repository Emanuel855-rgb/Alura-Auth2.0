from django.urls import path
from tech.views import index, membros
urlpatterns = [
    path('', index, name='url_index'),
    path("membros/", membros, name="url_membros")
]
