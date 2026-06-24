questions =("how many elements are in periodic table?",
            "what is co2?",
            "what is earth?"
            )

options=(("A. 116", "B. 117", "C. 118", "D. 119"),("A. Carbon Dioxide","B.Water", "C. Nitrogen", "D. Cat"),("A. Planet", "B. Star", "C. Satellite", "D. None of the above"))

answers=("C", "A", "A")

guesses=[]

score=0
question_num=0

for question in questions:
    print("-----------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    

    guess=input("Enter your option: ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score+=1
        print("Correct!!")
    else:
        print("Incorrect")
        print(f"{answers[question_num]} is the correct answer!")
    question_num+=1

print("Your score is", score )

