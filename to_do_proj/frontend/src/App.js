import React, { Component } from "react";
import axios from "axios";

const list = [
  {
    id: 1,
    title: "First To-do item",
    body: "My first task is to create this task.",
  },
  {
    id: 2,
    title: "Second task",
    body: "Create a new task other than the first.",
  },
  {
    id: 3,
    title: "Third",
    body: "This is my third to-do.",
  },
];

class App extends Component {
  state = {
    todos: [],
  };

  componentDidMount() {
    this.getTodos();
  }

  getTodos() {
    axios
      .get("http://127.0.0.1:8000/api/")
      .then((res) => {
        this.setState({ todos: res.data });
      })
      .catch((err) => {
        console.log(err);
      });
  }

  render() {
    return (
      <div>
        {this.state.todos.map((item) => (
          <div key={item.id}>
            <h1>{item.title}</h1>
            <span>{item.body}</span>
          </div>
        ))}
      </div>
    );
  }
}

export default App;
