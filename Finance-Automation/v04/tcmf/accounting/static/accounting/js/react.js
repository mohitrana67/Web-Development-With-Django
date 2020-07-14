class App extends React.Component{
    render() {
        return (
            <div>
                <Counter />
            </div>
        )
    }
}

class Counter extends React.Component{
    constructor(props){
        super(props)
        this.state = {
            num1: Math.floor((Math.random() *10) + 1),
            num2: Math.floor((Math.random() *10) + 1),
            score:0,
            response:""
        }
    }

    render(){
        return(
            <div>
                <h1>
                    {this.state.num1} + {this.state.num2}
                </h1>
                <div>
                    <input type="text" value={this.state.response}/>
                </div>
            </div>
        )
    }

    increment = () => {
        if(this.state.count === 5){
            this.setState(state => ({
                count : 0
            }))
        }
        else{
            this.setState(state => ({
                count : state.count + 1
            }))
        }
    }
}

ReactDOM.render(<App />, document.querySelector("#root"))