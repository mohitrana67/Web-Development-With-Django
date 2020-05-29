import pandas as pd

from django.shortcuts import render, HttpResponse
from django.template import loader
from django.http import Http404
from .model import CSV

from .classes import ReadCSV

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
        context = {}
        if not uploadedFileName.endswith('.csv'):   
            context = {
                "error_message":errorMessage
            }
        else:
            data_set = uploadedFile.read().decode('utf-8')

            # calling the csv class to read csv
            read_csv = ReadCSV(data_set)
            csv = read_csv.read_csv()
            test = []

            for i in range(len(csv)):
                """We will be converting all the cad and usd values to float
                    We have to use multiple try block for multiple values.
                """
                try:
                    csv[i][6] = float(csv[i][6])
                except ValueError:
                    pass
                
                try:
                    csv[i][7] = float(csv[i][7])
                except ValueError:
                    pass

                if i == 0:
                    pass
                else:
                    csv[i].pop()
                
                csv[i].pop(3)

            context = {
                "csv_header":csv[0],
                "csv_data":csv[1:]
            }

        # new_value = csv[len(csv)-1][7] + 1.0
        # return HttpResponse(new_value)
        # return HttpResponse(csv[0][8])
        return render(
            request,
            "acc/index.html",
            context
        )
    else:
        return render(
            request,
            'acc/index.html'
        )
        # return HttpResponse("You are not rendering a post")

# function to add data to the backend
def addData(request):
    if request.method == 'POST':
        result = 123
    # getting post values with request.POST
    return HttpResponse('')
