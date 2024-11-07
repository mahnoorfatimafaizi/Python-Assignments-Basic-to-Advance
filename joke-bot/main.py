PROMPT:str = "What do you want?"
JOKE: str = "Why did the math book look sad? \n Because it had too many problems!"

def joke_bot():
    user_input = input(PROMPT)
    print(user_input)

    if user_input.lower() == "joke":
      print(JOKE)
    else:
      print("Sorry, I only tell Jokes.")

joke_bot()