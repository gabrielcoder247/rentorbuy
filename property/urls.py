# from django.conf.urls import url
# from . import views

# urlpatterns=[
#     url('^$',views.welcome,name = 'welcome'),
# ]



from django.conf.urls import url, include
# from django.conf import settings
# from django.conf.urls.static import static
from . import views as core_views
from . import views

urlpatterns=[
    url(r'^$',views.index,name = 'index_page'),
    # url(r'^single_listing/(\d+)/$',views.single_listing,name='single_listing'),
    # url(r'^new/listing$',views.listing,name='listing_form'),
    # url(r'^signup/$', core_views.signup, name='signup'),
    # url(r'^booking/(\d+)/$', views.booking, name='booking'),
    # url(r'^profile/(?P<username>[0-9]+)$',views.profile, name='profile'),
    # url(r'^new/image$',views.new_image,name='new_image'),
    # url(r'^listing/times(\d+)/$',views.listing_times,name='listing_times'),
    
    
]


# if settings.DEBUG:
#     urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)