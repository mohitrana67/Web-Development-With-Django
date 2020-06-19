function myfunction(event){
    event.preventDefault()
    alert('Click me')
}

var form = document.createElement('form')
form.setAttribute(onsubmit='myFunction')
var input = documenet.createElement('input')
input.type = 'submit'

form.appendChild(input)

document.getElementById('test').appendChild(form)