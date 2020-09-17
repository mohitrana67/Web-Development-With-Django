import React from "react"
import "../Header/Header.css"

function Links(props){
    return <li><a href="#">{props.name}</a></li>
}

function Header() {
    return <div className="navbar-fixed">
        <nav>
            <div className="nav-wrapper">
            <a href="#" className="brand-logo">Finance Wizard</a>
            <ul id="nav-mobile" className="right hide-on-med-and-down">
                <Links name="Home" />
                <Links name="Login" />
                <Links name="Logout" />
            </ul>
            </div>
        </nav>
    </div>
}

export default Header;