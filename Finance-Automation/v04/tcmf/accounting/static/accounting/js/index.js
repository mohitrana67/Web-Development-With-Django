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
    // console.log("You are in adding expense")
    event.preventDefault()

    // alert(event)
            
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
        console.log(serverResponse.message)
        // addTripForm.style.display = "none"
        // load_trips(data_head)
        // addTripForm.reset()
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
    const expense_data_row = document.getElementById("expense_data")
    xhr.onload = function() {
        var serverResponse = xhr.response
        // console.log(serverResponse)
        var lenOfDataArray = (serverResponse.response).length
        var tbody = document.getElementById('expense_data')
        // NOw we have to iterate over the response to get all the rows of the response
        for(var i=0; i<lenOfDataArray; i++){
            // Now we have to create a form for every row we get in response
            var row = document.createElement('tr')
            row.className="tr"+i
            var csvExpenseForm = document.createElement('form')
            csvExpenseForm.setAttribute('onsubmit','handleTripAddFormDidSubmit(event)')
            csvExpenseForm.setAttribute('action','1/add_accouting_expense')
            csvExpenseForm.setAttribute('method', 'POST')
            // now we have to create the data rows and the input fields for the form
            // we have total of 10 rows 6 from the data we received, 3 for gst pst and pvt and 1 for submit buttons
            var csrf = document.querySelectorAll('input[name=csrfmiddlewaretoken]')[0].value
            
            var csrf_input = document.createElement('input')
            csrf_input.setAttribute('name', 'csrfmiddlewaretoken')
            csrf_input.setAttribute('value', csrf)
            csrf_input.setAttribute('type', 'hidden')

            csvExpenseForm.appendChild(csrf_input)
            for(var j=0; j<11; j++){
                // creating a table data for storing the input field
                var tableData = document.createElement('td')

                // creating the input for the table data
                var inputField = document.createElement('input')
                if(j==0){
                    inputField.name = 'expense_account_type'
                    inputField.disabled = false
                    inputField.type = 'text'
                    inputField.value = serverResponse.response[i][j]
                }else if(j==1){
                    inputField.name = 'expense_transaction_date'
                    inputField.disabled = false
                    inputField.type = 'text'
                    inputField.value = serverResponse.response[i][j]
                }else if(j==2){
                    inputField.name = 'expense_name'
                    inputField.disabled = false
                    inputField.type = 'text'
                    inputField.placeholder='Please enter expense type'
                    // inputField.value = serverResponse.response[i][j]
                }else if(j==3){
                    inputField.name = 'expense_description_1'
                    inputField.disabled = false
                    inputField.type = 'text'
                    inputField.value = serverResponse.response[i][j-1]
                }else if(j==4){
                    inputField.name = 'expense_description_2'
                    inputField.disabled = false
                    inputField.type = 'text'
                    inputField.value = serverResponse.response[i][j-1]
                }else if(j==5){
                    inputField.name = 'expense_amount_cad'
                    inputField.disabled = false
                    inputField.type = 'number'
                    inputField.step = "0.01"
                    inputField.value = serverResponse.response[i][j-1]
                }else if(j==6){
                    inputField.name = 'expense_amount_usd'
                    inputField.disabled = false
                    inputField.type = 'number'
                    inputField.step = "0.01"
                    inputField.value = serverResponse.response[i][j-1]
                }else if(j==7){
                    inputField.name = 'expense_gst'
                    inputField.placeholder = 'GST'
                    inputField.type = 'number'
                    inputField.step = "0.01"
                    inputField.disabled = false
                }else if(j==8){
                    inputField.name = 'expense_pst'
                    inputField.placeholder = 'PST'
                    inputField.type = 'number'
                    inputField.step = "0.01"
                    inputField.disabled = false
                }else if(j==9){
                    inputField.name = 'expense_pvt'
                    inputField.placeholder='PVT'
                    inputField.type = 'number'
                    inputField.step = "0.01"
                    inputField.disabled = false
                }else{
                    inputField.type='submit'
                }

                tableData.appendChild(inputField)
                csvExpenseForm.appendChild(tableData)
            }
            
            // appending form to the tr
            row.appendChild(csvExpenseForm)
            tbody.appendChild(row)
        }
        document.getElementById("add-individual-expense").style.display = "none"
        // create the form <form> element

        // document.getElementById("expense_data").appendChild()
        // expense_data_row.innerHTML = expense_list
        // console.log("you hit with error message" + serverResponse.message)
    }
    xhr.send(addCSVData)
}

const add_epense_form = document.getElementById("add_expense_form")
add_epense_form.addEventListener("submit", handleTripAddFormDidSubmit)

const add_csv_expense = document.getElementById("load_csv_data")
add_csv_expense.addEventListener("submit", handleLoadCSVFormDidSubmit)


// I have to check if the file being uploaded by the client is already there or not