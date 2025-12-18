print("Welcome to the Python Quiz Game")

questions = [
    "1) Which keyword is used to start a loop in Python?\nA) loop\nB) for\nC) repeat\n",
    "2) Which data type is immutable?\nA) List\nB) Tuple\nC) Dictionary\n",
    "3) What is the output of 5 % 2?\nA) 0\nB) 1\nC) 2\n"
]

answers = ("b", "b", "b")

score = 0
i = 0

while i < len(questions):
    print(questions[i])
    user_ans = input("Enter your answer (A/B/C) or type 'exit' to quit: ").lower()

    if user_ans == answers[i]:
        print("Correct!\n")
        score += 1
    elif user_ans == "exit":
        print("Game Exited")
        break
    else:
        print("Wrong Answer\n")

    i += 1

print(f"Final Score: {score}/3")

if score == 3:
    print("Perfect Score! Well done!")
elif score == 2:
    print("Good Job! Keep practicing!")
else:
    print("Try again!")
