angular.module('todoApp', [])
  .controller('TodoListController', function() {
    var todoList = this;
    todoList.input = []
    todoList.input.name = "";
    todoList.input.due = "";
    todoList.input.diff = "";

    todoList.todos = [
      {id:1, task_name:'learn AngularJS', time_to_do:10, default: false,done: false},
      {id:2, task_name:'build an AngularJS app', time_to_do:60, default: false, done: false}];

    todoList.update = function(){
      $.ajax(
          {url: "localhost/getTodo",
          success: function(result){
            console.log(result)
        }});
    }

    todoList.addTask = function(){
      console.log({id:3, task_name:todoList.input.name,time_to_do:10, default: false,done: false })
      todoList.todos.push({id:3, task_name:todoList.input.name,time_to_do:10, default: false,done: false })
    }

    todoList.done = function(id){
      for(i in todoList.todos){
        if(todoList.todos[i]["id"] == id){
          console.log(i)
          todoList.todos[i]["done"] = true;

        }
      }
    }
  });
