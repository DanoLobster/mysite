from django.contrib import admin
from django.urls import path, include
from wardrobe.views import add_clothing, view_clothing
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from wardrobe import views
from django.views.generic import TemplateView
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('add-clothing/', views.add_clothing, name='add_clothing'),
    path('view-clothing/', views.view_clothing, name='view_clothing'),
    path('accounts/', include('accounts.urls')),
    path('delete-clothing/', views.delete_clothing, name='delete_clothing'),
    path('delete-outfit/', views.delete_outfit, name='delete_outfit'),
    path('test/', views.test, name='test'),
    path('view-outfit/', views.view_outfit, name='view_outfit'),
    path('add-outfit/', views.add_outfit, name='add_outfit'),
    path('about/', views.about, name='about'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
