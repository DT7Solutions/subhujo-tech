# from django.shortcuts import render

# # Create your views here.
# def home(request):
#     context={}

#     return render(request,"myApp/home.html",context)


from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request,"myApp/index.html")
def about(request):
    return render (request,"myApp/about.html")
def carrers(request):
    return render (request,"myApp/carrers.html")
def contact(request):
    return render (request,"myApp/contact.html")
def application_development(request):
    return render (request,"myApp/Application-development.html")
def corporate_training(request):
    return render (request,"myApp/Corporate-training.html")
def dataware_housing(request):
    return render (request,"myApp/dataware_housing.html")
def it_ites_staffing(request):
    return render (request,"myApp/it_ites_staffing.html")
def oracle(request):
    return render (request,"myApp/Oracle.html")
def offshore_development(request):
    return render (request,"myApp/offshore_development.html")
def sap(request):
    return render (request,"myApp/Sap.html")
def testing(request):
    return render (request,"myApp/testing.html")
def microsoft_implementation(request):
    return render (request,"myApp/Microsoftimplementation.html")
    
    
    
    
