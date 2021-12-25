from django.urls import path
from index.views import hello, index_html

urlpatterns = [
    path('', hello),
    path('index_html', index_html),
]