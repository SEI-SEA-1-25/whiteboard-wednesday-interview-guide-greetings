language = input("What language does the person speak?").lower()

# using a dictionary
dictionary = {
  "english": "Hello!",
  "spanish": "Hola!",
  "french": "Bonjour!",
}

print(dictionary[language])

# using if/elif
if language == "english":
  print("Hello!")
elif language == "spanish":
  print("Hola!")
elif language == "french":
  print("Bonjour!")
