from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'displaysite'
urlpatterns = [
    path('', views.index, name='index'),#main page
    path('<int:product_id>/', views.product, name='product'),#product page
    path('loyaltyprogram/', views.loyaltyprogram, name='loyaltyprogram'),#loyalty program page
    path('signup/', views.signup, name='signup'),#signup page
    path('login/', views.login, name='login'),
    path('contacts/', views.contacts, name='contacts'),
    path('cart/', views.cart, name='cart'),
    path('allproducts/', views.allproducts, name='allproducts'),
    path('about/', views.about, name='about'),
    path('myaccount/', views.myaccount, name='myaccount'),
    path('logout', views.logout_view, name='logout'),
    path('product/<int:product_id>/makeorder/', views.makeorder, name='makeorder'),
    path('cancel_order/<int:order_id>/', views.cancel_order, name='cancel_order'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:cartitem_id>/', views.remove_from_cart, name='remove_from_cart'),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)