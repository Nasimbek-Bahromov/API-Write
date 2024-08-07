from . import views
from .views import BannerListView, BannerCreateView, BannerDetailView, BannerUpdateView, BannerDeleteView
from .views import ServiceListView, ServiceCreateView, ServiceDetailView, ServiceUpdateView, ServiceDeleteView
from .views import InfoListView, InfoCreateView, InfoDetailView, InfoUpdateView, InfoDeleteView
from django.urls import path

urlpatterns = [
    path('contact/list', views.contact_list),

    path('banners/list', BannerListView.as_view(), name='banner_list'),
    path('banners/create/', BannerCreateView.as_view(), name='banner_create'),
    path('banners/detail/<int:pk>/', BannerDetailView.as_view(), name='banner_detail'),
    path('banners/update/<int:pk>/', BannerUpdateView.as_view(), name='banner_update'),
    path('banners/delete/<int:pk>/', BannerDeleteView.as_view(), name='banner_delete'),

    path('service/list', ServiceListView.as_view(), name='service_list'),
    path('service/create/', ServiceCreateView.as_view(), name='service_create'),
    path('service/detail/<int:pk>/', ServiceDetailView.as_view(), name='service_detail'),
    path('service/update/<int:pk>/', ServiceUpdateView.as_view(), name='service_update'),
    path('service/delete/<int:pk>/', ServiceDeleteView.as_view(), name='service_delete'),

    path('info/list', InfoListView.as_view(), name='info_list'),
    path('info/create/', InfoCreateView.as_view(), name='info_create'),
    path('info/detail/<int:pk>/', InfoDetailView.as_view(), name='info_detail'),
    path('info/update/<int:pk>/', InfoUpdateView.as_view(), name='info_update'),
    path('info/delete/<int:pk>/', InfoDeleteView.as_view(), name='info_delet')

]