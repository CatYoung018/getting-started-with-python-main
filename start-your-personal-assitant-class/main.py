# Give the class a name
class PersonalAssistant:
  def __init__(self):
      self.contacts = {'Ann': 'Marketing Coordinator', 'Chelsea': 'Software Developer', 'Nichole': 'Sales Representative', 'Max': 'Technical Writer'}
      self.todos = []

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

  # Complete the get_contact function code
  def get_contact(self, name):
    if name in self.contacts:
      return self.contacts[name]
    else:
      return "No contacts with that name."
  


# Code to test output of the class
assistant = PersonalAssistant()
assistant.add_todo("Pick up groceries")
assistant.add_todo("Iron business attire")
assistant.add_todo("Fold laundry")
print(assistant.get_todos())
assistant.get_birthday("Lorraine")
# Change name to one from your contacts
print(assistant.get_contact("Chelsea"))