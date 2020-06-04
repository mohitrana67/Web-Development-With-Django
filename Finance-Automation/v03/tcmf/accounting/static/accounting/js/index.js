var expense_data_row = document.getElementById("expense_data_row")

const xhr = new XMLHttpRequest()
const method = 'GET'

const url = '../../expense_list'
// const responseType = "json"
// xhr.responseType = responseType

// console.log("We are opening xhr request here")
// xhr.open(method, url)

// xhr.onload = function(){
//     var response = xhr.response.response

//     var expense_list = ""
//     var i
//     for(i=0;i<response.length;i++){
//         current_expense = response[i]
//         // we have to decide what we will do with the data we get from the reponse
//         console.log(current_expense.id)
//         expense_list += "<td>"+current_expense.expense_account_type+"</td><td>"+current_expense.expense_transaction_date+"</td><td>"+current_expense.expense_name+"</td><td>"+current_expense.expense_description_1+"</td><td>"+current_expense.expense_description_2+"</td><td>"+current_expense.expense_amount_cad+"</td><td>"+current_expense.expense_amount_usd+"</td><td>"+current_expense.expense_gst+"</td><td>"+current_expense.expense_pst+"</td><td>"+current_expense.expense_pvt+"</td>"
//     }
//     expense_data_row .innerHTML = expense_list
// }

// xhr.send()

console.log("You are here")