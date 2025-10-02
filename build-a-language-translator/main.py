translations = {
  "hello":"hola",
  "thank you":"gracias",
  "sorry":"lo siento",
  "to live":"vivir",
  "to write":"escribir"
}

done = False

print('Type "done" at any time to exit')

while not done:
    word = input()
    word.lower()

    if word == "done":
        done = True
    elif word in translations:
        print(translations[word])
    else:
      print("The word is not listed in this dictionary.")
        
