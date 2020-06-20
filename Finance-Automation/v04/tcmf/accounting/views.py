from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404, JsonResponse

from .forms import *
from .classes import *

# Create your views here.
def home_view(request,*args,**kwargs):
    return render(
        request = request,
        template_name = 'accounting/index.html',
        context=None,
        content_type=None,
        status=None,
        using=None
    )

# API to store data in the accounting expense table in tcmf database.
def add_accounting_expense(request,*args,**kwargs):
    """
    The main task of this view is to create an API for storing accouting expenses in the database.
    """
    context = {}    #we are creating a context dictonary to send as a response to the request
    message = ""    #messages we will send
    status = 0  #status to check if data is saved or not

    """
    Now we will do all the validation on the data we received
        1.  First of all we will check for if we received either CAD amount or USD amout
        2.  Second, we will check if we received a float valud for all the numberic fields amount field
    """

    if not request.POST["expense_account_type"] or not request.POST["expense_transaction_date"] or not request.POST["expense_name"]:
        message = "Please enter all the necessary values"
        status = 401
    else:
        """
        Getting all the values we are getting from the post request
        """
        expense_account_type = request.POST.get("expense_account_type")
        expense_transaction_date = request.POST.get("expense_transaction_date")
        expense_name = request.POST.get("expense_name")
        expense_description_1 = request.POST.get("expense_description_1") or "There is no description"
        expense_description_2 = request.POST.get("expense_description_2") or "There is no description"
        expense_amount_cad = request.POST.get("expense_amount_cad") or 0
        expense_amount_usd = request.POST.get("expense_amount_usd") or 0
        expense_gst = request.POST.get("expense_gst") or 0
        expense_pst = request.POST.get("expense_pst") or 0
        expense_pvt = request.POST.get("expense_pvt") or 0

        date = expense_transaction_date.split('-')
        expense_year = int(float(date[0]))
        expense_month = int(date[1])
        current_flag = "N"  #setting flag to see if all the values we are getting are correct
        if expense_amount_cad == 0 and expense_amount_usd == 0:
            message = "Amount should be entered"
            status = 401
        else:
            if expense_amount_cad == 0:
                try:
                    expense_amount_usd = float(expense_amount_usd)
                    current_flag = "Y"
                except:
                    message = "You have to enter a numberical value for the Amounts"
                    status = 401
            else:
                try:
                    expense_amount_cad = float(expense_amount_cad)
                    current_flag = "Y"
                except:
                    message = "You have to enter a numberical value for the Amounts"
                    status = 401

        quarter1 = [1,2,3]
        quarter2 = [4,5,6]
        quarter3 = [7,8,9]
        quarter4 = [10,11,12]
        expense_quarter = 0
        if expense_month in quarter1:
            expense_quarter = 1
        elif expense_month in quarter2:
            expense_quarter = 2
        elif expense_month in quarter3:
            expense_quarter = 3
        elif expense_month in quarter4:
            expense_quarter = 4
        """
        Now we need to store the data we received from the form
        """
        if current_flag == "Y":
            expense = Expense(
                expense_account_type = expense_account_type,
                expense_transaction_date = expense_transaction_date,
                expense_name = expense_name,
                expense_description_1 = expense_description_1,
                expense_description_2 = expense_description_2,
                expense_amount_cad = expense_amount_cad,
                expense_amount_usd = expense_amount_usd,
                expense_gst = expense_gst,
                expense_pst = expense_pst,
                expense_pvt = expense_pvt,
                expense_quarter = expense_quarter,
                expense_year = expense_year
            )
            # we are checking if data saved or not
            try:
                # expense.save()
                message = "Expense saved"
                status = 200
            except:
                message = "Expense Not Saved"
                status = 401
        # return HttpResponse(error_message)
    context = {
        "message":message,
        "status":status,
    }

    print(context)
    if request.is_ajax():
            return JsonResponse(context) # 201 is for created items
    # return render(
    #     request = request,
    #     template_name = "accounting/index.html",
    #     context = {"message":error_message}
    # )

# API to show list of all the expenses.
def expenses_list(request,*args,**kwargs):
    data = {}
    expenses = Expense.objects.all()
    expense_list = [x.serialize() for x in expenses]
    data["response"] = expense_list

    return JsonResponse(data,status=200)

