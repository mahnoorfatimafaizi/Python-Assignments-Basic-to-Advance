import random 

# Generate a random number between 1 and 100
random_generated_number: int = random.randint(1,100)

allowed_attempts: int = 5

user_attempts: int = 0

while True:
 print(f"Attempts left: {allowed_attempts - user_attempts}")

 if (user_attempts == allowed_attempts):
  print("Sorry your attempt finished")
  break
 
# Get User Number 
 user_input: int = int(input("Enter User Number: "))
 user_attempts  += 1
 
 if user_input == random_generated_number:
  print("Congratulations! You guessed the correct number.")
  break 
 if user_input > random_generated_number:
  print("Too High! Try again.")
 elif user_input < random_generated_number:
  print("Too Low! Try")







  


