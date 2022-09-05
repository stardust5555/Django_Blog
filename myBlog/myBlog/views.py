from django.http import HttpResponse    #This allows us to send a response to the user. So when they request a page we send something back


#Function that fires when a user visits the homepage 
    #Just sends back a http response (which is just a string for the moment)
def homepage(request):
    return HttpResponse('homepage')

    #Function that fires when a user visits the /about page
    #Just sends back a http response (which is just a string for the moment)
def about(request):
    return HttpResponse('about')