game = [[1,0,1],
        [1,1,0],
        [5,0,1]]
 
def game_board(game_map,player=0, row=0, column=0, just_display=False):
    try:
        print("   a  b  c")
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)

        return game_map

    except IndexError as e:
        print("Error: dod you input row/column as 0 1 or 2 ?", e)

    except Exception as e:
        print("Something is not right", e)

# game_board(game,just_display=True)
# game_board(game_board,player=1,row=4,column=1)


# determine winner


def win(current_game):
    for row in current_game:
      print(row)
      if row.count(row[0]) == len(row) and row[0] != 0:
        print("Winner")



def win_vertically(current_game):
    for col in range(len(current_game)):
        check = []

        for row in current_game:
            check.append(row[col])

        
        if check.count(check[0]) == len(check) and check[0] != 0:
            print(row)
            print("Winner!!")


# win_vertically(game)

def diagonal_winner(current_game):
    # diagonals = []
    # for ix in range(len(current_game)):
    #     print(ix)
    #     diagonals.append(current_game[ix][ix])
    #     print(diagonals)
        diags = []
        for col, row  in enumerate(reversed(range(len(current_game)))):
        # print(col,row)
            diags.append(current_game[row][col])
        print(diags)


win_vertically(game)