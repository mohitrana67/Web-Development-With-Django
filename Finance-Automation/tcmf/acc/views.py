from django.shortcuts import render, HttpResponse
from django.template import loader
from django.http import Http404
from .model import CSV

import csv,io

# Create your views here.

# fucntion rendering the accounting index page
def index(request, userId):
    context = {'userId': userId}

    return render(request, 'acc/index.html', context)
    # return HttpResponse(result)

# function to generate the quartley report
def quartleyReport(request,qtr,year,userId):
    result = str(userId) + " wants to generate a report for the quarter "+ str(qtr) + " for the year of "+ str(year)

    return HttpResponse(result)

# function to upload file to the server
def uploadFile(request):
    if request.method == 'POST' and request.FILES['uploadedFile']:
        uploadedFile = request.FILES['uploadedFile']
        uploadedFileName = request.FILES['uploadedFile'].name
        errorMessage = "Please upload a csv file only"
        if not uploadedFileName.endswith('.csv'):   
            return HttpResponse("you have uploaded a file " + errorMessage)
        else:
            readCSV = CSV(uploadedFile, 1)

            csv = readCSV.read_csv_with_filelocation()
            
            if csv !=[]:
                result = "Csv file is not empty"
            else:
                result = "you did not get csv file"

            return HttpResponse(result)
    else:
        return HttpResponse("You are not rendering a post")