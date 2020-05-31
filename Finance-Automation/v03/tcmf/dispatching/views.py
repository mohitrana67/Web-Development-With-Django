from django.shortcuts import render, redirect   
from django.http import HttpResponse, Http404, JsonResponse

from .models import *

from .forms import *

# Create your views here.
def trip_home_view(request,*args, **kwargs):
    # return HttpResponse(f"Hello") 
    return render(
        request = request,
        template_name = "dispatching/home.html",
        context = None,
        content_type = None,
        status = None,
        using = None,
    )
# View to get information about the trip 
def trip_data(request,dispatcher_id,trip_id):
    """
    REST API View
    Consumed by JavaScript or Swift/Java/iOS/Android
    return json data
    """
    data = {
        "tripId":trip_id,
    }
    status = 200
    try:
        tripData = Trip.objects.get(id=trip_id)
        data["tripNo"]=tripData.trip_no
        data["originCity"]=tripData.origin_city
        data["destinationCity"]=tripData.destination_city
    except:
        data["error_message"] = "You dont have a trip with trip id " + str(trip_id)
        status = 404
    # return HttpResponse(f"Trip {tripData.trip_no} is going from {tripData.origin_city} to {tripData.destination_city}")
    return JsonResponse(data,status=status)

# view to list all the trips we have in the database
def trips_list(request,*args,**kwargs):
    """
    REST API view
    Consumed by JavaScript or Swift/Java/iOS/Android
    return json data
    """
    data = {

    }
    try:
        list = Trip.objects.all()
        trips_list=[{"id":x.id,"trip_no":x.trip_no,"origin_city":x.origin_city,"destination_city":x.destination_city} for x in list]
        data["response"] = trips_list
    except:
        data["response"] = "We dont have any trips at the moment"
    
    return JsonResponse(data)

# view to creat new trip
def create_trip(request,*args,**kwargs):
    form = AddTripForm(request.POST or None)
    
    next_url = request.POST.get("next") or None

    # we are checking if we are getting any data in the form already
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        if next_url != None:
            return redirect(next_url)
        # form = AddTripForm()
        
        # we can print in terminal using this
        print(f"next_url is {next_url}")
    return render(
        request = request,
        template_name = "components/form.html",
        context = {"form":form}
    )