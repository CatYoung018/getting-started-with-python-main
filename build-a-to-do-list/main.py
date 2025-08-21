todo_list = []
done = False

print("Type 'done' at any time to exit")

while not done:
    task = new_item = input("Please add an item to your todo list:")
    if new_item == "done":
        done = True
    else:
        todo_list.append(new_item)


for item in todo_list:
    print("Your todo list:" + " " + item)





