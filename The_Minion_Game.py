def minion_game(string):
    # your code goes here
    lms=len(string)
    lst=['A','E','I','O','U']
    stuart=0
    kevin=0
    for i in range(0,lms):
        if(string[i] in lst):
            kevin+=lms-i
        else:
            stuart+=lms-i
    if(kevin>stuart):
        print("Kevin",kevin)
    elif(kevin<stuart):
        print("Stuart",stuart)
    else:
        print("Draw")


s=raw_input()
minion_game(s)
