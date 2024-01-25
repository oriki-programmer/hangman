def hangman():
    import random
    x = random.randint(0,15)
    problemlist = ["banana","strawberry","orange","python","feel","happy","sadness","purify","play","like","great","programmer","language","available","peace","firefox"]
    word = problemlist[x]
    wrong = 0
    stages = ["______      ",
              "|           ",
              "|     |     ",
              "|     0     ",
              "|    /||    ",
              "|    //     ",
              "|           "
              ]
    rletters=list(word)
    board = ["_"] * len(word)
    win=False
    print("ハングマンへようこそ！！")
    while wrong < len(stages) :
        print("\n")
        msg = "一文字を予想してね(全て半角英数字で入力してください)"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else :

            wrong += 1
        print(" ".join(board))
        print("\n".join(stages[0:wrong]))
        if "_" not in board:
            print("あなたの勝ち！！")
            print(" ".join(board))
            win= True
            break
    if not win :
        print("\n".join(stages[0:wrong]))
        print("あなたの負け！！正解は {}".format(word))

hangman()
