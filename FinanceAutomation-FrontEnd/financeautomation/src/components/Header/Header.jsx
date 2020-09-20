import React from  "react"
import Authentication from "../Authentication/Authentication.jsx"
import ExpenseReport from "../ExpenseReporting/ExpenseReport.jsx"

class Header extends React.Component{

    constructor(props){
        super (props)
        this.state = {
            IsLoggedIn: true,
            ClickedLogin: false,
            ClickedHome: true,
            ClickedAbout: false,
        }
    }

    ShowAuthentication() {
        this.setState({
            ClickedLogin : true,
            ClickedHome : false,
            ClickedAbout : false,
        })
    }

    ShowHome() {
        this.setState({
            ClickedLogin : false,
            ClickedHome : true,
            ClickedAbout : false,
        })
    }

    ShowAbout() {
        this.setState({
            ClickedLogin : false,
            ClickedHome : false,
            ClickedAbout : true,
        })
    }

    render(){
        return(
            <div>
                <div>
                    <nav>
                        <div class="nav-wrapper">
                            <a onClick={() => this.ShowHome()} class="brand-logo">FinanceWizard</a>
                        <ul id="nav-mobile" class="right hide-on-med-and-down">
                            <li><a onClick={() => this.ShowHome()}>Home</a></li>
                            <li><a onClick={() => this.ShowAuthentication()}>Login/Register</a></li>
                            <li><a onClick={() => this.ShowAbout()}>About</a></li>
                        </ul>
                        </div>
                    </nav>
                </div>
                <div>
                    {this.state.ClickedHome === true ? <ExpenseReport lofinFlag={this.state.IsLoggedIn} />: null}
                    {this.state.ClickedLogin === true? <Authentication />: null}
                    {this.state.ClickedAbout === true? <center><h1>You want about me</h1></center>: null}
                </div>
            </div>
        )
    }
}

export default Header;