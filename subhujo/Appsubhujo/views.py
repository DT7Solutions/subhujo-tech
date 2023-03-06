# from django.shortcuts import render

# # Create your views here.
# def home(request):
#     context={}

#     return render(request,"myApp/home.html",context)


from django.shortcuts import render
from.models import ContactData
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.
def home(request):
    return render (request,"myApp/index.html",{'navbar':'home'})
def about(request):
    return render (request,"myApp/about.html",{'navbar':'about'})
def carrers(request):
    return render (request,"myApp/carrers.html",{'navbar':'carrers'})

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        phone = request.POST.get('phone',"")
        subject = request.POST.get('subject',"")
        message = request.POST.get('message',"")
        oContactinfo = ContactData(Name=name,Email=email,Phone=phone,Subject=subject,Message=message)
        oContactinfo.save()
        sucess =f'hi {name} Your message has been received, We will contact you soon'
        try:
            send_mail(subject, message,'noreplaysubhujotechnologies@gmail.com',recipient_list=['subhujotechnologies@gmail.com']) 
            messages.success(request,sucess)
        except:
            messages.error(request,'Your message has been failed, Please Try Agian')

    return render (request,"myApp/contact.html",{'navbar':'contact'})

def application_development(request):
    return render (request,"myApp/Application-development.html" ,{'navbar':'Application-development'})
def corporate_training(request):
    return render (request,"myApp/Corporate-training.html" ,{'navbar':'Corporate-training'})
def dataware_housing(request):
    return render (request,"myApp/dataware_housing.html" ,{'navbar':'dataware_housing'})
def it_ites_staffing(request):
    return render (request,"myApp/it_ites_staffing.html", {'navbar':'it_ites_staffing'})
def oracle(request):
    return render (request,"myApp/Oracle.html",{'navbar':'Oracle'})
def offshore_development(request):
    return render (request,"myApp/offshore_development.html",{'navbar':'offshore_development'})
def sap(request):
    return render (request,"myApp/Sap.html",{'navbar':'Sap'})
def testing(request):
    return render (request,"myApp/testing.html",{'navbar':'testing'})
def microsoft_implementation(request):
    return render (request,"myApp/microsoft_implementation.html",{'navbar':'microsoft_implementation'})
    
    
    
    
