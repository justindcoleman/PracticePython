completionState = False
userList = []
palindromeCheck = []
while completionState is not True:
    userAnswer = raw_input('Please enter a word: ')
    if userAnswer.isalpha():
        print('okay it\'s working so far')
    else:
        userAnswer = raw_input('Please enter a word this time: ')