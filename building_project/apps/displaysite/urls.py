from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'displaysite'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:product_id>/', views.product, name='product'),
    path(r'^$', views.product, name='product'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)