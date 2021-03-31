# Whiteboard Wednesday - Interview Guide - Greetings

## Intro

This is a good general set of steps to follow to guide someone through your problem.

You'll also find some solutions embedded at the end of this doc. You can refer to them here, or in this repo's `solution.py` file.

## Guide To Guiding

- If they're initially very stuck, ask them to describe the problem back to you in English (and if they can't, help them along!). Ask them how they would translate the sentence, "If it's English, print hello. Otherwise, if it's Spanish, print hola," to code. If they still don't get it, encourage them to use an `if`!
- If they're not taking care of the case problem, ask them what would happen with inputs with different cases. For example, if they're checking for "English", ask them what would happen if the input was all lowercase, or all uppercase.
- If they see the problem but not how to fix it, ask if it would be useful to know that the case was all lowercased or all uppercased. Once they see that that would be beneficial, ask them how they could force the input into that form.
  - If they get the idea but don't remember `.lower`, ask them to invent a function that would lowercase a string and then ask them where they would use it.
- If they've got an `if`-using solution working, ask them what would happen if there were 20 languages, or 100. If they jump right to using a dictionary, awesome!
  - If they see that they could use an easier way to do it, but not how, ask them if there's a data type that could get them there. If they're thinking `list`, let them explore it (spoiler alert: it won't be pretty). When you think it's appropriate, suggest a dictionary.
    - If they don't see how a dictionary could help, give them the following metaphor (in your own words): "What if you could just turn to the right page when they said "English"--that's what a dictionary does for you. We could say that the language is the entry we could look up, and for each entry, we have a greeting attached to it."
    - If they struggle to make a dictionary, that's not uncommon at this point, and this is _great_ practice for them. Walk them through the key/value structure (and don't worry about exact syntax, a missed comma can always be caught when they run the program later!!), and lead them to the keys being the language needed. Then try to guide them to the values being the greetings, but let them mostly figure that out on their own!

## Solution(s)

```python
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
```
