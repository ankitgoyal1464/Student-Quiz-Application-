
print("================================")
print("     STUDENT QUIZ APPLICATION")
print("================================")

student_name = input("Enter your name: ")

questions = [
    {
        "question": "1. Which language is used for Python programming?",
        "options": ["A. HTML", "B. Python", "C. CSS", "D. SQL"],
        "answer": "B"
    },
    {
        "question": "2. Which function is used to display output in Python?",
        "options": ["A. input()", "B. print()", "C. display()", "D. show()"],
        "answer": "B"
    },
    {
        "question": "3. Which data type stores multiple values in Python?",
        "options": ["A. List", "B. Integer", "C. Float", "D. Boolean"],
        "answer": "A"
    },
    {
        "question": "4. Which symbol is used for comments in Python?",
        "options": ["A. //", "B. <!-- -->", "C. #", "D. **"],
        "answer": "C"
    },
    {
        "question": "5. Which keyword is used for a loop in Python?",
        "options": ["A. repeat", "B. for", "C. loop", "D. next"],
        "answer": "B"
    }
]

score = 0

print("\nWelcome", student_name)
print("\nQuiz has started!")
print("--------------------------------")

for q in questions:
    print("\n" + q["question"])

    for option in q["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    while user_answer not in ["A", "B", "C", "D"]:
        print("Invalid choice! Please enter A, B, C or D.")
        user_answer = input("Enter your answer: ").upper()

    if user_answer == q["answer"]:
        print("Correct Answer!")
        score += 1
    else:
        print("Wrong Answer!")
        print("Correct answer:", q["answer"])

print("\n================================")
print("          QUIZ RESULT")
print("================================")

print("Student Name:", student_name)
print("Total Questions:", len(questions))
print("Correct Answers:", score)
print("Wrong Answers:", len(questions) - score)

percentage = (score / len(questions)) * 100

print("Percentage:", percentage, "%")

if percentage >= 80:
    print("Grade: Excellent")
elif percentage >= 60:
    print("Grade: Good")
elif percentage >= 40:
    print("Grade: Average")
else:
    print("Grade: Needs Improvement")

print("\nThank you for participating!")
