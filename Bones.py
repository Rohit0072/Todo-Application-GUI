import json

with open("question.json", 'r') as file:
    content = file.read()

data = json.loads(content)

score = 0
for question in data:
    print(question["question_text"])
    for index,alternative in enumerate(question["alternatives"]):
        print(index + 1, "_",alternative)
    user_choice = int(input("Enter your answer: "))
    question['user_choice'] = user_choice


for question in data:
    if question["user_choice"] == question["correct_answer"]:
        score = score + 1
        result = "Correct Answer"
    else:
        result = "Wrong Answer"
    message = f"{result} {index + 1} Your answer:{question['user_choice']}, Correct answer:{question['correct_answer']}"
    print(message)

print("Score: ", score, "/", len(data))
