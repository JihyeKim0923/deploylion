from django.contrib import admin
from django.urls import path, include
import review,accounts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('review/', include('review.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
]
