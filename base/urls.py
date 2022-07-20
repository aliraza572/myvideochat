from django.urls import path 
from .views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', test_view, name='test_view'),
]