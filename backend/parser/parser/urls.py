from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path, include
# from card.views import search


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('card.urls')),
    # path('api/search/', search, name='search'),
]