print(" GENERAL KNOWLEDGE QUIZ ")

score = 0

# Question 1
answer1 = input("Q1: What is the capital of France? \n Answer: ").strip().lower()
if answer1 == "paris":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is Paris.")

# Question 2
answer2 = input("\nQ2: Which planet is known as the Red Planet? \n Answer: ").strip().lower()
if answer2 == "mars":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is Mars.")

# Question 3
answer3 = input("\nQ3: Who developed Python programming language? \n Answer:").strip().lower()
if answer3 == "guido van rossum":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is Guido van Rossum.")

# Final Score
print("\n RESULT ")
print("Your score is:", score, "/ 3")

# Feedback
if score == 3:
    print("Excellent! 🎉")
elif score == 2:
    print("Good job 👍")
else:
    print("Keep practicing 💪")