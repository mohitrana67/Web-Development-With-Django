var data_head = document.getElementById("expense_data")

// Function to Load the trips via ajax call.
function load_trips(data_head){
    const expense_data_row = data_head
    const xhr = new XMLHttpRequest()
    const method = 'GET'
    // we have to get user id here to make it much more dynamic
    const url = '/accounting/1/expenses_list'
    const responseType = "json"
    xhr.responseType = responseType

    xhr.open(method, url)

    xhr.onload = function(){
        var response = xhr.response.response
        console.log(typeof(xhr.response))
        var expense_list = ""
        var i
        for(i=0;i<response.length;i++){
            current_expense = response[i]
            // we have to decide what we will do with the data we get from the reponse
            // console.log("Id is", current_expense.id)
            expense_list += "<tr><td>"+current_expense.expense_account_type+"</td><td>"+current_expense.expense_transaction_date+"</td><td>"+current_expense.expense_name+"</td><td>"+current_expense.expense_description_1+"</td><td>"+current_expense.expense_description_2+"</td><td>"+current_expense.expense_amount_cad+"</td><td>"+current_expense.expense_amount_usd+"</td><td>"+current_expense.expense_gst+"</td><td>"+current_expense.expense_pst+"</td><td>"+current_expense.expense_pvt+"</td></tr>"
        }
        expense_data_row.innerHTML = expense_list
    }

    xhr.send()
}

// Fucntion to add the trips with the ajax call.
function handleTripAddFormDidSubmit(event){
    event.preventDefault()
            
    const addTripForm = event.target
    const addTripData = new FormData(addTripForm)
    const url = addTripForm.getAttribute("action")
    const method = addTripForm.getAttribute("method")

    const xhr = new XMLHttpRequest();
    xhr.responseType = "json"
    const requestMethod = method
    //  Be aware that we are in accouinting/home and we need to render dispatching/trips so we need to go one trr level down -->
    //  We have to define the url we are targetting to get data from-->
    const requestURL = '/accounting/1/add_accouting_expense'
    xhr.open(method, url)
    xhr.setRequestHeader("HTTP_X_REQUESTED_WITH","XMLHttpRequest")
    xhr.setRequestHeader("X-Requested-With","XMLHttpRequest")
    xhr.onload = function() {
        var serverResponse = xhr.response
        console.log(serverResponse)
        load_trips(data_head)
        addTripForm.reset()
    }
    xhr.send(addTripData)
}

// Function to add the expense csv data
function handleLoadCSVFormDidSubmit(event){
    event.preventDefault()
            
    const addCSVDataForm = event.target
    const addCSVData = new FormData(addCSVDataForm)
    const url = addCSVDataForm.getAttribute("action")
    const method = addCSVDataForm.getAttribute("method")

    const xhr = new XMLHttpRequest();
    xhr.responseType = "json"
    const requestMethod = method
    //  Be aware that we are in accouinting/home and we need to render dispatching/trips so we need to go one trr level down -->
    //  We have to define the url we are targetting to get data from-->
    const requestURL = '/accounting/1/add_csv_data'
    xhr.open(method, url)
    xhr.setRequestHeader("HTTP_X_REQUESTED_WITH","XMLHttpRequest")
    xhr.setRequestHeader("X-Requested-With","XMLHttpRequest")
    xhr.onload = function() {
        var serverResponse = xhr.response.response
        const lenOfDataArray = (xhr.response.response).length
        for(var i=0; i<lenOfDataArray; i++){
            console.log(serverResponse[i])
        }
    }
    xhr.send(addCSVData)
}

const add_epense_form = document.getElementById("add_expense_form")
add_epense_form.addEventListener("submit", handleTripAddFormDidSubmit)

const add_csv_expense = document.getElementById("load_csv_data")
add_csv_expense.addEventListener("submit", handleLoadCSVFormDidSubmit)

load_trips(data_head)
