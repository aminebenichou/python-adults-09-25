def draw_table():
    i=0
    while i<7:
        print(f" {cells[i]} | {cells[i+1]} | {cells[i+2]} ")
        print(f"___|___|___") if i<5 else print("")
        i += 3

def get_winner(limit, addon, incrm):
    k=0
    while k<limit:
        if cells[k]==cells[k+addon]==cells[k+(2*addon)]:
            print("You Win")
        k += incrm

cells = [1, 2, 3, 4, 5, 6, 7, 8, 9]
player = "X"
wins= [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]
running = True



while running:
    draw_table()
    i=0
    player_input = input("Enter a number between 1-9: ")
    while i<len(cells):
        if int(player_input) == cells[i]:
            cells[i]=player
        i += 1
    if player=="X":
        player="O"
    else:
        player="X"

    get_winner(7, 1, 3)
    get_winner(3, 3, 1)

    if (cells[0]==cells[4]==cells[8]) or (cells[2]==cells[4]==cells[6]) :
        print("You Win")

    # for win in wins:
    #     if cells[win[0]]==cells[win[1]]==cells[win[2]]:
    #         print("You win")
    #         running=False
        

   