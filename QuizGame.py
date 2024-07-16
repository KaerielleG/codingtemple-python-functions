#task1
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) London", "B) Paris", "C) Berlin", "D) Madrid"],
        "answer": "B"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["A) 3", "B) 4", "C) 5", "D) 6"],
        "answer": "B"
    },
    {
        "question": "What is the largest planet in our Solar System?",
        "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
        "answer": "C"
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["A) O2", "B) H2O", "C) CO2", "D) NaCl"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["A) Charles Dickens", "B) William Shakespeare", "C) Mark Twain", "D) Jane Austen"],
        "answer": "B"
    }
]

#task2
def quiz_user(questions):
    user_answers = []
    for index, question in enumerate(questions):
        print(f"Question {index + 1}: {question['question']}")
        for option in question['options']:
            print(option)
        answer = input("Please enter the letter of your answer: ").upper()
        user_answers.append(answer)
    return user_answers



#task3
def score_quiz(questions, user_answers):
    score = 0
    total_questions = len(questions)
    for question, user_answer in zip(questions, user_answers):
        if user_answer == question['answer']:
            score += 1
    return score, total_questions

def main():
    print("Welcome to the Quiz Game!")
    user_answers = quiz_user(quiz_questions)
    score, total_questions = score_quiz(quiz_questions, user_answers)
    print(f"\nYou scored {score} out of {total_questions}.")
    print(f"Your percentage score is {score / total_questions * 100:.2f}%")
    if score == total_questions:
        print("Excellent! You got all the questions right!")
    elif score >= total_questions * 0.75:
        print("Great job! You scored above 75%.")
    elif score >= total_questions * 0.5:
        print("Good effort! You scored above 50%.")
    else:
        print("Keep trying! Practice makes perfect.")

if __name__ == "__main__":
    main()