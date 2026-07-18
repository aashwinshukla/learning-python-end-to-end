secret_word = "animal"
guess = ""
move = 0
move_limit = 3
out_of_move = False

while guess != secret_word and not(out_of_move):
    if move<move_limit:
        
        guess = input("enter guess:")
        move += 1
    else :
        out_of_move = True
if out_of_move:
        print("out of move , you loose")
else:
    print("you win")
