def minion_game(string):
    # your code goes here
    s = list(string)
    vowels = ["A","I","U","E","O"]
    length_s = len(s)
    stuart = 0
    kevin = 0

    for i in range(length_s):
        if s[i] in vowels:
            kevin += length_s - i
        else:
            stuart += length_s - i
            
    if stuart > kevin:
        print("Stuart",sturt)
    elif kevin > stuart:
        print("Kevin",kevin)
    else:
        print("Draw")
