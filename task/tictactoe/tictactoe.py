first_input = "         "

main_list = [[first_input[0], first_input[1], first_input[2]],
             [first_input[3], first_input[4], first_input[5]],
             [first_input[6], first_input[7], first_input[8]]]

winning_option = []
order, x, y = 0, 0, 0


def main():
    global main_list
    print(f"""---------
| {main_list[0][0]} {main_list[0][1]} {main_list[0][2]} |
| {main_list[1][0]} {main_list[1][1]} {main_list[1][2]} |
| {main_list[2][0]} {main_list[2][1]} {main_list[2][2]} |
---------
    """)


def interactive():
    global main_list, x, y
    try:
        x, y = [int(number) for number in input("Enter the coordinates: ").split()]
    except ValueError:
        print("You should enter numbers!")
        interactive()
    finally:
        global order
        if x > 3 or y > 3:
            print("Coordinates should be from 1 to 3!")
            interactive()
        elif main_list[x - 1][y - 1] == " " and order % 2 == 0:
            main_list[x - 1][y - 1] = "X"
            order = order + 1
        elif main_list[x - 1][y - 1] == " " and order % 2 != 0:
            main_list[x - 1][y - 1] = "O"
            order = order + 1
        else:
            print("This cell is occupied! Choose another one!")
    pass


def update_list():
    global winning_option
    winning_option = [(main_list[0][0] + main_list[0][1] + main_list[0][2]),
                      (main_list[1][0] + main_list[1][1] + main_list[1][2]),
                      (main_list[2][0] + main_list[2][1] + main_list[2][2]),
                      (main_list[0][0] + main_list[1][0] + main_list[2][0]),
                      (main_list[0][1] + main_list[1][1] + main_list[2][1]),
                      (main_list[0][2] + main_list[1][2] + main_list[2][2]),
                      (main_list[0][0] + main_list[1][1] + main_list[2][2]),
                      (main_list[0][2] + main_list[1][1] + main_list[2][0])]


while True:
    main()
    interactive()
    update_list()
    if any(word == "XXX" for word in winning_option):
        main()
        print("X wins")
        break
    elif any(word == "OOO" for word in winning_option):
        main()
        print("O wins")
        break
    if order > 1:
        if sum(space.count(" ") for space in main_list) == 0:
            main()
            print("Draw")
            break
