def minion_game(s):
    vowels='AEIOU'
    kevin_score = 0
    stuart_score = 0
    for i in range(len(s)):
        if s[i] not in vowels:
            stuart_score += (len(s) - i)
        else:
            kevin_score += (len(s) - i)
    if (stuart_score > kevin_score):
        print('Stuart', stuart_score)
    elif (kevin_score > stuart_score):
        print('Kevin', kevin_score)
    else:   
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)
