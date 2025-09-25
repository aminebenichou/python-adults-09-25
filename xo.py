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
    print(f" {cells[0]} | {cells[1]} | {cells[2]} ")
    print("___|___|___")
    print(f" {cells[3]} | {cells[4]} | {cells[5]} ")
    print("___|___|___")
    print(f" {cells[6]} | {cells[7]} | {cells[8]} ")
    print("   |   |   ")
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

    # k=0
    # while k<7:
    #     if cells[k]==cells[k+1]==cells[k+2]:
    #         print("You Win")
    #     k += 3
    # k=0
    # while k<3:
    #     if cells[k]==cells[k+3]==cells[k+6]:
    #         print("You Win")
    #     k += 1

    # if (cells[0]==cells[4]==cells[8]) or (cells[2]==cells[4]==cells[6]) :
    #     print("You Win")

    for win in wins:
        if cells[win[0]]==cells[win[1]]==cells[win[2]]:
            print("You win")
            running=False
        

   