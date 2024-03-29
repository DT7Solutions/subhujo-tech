# from .  import views
# from django.urls import path

# urlpatterns = [
#     path('', views.home),
#     path('/about-us', views.about),
   
# ]

from django.urls import path
from .views import home,about,carrers,contact,application_development,vmware_tanzu,apigee,openshift,apigee_consulting,temenos_consulting,termsconditions,privacypolicy,corporate_training,sap,dataware_housing,oracle,microsoft_implementation,testing,offshore_development,page_not_found_view,it_ites_staffing
urlpatterns = [
    path('', home, name='home'),
    path('about_us/', about, name='about_us'),
    path('careers/', carrers, name='carrers'),
    path('contact/', contact, name='contact'),
    path('application_development/',application_development, name='application_development'),
    path('corporate_training/',corporate_training, name='corporate_training'),
    path('dataware_housing/',dataware_housing, name='dataware_housing'),
    path('it_ites_staffing/',it_ites_staffing, name='it_ites_staffing'),
    path('microsoft_implementation/',microsoft_implementation, name='microsoft_implementation'),
    path('vmware_tanzu/',vmware_tanzu, name='vmware_tanzu'),
    path('apigee/',apigee, name='apigee'),
    path('openshift/',openshift, name='openshift'),
    path('apigee_consulting/',apigee_consulting,name='apigee_consulting'),
    path('temenos_consulting/',temenos_consulting,name='temenos_consulting'),
    path('oracle/',oracle, name='oracle'),
    path('sap/',sap, name='sap'),
    path('testing/',testing, name='testing'),
    path('terms-conditions/',termsconditions, name='terms-conditions'),
    path('privacypolicy/',privacypolicy, name='privacypolicy'),
    path('offshore_development/',offshore_development, name='offshore_development'),
    path('not_found/',page_not_found_view, name='not_found'),

]