# API to load the csv and save data in database
def add_csv_data(request, *args, **kwargs):
    context = {
        "message": "",
        "response": []   
    }
    if request.method == 'POST' and request.FILES['uploadedFile']:  # We are cehcking if the request we are getting from the form is the POST request and the FILE field actually has something in it
        uploadedFile = request.FILES['uploadedFile']    # We are getting all the varible from the uploded file
        uploadedFileName = request.FILES['uploadedFile'].name   # getting the name of the uploaded file to check whether the file uploaded is a csv file or not
        if not uploadedFileName.endswith('.csv'):   # checking if the file we received is a csv file and throw the error if the file received is not a csv file
            context["message"] = "Please upload a csv file"
        else:
            data_set = uploadedFile.read().decode('utf-8')  # read the csv file and decoding it with utf-8 format so that we can use it in the fuction we creatred in ReadCSV class
            read_csv = ReadCSV(data_set)    # calling the csv class to read csvs
            csv = read_csv.read_csv()   # getting the resultback from the read_csv funtion and assiging it to the variable csv. read_csv function is returning a list of all the csv elements with rows seperated by the array in the array [[row1],[row2],.....,[rowN]]
            quarter = 1
            full_date = csv[-1][2].split('/')    # converting the date into the database accepted date
            year = int(full_date[2])
            month = int(full_date[0])
            account_type = csv[-1][0]
            if account_type == 'Chequing':
                docuemnt_type = 'Debit'
            else:
                docuemnt_type = 'Credit'
            
            if month in [1,2,3]:
                quarter = 1
            elif month in [4,5,6]:
                quarter = 2
            elif month in [7,8,9]:
                quarter = 3
            else:
                quarter = 4
            for i in range(len(csv)):   # iteratin over the csv file to get all the values from the csv data we got from function call
                if  i==0:   # checking if we are iterating the first row of the csv data. First row is the row with the Headers
                    context["csv_header"] = csv[i]
                else:
                    csv[i].pop()    # poping out the last column of the data arrays as our file has an extra blank colum at the end
                    try:
                        csv[i][6] = float(csv[i][6])    # coverting CAD string values to the float values
                    except:
                        pass
                    try:
                        csv[i][7] = float(csv[i][7])    # Converting USD string values to the float values
                    except:
                        pass
                    type_of_cad = type(csv[i][6])
                    type_of_usd = type(csv[i][7]) 
                    if type_of_cad != float:   # now for the USD amounts the CAD values will be balnk and converting them to float will return nuthing
                        pass
                    else:
                        file_date = csv[i][2].split('/')    # converting the date into the database accepted date
                        file_year = file_date[2]
                        file_date = file_date[1]
                        file_month = file_date[0]
                        formatted_date = file_year+ '-' + file_month + '-' + file_date
                        csv[i][2] = formatted_date
                        if (csv[i][6] >= 0.0):
                            expense_transaction_date= formatted_date
                            expense_account_type = csv[i][0]    
                            expense_name = 'Revenue'
                            expense_description_1 = csv[i][4]
                            expense_description_2 = csv[i][5]
                            expense_amount_cad = csv[i][6] or '0.0'
                            expense_amount_usd = csv[i][7] or '0.0'
                            try:
                                expense_amount_usd = float(expense_amount_usd)
                            except:
                                pass
                            try:
                                expense_amount_cad = float(expense_amount_cad)
                            except:
                                pass

                            expense = Expense(
                                expense_account_type = expense_account_type,
                                expense_transaction_date = expense_transaction_date,
                                expense_name = expense_name,
                                expense_description_1 = expense_description_1,
                                expense_description_2 = expense_description_2,
                                expense_amount_cad = expense_amount_cad,
                                expense_amount_usd = expense_amount_usd,
                                expense_quarter = quarter,
                                expense_year = year,
                                docuemnt_type = docuemnt_type
                            )
                            try:
                                # expense.save()
                                context["message"] = "Data saved Successfully"
                                # return HttpResponse(csv)
                            except:
                                context["message"] = "Please contact administration, data didnt saved correctly."
                        else:
                            csv[i].pop(1)
                            # csv[i].pop(2)
                            # print(csv[i])
                            context["response"].append(csv[i])
        return JsonResponse(context)
        # new_value = csv[len(csv)-1][7] + 1.0
        # return HttpResponse(new_value)
        # return HttpResponse(csv[0][8])
    else:
        message = "File type is not csv"
        # return HttpResponse("You are not rendering a post")
