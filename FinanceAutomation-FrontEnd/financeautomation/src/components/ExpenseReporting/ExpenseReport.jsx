import React from "react"
import "./ExpenseCard.css"

class ExpenseReport extends React.Component {
    constructor(props){
        super(props)

        this.state = {
            isLoggedIn: this.props.lofinFlag
        }
    }

    render(){
        return (
            <div>
                
            </div>
        )
    }
}

export default ExpenseReport;