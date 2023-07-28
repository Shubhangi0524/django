from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        "variable":"This is Anita Kadam",
        "variable1":"This is Shubhangi"
    }
    return render(request, 'index.html',context)
    # return HttpResponse("This is homepage")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is aboutpage")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse("This is servicepage")

def contacts(request):
    return render(request, 'contacts.html',)
    # return HttpResponse("This is contactpage")