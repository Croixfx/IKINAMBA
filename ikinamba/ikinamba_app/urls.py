from django.urls import path
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns=[
    path('',index,name=''),
    path('about/',about,name='about'),
    path('contactus/',contactus,name='contactus'),
    path('login/',login_view,name='login'),
    path('registration/', Register, name='registration'),
    path('register', RegisterView.as_view(), name='register'),
    path('register/<int:pk>/',RegisterRetrieveUpdateDelete.as_view(),name='register-detail'),
    path('useradmin/',useradmin,name='useradmin'),
    path('userDashboard/',userDashboard,name='userDashboard'),
    path('userprofile',userprofile_view,name='userprofile'),
    path('setting',setting_view,name='setting'),
    path('notification',notification_view,name='notification'),
    path('parents',pandb_view,name='parents'),
    path('vaccine',vandm_view,name='vaccine'),
    path('logout',logout_view,name='logout'),
    path('babies',babies,name='babies'),
    path('ikinamba_list',ikinambaList,name='ikinamba_list'),
    path('cars', carList, name='cars'),
    path('carView', carviewlist, name='car List'),
    path('serviceView',serviceViewList,name='service List'),
    path('services',serviceList, name='services'),
    path('ikinamba', ikinambaListCreateView.as_view(), name='ikinamba-list'), 
    path('ikinamba/<int:pk>/', ikinambaDetailView.as_view(), name='ikinamba-detail'),
    path('CarAPI', CarListCreate.as_view(), name='car-list-create'), 
    path('Servicesapi',ServiceListCreateView.as_view(),name='service-list-create'),
    path('Servicesapi/<int:pk>/',ServiceRetrieveUpdateDeleteView.as_view(), name='service-detail'),
    path('CarAPI/<int:pk>/', CarDetailView.as_view(), name='car-retrieve-update-destroy'),
    path('subscribe', SubscriptionListCreateAPIView.as_view(), name='subscribe'),
    path('subscribe/<int:pk>/', SubscriptionUpdateAPIView.as_view(), name='update_subscription'),  # Update endpoint







    ]

urlpatterns+= staticfiles_urlpatterns()
