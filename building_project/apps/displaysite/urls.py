from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'displaysite'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:product_id>/', views.product, name='product'),
    path('loyaltyprogram/', views.loyaltyprogram, name='loyaltyprogram'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('contacts/', views.contacts, name='contacts'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)