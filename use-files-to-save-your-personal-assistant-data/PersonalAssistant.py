# Give the class a name
class PersonalAssistant:
  def __init__(self, todos):

    self.todos = todos

  def add_todo(self, new_item):
    self.todos.append(new_item)

  def remove_todo(self, todo_item):
    if todo_item in self.todos:
        # Get the todo_item index in list
        index = self.todos.index(todo_item)
        # pop the index for todo_item in todos list
        self.todos.pop(index)
    else:
        print("Todo is not in list!")

  def get_todos(self):
    return self.todos

  def get_birthday(self, name):
    if name == "Robert":
      print("Birthday is 1/8/54!")
    elif name == "Lorraine":
      print("Birthday is 3/13/55!")
    elif name == "RJ":
      print("Birthday is 6/10/82!")
    else:
      print("Can't find a birthday for this person...")


  
