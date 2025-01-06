
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static

from account import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('account/', include('account.urls')),

    path('invoice_app/', include('invoice_app.urls')),

    path('', views.index, name='index'),
]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)