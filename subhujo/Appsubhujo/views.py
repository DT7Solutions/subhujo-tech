# from django.shortcuts import render

# # Create your views here.
# def home(request):
#     context={}

#     return render(request,"myApp/home.html",context)


from django.http import HttpResponse
from django.shortcuts import render
from.models import ContactData,AddJob
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render (request,"myApp/index.html",{'navbar':'home'})
def about(request):
    return render (request,"myApp/about.html",{'navbar':'about'})
def carrers(request):
    job_data = AddJob.objects.all()
    return render (request,"myApp/carrers.html",{'navbar':'carrers','job_list':job_data})

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
        jobdata = [{
        'name':'dinesh',
        'age':'28years',
        'qualification':'mca',
        'passout':'2018'
        }]
        # post_job_to_linkedin(job_data=jobdata)
        #post_job(request)
        # linkedJobPosting(request)
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
def termsconditions(request):
    return render (request,"myApp/terms-conditions.html")
def privacypolicy(request):
    return render (request,"myApp/privacypolicy.html")
def page_not_found_view(request ,exception):
    return render (request,"myApp/404.html",status=404)
def vmware_tanzu(request):
    return render(request, "myApp/vmware-tanzu.html",{'navbar':'vmware_tanzu'})
def apigee(request):
    return render(request, "myApp/apigee.html", {'navbar':'apigee'})
    
def openshift(request):
    return render(request, "myApp/openshift.html", {'navbar':'openshift'})

def apigee_consulting(request):
    return render(request, "myApp/apigee_consulting.html", {'navbar':'apigee_consulting'})

def temenos_consulting(request):
    return render(request, 'myApp/temenos_consulting.html', {'navbar':'temenos_consulting'})


import requests

import json
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient




def linkedJobPosting(job_data):
    print("this is views section!")
    title = job_data.get('Title')
    print(title)
    # for item in job_data:
    #     print(item)

    # Define the PNet API endpoint
    #PNET_API_ENDPOINT = "https://api.pnet.co.za/v1/externalfeedservice.svc/JobAdverts?apikey=<YOUR_API_KEY>&categoryId=0&countryId=0&top=100"

    # Define the LinkedIn API endpoint
    LINKEDIN_API_ENDPOINT = "https://api.linkedin.com/v2/ugcPosts"

    # Define the LinkedIn authentication token
    LINKEDIN_TOKEN = "AQW-RRLGj29rf0imUBmx-1oh9rR1kt4QV6DCdRHWK3tZgFfnBl4jue7KhWGJ5VljakzMOcL3Kz83J09VUzIyLqA_TfklPOdSuTp059qX0XBJcxlOe_zgaaSyktW8-cayi8OzKlvfiGwWtBkYSJG9mglnYQdvMlmTvMysUc8nOt7wRsnDUv4gE6_F4ZRVjGMuwaoIgY5gAYDRLP1puXFsDhf7gzb966Lub2bfMiypBkJVWxhQDI1dMLMc0DjM9dIzMfxEGPOPZHQcz1viWIwTjfLndQsDSVuLqJWrikm6SuMiEJxjwQjV4y92vZXOpFV8rfiAZHjwKLmNPvdVN1NlbwHK568vqw"

        # Retrieve the job postings from PNet
        # response = requests.get(PNET_API_ENDPOINT)
        # job_postings = json.loads(response.text)

        # Loop through the job postings and post them to LinkedIn
        # for job_posting in job_postings:
        # Create the LinkedIn post payload
    dec1 = job_data.get('ShortDescription')
    dec2 = job_data.get('LongDescription')
    exp = job_data.get('Experince')
    payload = {
                
                "author": "urn:li:person:GkIVWDje6C",
                "lifecycleState": "PUBLISHED",
                "specificContent": {    
                    "com.linkedin.ugc.ShareContent": {
                        "shareCommentary": {
                            "text": title,
                
                        },
                        # "shareMediaCategory": "NONE"
                        "shareMediaCategory": "ARTICLE",
                        "media": [
                                        {
                                            "status": "READY",
                                            "description": {
                                                "text": dec2
                                            },
                                            "originalUrl": "https://dt7solutions.com",
                                            "title": {
                                                "text": dec1
                                            },
                                            "title": {
                                                "text": exp
                                            }
                                        }
                                ]
                    }
                },
                "visibility": {
                    "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
                }
        
            }
            
    print("start Post the job posting to LinkedIn")
    response = requests.post(LINKEDIN_API_ENDPOINT, json=payload, headers={"Authorization": f"Bearer {LINKEDIN_TOKEN}"})
    print("sucesfully Post the job posting to LinkedIn")
    return ''





'''
def linkedJobPosting(request):
    # Define the PNet API endpoint
    PNET_API_ENDPOINT = "https://api.pnet.co.za/v1/externalfeedservice.svc/JobAdverts?apikey=<YOUR_API_KEY>&categoryId=0&countryId=0&top=100"

    # Define the LinkedIn API endpoint
    LINKEDIN_API_ENDPOINT = "https://api.linkedin.com/v2/ugcPosts"

    # Define the LinkedIn authentication token
    LINKEDIN_TOKEN = "<YOUR_LINKEDIN_TOKEN>"

        # Retrieve the job postings from PNet
        response = requests.get(PNET_API_ENDPOINT)
        job_postings = json.loads(response.text)

        # Loop through the job postings and post them to LinkedIn
        for job_posting in job_postings:
            # Create the LinkedIn post payload
            payload = {
                "author": f"urn:li:organization:<YOUR_ORGANIZATION_ID>",
                "lifecycleState": "PUBLISHED",
                "specificContent": {
                    "com.linkedin.ugc.ShareContent": {
                        "shareCommentary": job_posting["jobTitle"],
                        "media": [
                            {
                                "status": "READY",
                                "description": {
                                    "text": job_posting["jobDescription"]
                                },
                                "media": job_posting["jobUrl"]
                            }
                        ]
                    }
                },
                "visibility": {
                    "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
                }
            }
            
            # Post the job posting to LinkedIn
            response = requests.post(LINKEDIN_API_ENDPOINT, json=payload, headers={"Authorization": f"Bearer {LINKEDIN_TOKEN}"})
    
    return ''

    '''


# (or)

''' 
url = "https://api.pnet.co.za/v1/externalfeedservice.svc/JobAdverts"
api_key = "YOUR_API_KEY"

params = {
    "apikey": api_key,
    "categoryId": 0,
    "countryId": 0,
    "top": 100
}

response = requests.get(url, params=params)

if response.status_code == 200:
    job_adverts = response.json()
    # Do something with the job adverts
else:
    print("Failed to retrieve job adverts from Pnet API.")

    '''