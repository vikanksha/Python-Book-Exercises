# The Minion Game.
def minion_game(S):
    Kev = 0
    Stu = 0
    for w in range(len(S)):
        if S[w] in "AEIOU":
            Kev = Kev+len(S)-w
        else:
            Stu = Stu+len(S)-w
    
    if Kev> Stu:
        print("Kevin", Kev)
    elif Kev< Stu:
         print("Stuart", Stu)
    else:
        print("Draw")
minion_game("BANANA") 