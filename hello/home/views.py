from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("This is HomePage")
    context = {
        'variable_1':"this is sent",
        'variable_2':"I'm getting a hang of it"
    }
    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "services.html")

def contact(request):
    return render(request, "contact.html")




  