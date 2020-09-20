import React from "react"
import {LoginInputs,RegisterInputs} from "../Authentication/AuthenticationInputs.jsx"
import '../Authentication/Authentication.css'

class Authentication extends React.Component{
    
    constructor(props){
        super (props)
        this.state = {
            isRegistered: false
        }
    }

    switchAuthenticationPanels(flag) {

        this.setState({
            isRegistered: flag
        })
    }

    render(){
        return (
            <div className="authetication-container">
                <center>
                    <div className="Authentication">
                        <form name={this.state.isRegistered === false?"LoginForm":"RegisterForm"}>
                            {
                                this.state.isRegistered === false ? LoginInputs.map( x => 
                                <div>
                                    <input type={x.type} name={x.name} placeholder={x.placeholder} value = {x.type === "submit"?x.value:null} />
                                    <br />
                                </div>): 
                                RegisterInputs.map( x => 
                                <div>
                                    <input type={x.type} name={x.name} placeholder={x.placeholder} value={x.type === "submit"?x.value:null} />
                                    <br />
                                </div>)
                            }
                        </form>
                        {
                            this.state.isRegistered === false? 
                            <a onClick={() => this.switchAuthenticationPanels(true)}>
                                Wanna Register
                            </a> :
                            <a onClick={() => this.switchAuthenticationPanels(false)}>
                                Already have an account
                            </a> 
                        }
                    </div>
                </center>
            </div>
        )
    }
}

export default Authentication