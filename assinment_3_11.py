state_capitals = {
    'what is capital of Gujarat': 'Gandhinagar',
    'what is the capital of Maharashtra': 'Mumbai',
    'what is the capital of Rajasthan': 'Jaipur',
    'what is the capital of Karnataka': 'Bangalore',
    'what is the capital of Tamil Nadu': 'Chennai'
}
point = 0
for key, value in state_capitals.items():
    print(key)
    ans = input("Enter your answer: ")
    if (ans.lower() == value.lower()):
        print("Correct answer")
        point += 1
    else:
        print("Wrong answer")