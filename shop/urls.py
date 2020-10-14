from django.urls import path, include
from . import views
from .views import *


app_name = 'shop'


urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('my_account/', views.my_account, name='my_account'),
    # path('shopping/', views.shopping, name='shopping'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('detail/', views.detail, name='detail'),
    path('blog/', views.blog, name='blog'),
    path('applications/', views.ApplicationsView.as_view(), name='applications'),
    # path('shop2/', views.listing, name='listing')
    # path('shop/', views.ShopListView.as_view(), name='shop'),
    # path('<slug:category_slug>/', views.shopping, name='product_list_by_category'),
    # path('<int:id>/<slug:slug>/', views.product_details, name='product_detail'),
]