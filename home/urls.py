from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


#urlconfig for ever app ill create
urlpatterns = [
    path('', views.index, name='index'),
    path('volunteer', views.volunteer, name = 'volunteer'),
    path('donate', views.donate, name='donate'),
    path('contact', views.contact,name='contact' ),
    path('team', views.team_list, name='team'),
    path('events', views.events_list, name='events'),
    path('about', views.about, name='about'),    
    path('shop', views.shop, name='shop'),    
    path('resources', views.resources, name='resources'), 
    path('faq', views.faq, name='faq'), 
   path('program/<int:pk>/', views.program_details, name='program-details'),
   path('search/', views.search, name='search'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)