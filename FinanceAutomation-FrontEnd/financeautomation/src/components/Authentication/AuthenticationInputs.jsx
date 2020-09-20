const RegisterInputs = [
    {
        key:1,
        type: "text",
        name: "email",
        placeholder: "Please enter your email"
    },
    {
        key:2,
        type: "text",
        name: "username",
        placeholder: "Please enter your username"
    },
    {
        key:3,
        type: "text",
        name: "fname",
        placeholder:"Please enter First Name"
    },
    {
        key:4,
        type: "text",
        name: "lname",
        placeholder:"Please enter Last Name"
    },
    {
        key:4,
        type: "password",
        name: "password1",
        placeholder:"Please enter your password"
    },
    {
        key:4,
        type: "password",
        name: "password2",
        placeholder:"Please re-enter your password"
    },
    {
        key:5,
        type:"submit",
        value: "Register"
    }
]

const LoginInputs = [
    {
        kry:1,
        type:"text",
        name:"email",
        placeholder:"Please enter your email"
    },
    {
        key:2,
        type:"password",
        name:"password",
        placeholder:"Please enter your password"
    },
    {
        key:3,
        type:"submit",
        value:"Login"
    }
]

export {LoginInputs, RegisterInputs}