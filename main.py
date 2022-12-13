# a dictionary that stores questions and answers
# have a variable that tracks the score of a player
# loop through the dictionary using the key values pairs
# display each question to the user and allow them to answer
# tell them if they are right or wrong
# show the final result when quiz is completed

quiz = {
    "question1": {
        "question": "What is the capital of Japan?",
        "answer": "Tokyo"
    },
    "question2": {
        "question": "What is the capital of Kanagawa Prefecture?",
        "answer": "Yokohama"
    },
    "question3": {
        "question": "What is the capital of Tochigi Prefecture?",
        "answer": "Utsunomiya"
    },
    "question4": {
        "question": "What is the capital of Saitama Prefecture?",
        "answer": "Saitama"
    },
    "question5": {
        "question": "What is the capital of Okinawa Prefecture?",
        "answer": "Naha"
    },
    "question6": {
        "question": "What is the capital of Hokkaido Prefecture?",
        "answer": "Sapporo"
    },
    "question7": {
        "question": "What is the capital of Ibaraki Prefecture?",
        "answer": "Mito"
    },
    "question8": {
        "question": "What is the capital of Nagasaki Prefecture?",
        "answer": "Nagasaki"
    },
    "question9": {
        "question": "What is the capital of Iwate Prefecture?",
        "answer": "Morioka"
    },
    "question10": {
        "question": "What is the capital of Miyagi Prefecture?",
        "answer": "Sendai"
    },
    "question11": {
        "question": "What is the capital of Gunma Prefecture?",
        "answer": "Maebashi"
    },
    "question10": {
        "question": "What is the capital of Yamanashi Prefecture?",
        "answer": "Kofu"
    },
    "question11": {
        "question": "What is the capital of Ishikawa Prefecture?",
        "answer": "Kanazawa"
    },
    "question12": {
        "question": "What is the capital of Aichi Prefecture?",
        "answer": "Nagoya"
    },
    "question13": {
        "question": "What is the capital of Shiga Prefecture?",
        "answer": "Otsu"
    },
    "question14": {
        "question": "What is the capital of Hyogo Prefecture?",
        "answer": "Kobe"
    },
    "question15": {
        "question": "What is the capital of Shimane Prefecture?",
        "answer": "Matsue"
    },
    "question16": {
        "question": "What is the capital of Kagawa Prefecture?",
        "answer": "Takamatsu"
    },
    "question17": {
        "question": "What is the capital of Eihime Prefecture?",
        "answer": "Matsuyama"
    },
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer? ")

    if answer.lower() == value['answer'].lower():
        print('Correct')
        score = score + 1
        print("Your score is: " + str(score) + "/" + str(len(quiz)))
    else:
        print("Incorrect.")
        print("The answer is: " + value['answer'])
        print("Your score is: " + str(score) + "/" + str(len(quiz)))
