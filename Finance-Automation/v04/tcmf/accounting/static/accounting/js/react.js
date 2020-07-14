class App extends React.Component{
    render() {
        return (
            <div>
                <ToDoList />
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

// This is the class for to do list
class ToDoList extends React.Component{
    constructor(props){
        super(props)
        this.state = {
            tasks:[],
            input: ""
        }
    }

    render(){
        return(
            <div>
                <h1>
                    Tasks
                </h1>
                <ul>
                    {this.state.tasks.map((tasks, i) =>
                         <li key={i}>
                             {/* way of calling a funtion and calling it without the parameter is {() => this.deleteTask(i)} */}
                             {tasks} <button data-index={i} onClick={this.deleteTask}>Delete</button>
                         </li>
                    )}
                </ul>
                <input onChange={this.handleChange} value={this.state.input} />
             
                <button onClick={this.addTask}>Add Task</button>
                <div>
                    Number Of tasks = {this.state.tasks.length}
                </div>
            </div>
        )
    }

    handleChange = (event) => {
        this.setState({
            input: event.target.value
        })
    }
    addTask = (event) => {
        this.setState(state => {
            return{
                tasks: [...state.tasks, state.input],
                input: ""
            }
        })
        // this.setState(state => ({
        //     tasks: [...state.tasks, state.input],
        //     input: ""
        // }))
    }

    deleteTask = (event) => {
        const index = event.target.dataset.index
        this.setState(state => {
            const tasks = [...state.tasks]
            tasks.splice(index,1)
            return{
                tasks: tasks
            }
        })
    }
}

ReactDOM.render(<App />, document.querySelector("#root"))