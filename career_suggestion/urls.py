# career_suggestion/urls.py

from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='recommendations/', permanent=False)),  # Redirect root URL
    path('recommendations/', include('recommendations.urls')),
]
