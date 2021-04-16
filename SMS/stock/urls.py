from django.conf.urls import url
from . import views 
app_name = 'stock'

urlpatterns = [
    url(r'^brand/create/$',views.BrandCreateView.as_view(),name='create_brand'),
    url(r'^brand/list/$',views.BrandListView.as_view(),name='list_brand'),
    url(r'^brand/delete/(?P<pk>[-\w]+)/$',views.BrandDeleteView.as_view(),name='delete_brand'),
    url(r'^brand/update/(?P<pk>[-\w]+)/$',views.BrandUpdateView.as_view(),name='update_brand'),
    url(r'^category/create/$',views.CategoryCreateView.as_view(),name='create_category'),
    url(r'^category/list/$',views.CategoryListView.as_view(),name='list_category'),
    url(r'^category/delete/(?P<pk>[-\w\d\s]+)/$',views.CategoryDeleteView.as_view(),name='delete_category'),
    url(r'^category/update/(?P<pk>[-\w\d\s]+)/$',views.CategoryUpdateView.as_view(),name='update_category'),
    url(r'^product/create/$',views.ProductCreateView.as_view(),name='create_product'),
    url(r'^product/list/$',views.ProductListView.as_view(),name='list_product'),
    url(r'^product/delete/(?P<pk>[-\w\d\s]+)/$',views.ProductDeleteView.as_view(),name='delete_product'),
    url(r'^product/update/(?P<pk>[-\w\d\s]+)/$',views.ProductUpdateView.as_view(),name='update_product'),
    url(r'^order/create/$',views.OrderCreateView.as_view(),name='create_order'),
    url(r'^order/list/$',views.OrderListView.as_view(),name='list_order'),
    url(r'^order/detail/(?P<pk>[-\w\d\s]+)/$',views.OrderDetailView.as_view(),name='order_detail'),
]