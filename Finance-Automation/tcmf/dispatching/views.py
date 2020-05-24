from django.shortcuts import render, HttpResponse
from django.template import loader
from django.http import Http404

# Create your views here.
def index(request,userId):
    if request.method == "GET":
        return render(request, 'dispatching/index.html') 
    else:
        return HttpResponse("You are in post request")


# adding the trip to the database
def addTrip(request):
    if request.method != 'POST':
        # return HttpResponse("You need POST to this address")
        return redirect(
                request,
                'dispatching/index.html',
            )
    else:
        data = request.POST.copy()
        tripNo = data.get('tripNo')
        # checking if the fields are empty
        if not tripNo:
            # creating context with the error messages
            context = {
                'message':'Please enter all the values'
            }

            # we are rendering the index page again and sending messages as context
            return render(
                request,
                'dispatching/index.html',
                context
            )
        else:
            context = {
                'messaeg': 'Data Added'
            }
            return render(
                request,
                'dispatching/index.html',
                context
            )