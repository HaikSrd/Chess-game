import pygame
import config

pygame.mixer.init()

white_pawn = pygame.image.load("PATH_TO_CHESS_PIECES")
white_pawn = pygame.transform.smoothscale(white_pawn,(config.screen_size[1]/8,config.screen_size[1]/8))

black_pawn = pygame.image.load("PATH_TO_CHESS_PIECES")
black_pawn = pygame.transform.smoothscale(black_pawn,(config.screen_size[1]/8,config.screen_size[1]/8))

white_rook = pygame.image.load("PATH_TO_CHESS_PIECES")
white_rook = pygame.transform.smoothscale(white_rook,(config.screen_size[1]/8,config.screen_size[1]/8))

black_rook = pygame.image.load("PATH_TO_CHESS_PIECES")
black_rook = pygame.transform.smoothscale(black_rook,(config.screen_size[1]/8,config.screen_size[1]/8))

white_bishop = pygame.image.load("PATH_TO_CHESS_PIECES")
white_bishop = pygame.transform.smoothscale(white_bishop,(config.screen_size[1]/8,config.screen_size[1]/8))

black_bishop = pygame.image.load("PATH_TO_CHESS_PIECES")
black_bishop = pygame.transform.smoothscale(black_bishop,(config.screen_size[1]/8,config.screen_size[1]/8))

white_king = pygame.image.load("PATH_TO_CHESS_PIECES")
white_king = pygame.transform.smoothscale(white_king,(config.screen_size[1]/8,config.screen_size[1]/8))

black_king = pygame.image.load("PATH_TO_CHESS_PIECES")
black_king = pygame.transform.smoothscale(black_king,(config.screen_size[1]/8,config.screen_size[1]/8))

white_queen = pygame.image.load("PATH_TO_CHESS_PIECES")
white_queen = pygame.transform.smoothscale(white_queen,(config.screen_size[1]/8,config.screen_size[1]/8))

black_queen = pygame.image.load("PATH_TO_CHESS_PIECES")
black_queen = pygame.transform.smoothscale(black_queen,(config.screen_size[1]/8,config.screen_size[1]/8))

white_knight = pygame.image.load("PATH_TO_CHESS_PIECES")
white_knight = pygame.transform.smoothscale(white_knight,(config.screen_size[1]/8,config.screen_size[1]/8))

black_knight = pygame.image.load("PATH_TO_CHESS_PIECES")
black_knight = pygame.transform.smoothscale(black_knight,(config.screen_size[1]/8,config.screen_size[1]/8))

move_sound = pygame.mixer.Sound("PATH_TO_MOVE_AUDIO")
capture_sound = pygame.mixer.Sound("PATH_TO_CAPTURE_AUDIO")

def background(screen):
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                pygame.draw.rect(screen,config.white_color,[config.x_border + config.screen_size[1]*i/8, config.screen_size[1]*j/8, config.screen_size[1]/8,config.screen_size[1]/8])
            else:
                pygame.draw.rect(screen, config.dark_color, [config.x_border + config.screen_size[1]*i/8, config.screen_size[1]*j/8, config.screen_size[1]/8,config.screen_size[1]/8])
    #tf do these do???
    pygame.draw.rect(screen,(0,0,0), [config.x_border - 4, 0, 4,config.screen_size[1]])
    pygame.draw.rect(screen, (64, 237, 162),[0, 0, ((config.screen_size[0] - config.screen_size[1]) / 2) - 4, config.screen_size[1]])
    pygame.draw.rect(screen, (0,0,0), [config.x_border + config.screen_size[1], 0, 4, config.screen_size[1]])
    pygame.draw.rect(screen, (64, 237, 162),[(config.screen_size[1] + config.screen_size[0])/2 + 4, 0, ((config.screen_size[0] - config.screen_size[1]) / 2) - 4, config.screen_size[1]])

pieces_cords = [[8,10, 9, 12, 11, 9, 10, 8], [7, 7, 7, 7,7 , 7, 7, 7], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0,0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1], [2, 4, 3, 6, 5, 3, 4, 2]]

"""
nothing = 0
white pawn = 1
white rook = 2
white bishop = 3
white knight = 4
white king = 5
white queen = 6

black pawn = 7
black rook = 8
black bishop = 9
black knight = 10
black king = 11
black queen = 12
"""
piece_dict = {
    1 : white_pawn,
    2 : white_rook,
    3 : white_bishop,
    4 : white_knight,
    5 : white_king,
    6 : white_queen,
    7 : black_pawn,
    8 :black_rook,
    9 : black_bishop,
    10 : black_knight,
    11 : black_king,
    12 :black_queen
}
change_bg = False
whites = [1,2,3,4,5,6]
blacks = [7,8,9,10,11,12]
turn = "White"
#config.x_border + config.screen_size[1]*i/8, config.screen_size[1]*j/8, config.screen_size[1]/8,config.screen_size[1]/8]









captures_white = []
captures_black = []

class pieces:

    def check(pieces_cords):
        for i in range(8):
            for j in range(8):
                if pieces_cords[j][i] in whites and turn == "White":
                    list_of_moves = pieces.possible_next_moves_check(pieces_cords[j][i],[i,j])
                    for k in list_of_moves:
                        if pieces_cords[k[1]][k[0]] == 11:
                            return True
                elif pieces_cords[j][i] in blacks and turn == "Black":
                    list_of_moves = pieces.possible_next_moves_check(pieces_cords[j][i],[i,j])
                    for k in list_of_moves:
                        if pieces_cords[k[1]][k[0]] == 5:
                            return True
        return False

    def horse(cords):

        list_of_moves = [[cords[0],cords[1]],[cords[0]+1, cords[1] + 2],[cords[0]+1, cords[1] - 2],[cords[0]-1, cords[1] + 2],[cords[0]-1, cords[1] - 2]
               ,[cords[0] + 2,cords[1] + 1], [cords[0] + 2,cords[1] - 1],[cords[0] - 2,cords[1] + 1], [cords[0] - 2,cords[1] - 1]]
        list_of_moves.remove(cords)
        new_list = []
        for i in list_of_moves :
            if i[0] >= 0 and i[1] >= 0 and i[0] <= 7 and i[1] <= 7:
                if turn == "White" and (pieces_cords[i[1]][i[0]] in blacks or pieces_cords[i[1]][i[0]] == 0):
                    new_list.append(i)
                if turn == "Black" and (pieces_cords[i[1]][i[0]] in whites or pieces_cords[i[1]][i[0]] == 0):
                    new_list.append(i)
        list_of_moves = new_list
        return list_of_moves

    def bishop(cords):
        list_of_moves = []
        for i in range(0,8):
            list_of_moves.append([cords[0]+i,cords[1]+i])
            list_of_moves.append([cords[0] + i, cords[1] - i])
            list_of_moves.append([cords[0] - i, cords[1] + i])
            list_of_moves.append([cords[0] - i, cords[1] - i])

        k = list(map(tuple, list_of_moves))
        list_of_moves = list(dict.fromkeys(k))
        list_of_moves = sorted([list(t) for t in list_of_moves])
        list_of_moves.remove(cords)

        new_list = []
        for i in range(len(list_of_moves)):
            if list_of_moves[i][0] <= 7 and list_of_moves[i][1] <= 7 and list_of_moves[i][0] >= 0 and list_of_moves[i][1] >= 0:
                new_list.append(list_of_moves[i])
        list_of_moves = new_list

        pieces.remove_impossible_moves_diag(pieces_cords,list_of_moves,cords)
        return list_of_moves

    def queen(cords):
        list_of_moves_xy = [[cords[0], 0], [0, cords[1]]]
        list_of_moves_diag = []
        for i in range(0, 8):
            list_of_moves_xy.append([cords[0], i])
            list_of_moves_xy.append([cords[0], - i])
            list_of_moves_xy.append([i, cords[1]])
            list_of_moves_xy.append([- i, cords[1]])
            list_of_moves_diag.append([cords[0] + i, cords[1] + i])
            list_of_moves_diag.append([cords[0] + i, cords[1] - i])
            list_of_moves_diag.append([cords[0] - i, cords[1] + i])
            list_of_moves_diag.append([cords[0] - i, cords[1] - i])

        # removing duplicates
        k = list(map(tuple, list_of_moves_xy))
        list_of_moves_xy = list(dict.fromkeys(k))
        list_of_moves_xy = sorted([list(t) for t in list_of_moves_xy])

        k = list(map(tuple, list_of_moves_diag))
        list_of_moves_diag = list(dict.fromkeys(k))
        list_of_moves_diag = sorted([list(t) for t in list_of_moves_diag])
        list_of_moves_xy.remove(cords)

        new_list = []
        for i in range(len(list_of_moves_xy)):
            if list_of_moves_xy[i][0] <= 7 and list_of_moves_xy[i][1] <= 7 and list_of_moves_xy[i][0] >= 0 and list_of_moves_xy[i][1] >= 0:
                new_list.append(list_of_moves_xy[i])

        list_of_moves_xy = new_list

        new_list = []
        for i in range(len(list_of_moves_diag)):
            if list_of_moves_diag[i][0] <= 7 and list_of_moves_diag[i][1] <= 7 and list_of_moves_diag[i][0] >= 0 and list_of_moves_diag[i][1] >= 0:
                new_list.append(list_of_moves_diag[i])

        list_of_moves_diag = new_list
        list_of_moves_diag.remove(cords)

        pieces.remove_impossible_moves_xy(pieces_cords,list_of_moves_xy,cords)
        pieces.remove_impossible_moves_diag(pieces_cords, list_of_moves_diag, cords)

        list_of_moves = list_of_moves_xy + list_of_moves_diag
        return list_of_moves

    def rook(cords):
        list_of_moves = [[cords[0], 0],[ 0, cords[1]]]
        for i in range(0, 8):
            list_of_moves.append([cords[0], i])
            list_of_moves.append([cords[0], - i])
            list_of_moves.append([ i, cords[1]])
            list_of_moves.append([ - i, cords[1]])
        for i in list_of_moves:
            if i[0] <= -1 or i[1] <= -1 or i[0] >= 8 or i[1] >= 8:
                list_of_moves.remove(i)
        #removing duplicates
        k = list(map(tuple, list_of_moves))
        list_of_moves = list(dict.fromkeys(k))
        list_of_moves = sorted([list(t) for t in list_of_moves])
        list_of_moves.remove(cords)

        pieces.remove_impossible_moves_xy(pieces_cords,list_of_moves,cords)
        return list_of_moves

    def king(cords):
        list_of_moves = [[cords[0] + 1, cords[1]],[cords[0] - 1, cords[1]],[cords[0], cords[1] + 1],[cords[0], cords[1] - 1],
                         [cords[0] + 1, cords[1]+1],[cords[0] + 1, cords[1]-1],[cords[0]-1, cords[1] + 1],[cords[0]-1, cords[1] - 1]]

        new_list = []
        for i in list_of_moves:
            if i[0] <= 7 and i[1] <= 7 and i[0] >= 0 and i[1] >= 0:
                new_list.append(i)
        list_of_moves = new_list

        new_list = []

        for i in list_of_moves:
            if turn == "White" and pieces_cords[i[1]][i[0]] not in whites:
                new_list.append(i)
            elif turn == "Black" and pieces_cords[i[1]][i[0]] not in blacks:
                new_list.append(i)
        list_of_moves = new_list


        return list_of_moves

    def remove_impossible_moves_xy(position, list_of_moves, cords):

        #calculating the position of first pieces on the top and bottom of the piece, if there is no piece it should not remove any of them
        list_of_pieces_y_top = []
        list_of_pieces_y_bottom = []
        for i in range(8):
            if position[i][cords[0]] != 0 and cords[1]!= i:
                if i < cords[1]:
                    list_of_pieces_y_top.append(i)
                if i > cords[1]:
                    list_of_pieces_y_bottom.append(i)

        if len(list_of_pieces_y_top) != 0:
            if (turn == "White" and position[max(list_of_pieces_y_top)][cords[0]] in blacks) or (turn == "Black" and position[max(list_of_pieces_y_top)][cords[0]] in whites):
                top_adder = [cords[0], max(list_of_pieces_y_top)]

            for i in range(max(list_of_pieces_y_top) + 1):
                for j in list_of_moves:
                    if j[1] == i:
                        try:
                            list_of_moves.remove(j)
                        except:
                            pass
        if len(list_of_pieces_y_bottom) != 0:
            if (turn == "White" and position[min(list_of_pieces_y_bottom)][cords[0]] in blacks) or (turn == "Black" and position[min(list_of_pieces_y_bottom)][cords[0]] in whites):
                bottom_adder = [cords[0], min(list_of_pieces_y_bottom)]
            for i in range(min(list_of_pieces_y_bottom), 8):
                for j in list_of_moves:
                    if j[1] == i:
                        try:
                            list_of_moves.remove(j)
                        except:
                            pass
        try:
            list_of_moves.append(top_adder)
        except:
            pass
        try:
            list_of_moves.append(bottom_adder)
        except:
            pass


        #right and left
        list_of_pieces_y_left = []
        list_of_pieces_y_right = []
        #this works, dont touch it
        for i in range(8):
            if position[cords[1]][i] != 0 and cords[0] != i:
                if i < cords[0]:
                    list_of_pieces_y_left.append(i)
                if i > cords[0]:
                    list_of_pieces_y_right.append(i)

        if len(list_of_pieces_y_left) != 0:
            if (turn == "White" and position[cords[1]][max(list_of_pieces_y_left)] in blacks) or (
                    turn == "Black" and position[cords[1]][max(list_of_pieces_y_left)] in whites):
                left_adder = [max(list_of_pieces_y_left), cords[1]]

            for i in range(max(list_of_pieces_y_left) + 1):
                for j in list_of_moves:
                    if j[0] == i:
                        try:
                            list_of_moves.remove(j)
                        except:
                            pass
        if len(list_of_pieces_y_right) != 0:
            if (turn == "White" and position[cords[1]][min(list_of_pieces_y_right)] in blacks) or (
                    turn == "Black" and position[cords[1]][min(list_of_pieces_y_right)] in whites):
                right_adder = [min(list_of_pieces_y_right),cords[1]]
            for i in range(min(list_of_pieces_y_right), 8):
                for j in list_of_moves:
                    if j[0] == i:
                        try:
                            list_of_moves.remove(j)
                        except:
                            pass
        try:
            list_of_moves.append(left_adder)
        except:
            pass
        try:
            list_of_moves.append(right_adder)
        except:
            pass

        return list_of_moves

    def remove_impossible_moves_diag(position, list_of_moves, cords):
        list_of_pieces_y_topright = []
        list_of_pieces_y_topleft = []
        list_of_pieces_y_bottomright = []
        list_of_pieces_y_bottomleft = []

        #top right positions
        for i in range(8):
            if [cords[0] + i, cords[1] - i] in list_of_moves and position[cords[1] - i][cords[0] + i] != 0:

                list_of_pieces_y_topright.append([cords[0] + i, cords[1] - i])
        if len(list_of_pieces_y_topright) != 0:
            limit = list_of_pieces_y_topright[0]
            if turn == "White" and position[limit[1]][limit[0]] in whites or turn == "Black" and position[limit[1]][limit[0]] in blacks:
                for i in range(8):
                    try:
                        list_of_moves.remove([limit[0] + i, limit[1] -i])
                    except:
                        pass
            elif turn == "White" and position[limit[1]][limit[0]] in blacks or turn == "Black" and position[limit[1]][limit[0]] in whites:
                for i in range(1,8):
                    try:
                        list_of_moves.remove([limit[0] + i, limit[1] -i])
                    except:
                        pass



        # top left positions
        for i in range(8):
            if [cords[0] - i, cords[1] - i] in list_of_moves and position[cords[1] - i][cords[0] - i] != 0:
                list_of_pieces_y_topleft.append([cords[0] - i, cords[1] - i])
        if len(list_of_pieces_y_topleft) != 0:
            limit = list_of_pieces_y_topleft[0]
            if turn == "White" and position[limit[1]][limit[0]] in whites or turn == "Black" and position[limit[1]][
                limit[0]] in blacks:
                for i in range(8):
                    try:
                        list_of_moves.remove([limit[0] - i, limit[1] - i])
                    except:
                        pass
            elif turn == "White" and position[limit[1]][limit[0]] in blacks or turn == "Black" and position[limit[1]][
                limit[0]] in whites:
                for i in range(1, 8):
                    try:
                        list_of_moves.remove([limit[0] - i, limit[1] - i])
                    except:
                        pass

        # bottom right position
        for i in range(8):
            if [cords[0] + i, cords[1] + i] in list_of_moves and position[cords[1] + i][cords[0] + i] != 0:
                list_of_pieces_y_bottomright.append([cords[0] + i, cords[1] + i])
        if len(list_of_pieces_y_bottomright) != 0:
            limit = list_of_pieces_y_bottomright[0]
            if turn == "White" and position[limit[1]][limit[0]] in whites or turn == "Black" and position[limit[1]][
                limit[0]] in blacks:
                for i in range(8):
                    try:
                        list_of_moves.remove([limit[0] + i, limit[1] + i])
                    except:
                        pass
            elif turn == "White" and position[limit[1]][limit[0]] in blacks or turn == "Black" and position[limit[1]][
                limit[0]] in whites:
                for i in range(1, 8):
                    try:
                        list_of_moves.remove([limit[0] + i, limit[1] + i])
                    except:
                        pass

        # bottom left position
        for i in range(8):
            if [cords[0] - i, cords[1] + i] in list_of_moves and position[cords[1] + i][cords[0] - i] != 0:
                list_of_pieces_y_bottomleft.append([cords[0] - i, cords[1] + i])
        if len(list_of_pieces_y_bottomleft) != 0:
            limit = list_of_pieces_y_bottomleft[0]
            if turn == "White" and position[limit[1]][limit[0]] in whites or turn == "Black" and position[limit[1]][
                limit[0]] in blacks:
                for i in range(8):
                    try:
                        list_of_moves.remove([limit[0] - i, limit[1] + i])
                    except:
                        pass
            elif turn == "White" and position[limit[1]][limit[0]] in blacks or turn == "Black" and position[limit[1]][
                limit[0]] in whites:
                for i in range(1, 8):
                    try:
                        list_of_moves.remove([limit[0] - i, limit[1] + i])
                    except:
                        pass


        return list_of_moves

    def white_pawn(cords):
        list_of_moves = []
        if pieces_cords[cords[1] - 1][cords[0]] == 0:
            list_of_moves.append([cords[0], cords[1] - 1])
            if cords[1] == 6 and pieces_cords[cords[1] - 2][cords[0]] == 0:
                list_of_moves.append([cords[0], cords[1] - 2])
        if pieces_cords[cords[1] - 1][cords[0] - 1] != 0 and pieces_cords[cords[1] - 1][cords[0] - 1] in blacks:
            list_of_moves.append([cords[0] - 1, cords[1] - 1])
        if cords[0] != 7 and pieces_cords[cords[1] - 1][cords[0] + 1] != 0 and pieces_cords[cords[1] - 1][cords[0] + 1] in blacks:
                list_of_moves.append([cords[0] + 1, cords[1] - 1])

        return list_of_moves

    def black_pawn(cords):
        list_of_moves = []
        if pieces_cords[cords[1] + 1][cords[0]] == 0:
            list_of_moves.append([cords[0], cords[1] + 1])
            if cords[1] == 1 and pieces_cords[cords[1] + 2][cords[0]] == 0:
                list_of_moves.append([cords[0], cords[1] + 2])
        if pieces_cords[cords[1] + 1][cords[0] - 1] != 0 and pieces_cords[cords[1] + 1][cords[0] - 1] in whites:
            list_of_moves.append([cords[0] - 1, cords[1] + 1])
        if cords[0] != 7 and pieces_cords[cords[1] + 1][cords[0] + 1] != 0 and pieces_cords[cords[1] + 1][cords[0] + 1] in whites:
            list_of_moves.append([cords[0] + 1, cords[1] + 1])
        return list_of_moves

    def possible_next_moves(piece, cords):
        if piece == 4 and turn == "White":
            return pieces.horse(pieces.mouse_square(cords))
        elif piece == 10 and turn == "Black":
            return pieces.horse(pieces.mouse_square(cords))
        elif piece == 3 and turn == "White":
            return pieces.bishop(pieces.mouse_square(cords))
        elif piece == 9 and turn == "Black":
            return pieces.bishop(pieces.mouse_square(cords))
        elif piece == 6 and turn == "White":
            return pieces.queen(pieces.mouse_square(cords))
        elif piece == 12 and turn == "Black":
            return pieces.queen(pieces.mouse_square(cords))
        elif piece == 2 and turn == "White":
            return pieces.rook(pieces.mouse_square(cords))
        elif piece == 8 and turn == "Black":
            return pieces.rook(pieces.mouse_square(cords))
        elif piece == 5 and turn == "White":
            return pieces.king(pieces.mouse_square(cords))
        elif piece == 11 and turn == "Black":
            return pieces.king(pieces.mouse_square(cords))
        elif piece == 1 and turn == "White":
            return pieces.white_pawn(pieces.mouse_square(cords))
        elif piece == 7 and turn == "Black":
            return pieces.black_pawn(pieces.mouse_square(cords))
        return 0

    def possible_next_moves_check(piece, cords):
        if piece == 4 and turn == "White":
            return pieces.horse(cords)
        elif piece == 10 and turn == "Black":
            return pieces.horse(cords)
        elif piece == 3 and turn == "White":
            return pieces.bishop(cords)
        elif piece == 9 and turn == "Black":
            return pieces.bishop(cords)
        elif piece == 6 and turn == "White":
            return pieces.queen(cords)
        elif piece == 12 and turn == "Black":
            return pieces.queen(cords)
        elif piece == 2 and turn == "White":
            return pieces.rook(cords)
        elif piece == 8 and turn == "Black":
            return pieces.rook(cords)
        elif piece == 5 and turn == "White":
            return pieces.king(cords)
        elif piece == 11 and turn == "Black":
            return pieces.king(cords)
        elif piece == 1 and turn == "White":
            return pieces.white_pawn(cords)
        elif piece == 7 and turn == "Black":
            return pieces.black_pawn(cords)
        return 0

    # def possible_next_moves_check(piece, cords):
    #     if piece == 4 and turn == "White":
    #         return pieces.horse(cords)
    #     elif piece == 10 and turn == "Black":
    #         return pieces.horse(cords)
    #     elif piece == 3 and turn == "White":
    #         return pieces.bishop(cords)
    #     elif piece == 9 and turn == "Black":
    #         return pieces.bishop(cords)
    #     elif piece == 6:
    #         return pieces.queen(cords)
    #     elif piece == 12 and turn == "Black":
    #         return pieces.queen(cords)
    #     elif piece == 2 and turn == "White":
    #         return pieces.rook(cords)
    #     elif piece == 8 and turn == "Black":
    #         return pieces.rook(cords)
    #     elif piece == 5 and turn == "White":
    #         return pieces.king(cords)
    #     elif piece == 11 and turn == "Black":
    #         return pieces.king(cords)
    #     elif piece == 1 and turn == "White":
    #         return pieces.white_pawn(cords)
    #     elif piece == 7 and turn == "Black":
    #         return pieces.black_pawn(cords)
    #     return 0

    #takes coordinates where we clicked and gives us the square
    def mouse_square(mouse):
        for i in range(8):
            for j in range(8):
                if config.x_border + config.screen_size[1]*i/8 < mouse[0] <= config.x_border + config.screen_size[1]*(i+1)/8 and config.screen_size[1]*j/8 < mouse[1] <= config.screen_size[1]*(j+1)/8:
                    return [i,j]

    #tells us if a move is possible....
    def possible_move(piece, mouse1, mouse2):
        if piece == 4 or piece == 10:
            for i in pieces.horse(pieces.mouse_square(mouse1)):
                if pieces.mouse_square(mouse2) == i:
                    return True
            return False
        elif piece == 3 or piece == 9:
            for i in pieces.bishop(pieces.mouse_square(mouse1)):
                if pieces.mouse_square(mouse2) == i:
                    return True
            return False
        elif piece == 6 or piece == 12:
            for i in pieces.queen(pieces.mouse_square(mouse1)):
                if pieces.mouse_square(mouse2) == i:
                    return True
            return False
        elif piece == 2 or piece == 8:
            for i in pieces.rook(pieces.mouse_square(mouse1)):
                if pieces.mouse_square(mouse2) == i:
                    return True
            return False
        elif piece == 5 or piece == 11:
            for i in pieces.king(pieces.mouse_square(mouse1)):
                if pieces.mouse_square(mouse2) == i:
                    return True
            return False
        elif piece == 1:
            for i in pieces.white_pawn(pieces.mouse_square(mouse1)):
                if pieces.mouse_square(mouse2) == i:
                    return True
            return False
        elif piece == 7:
            for i in pieces.black_pawn(pieces.mouse_square(mouse1)):
                if pieces.mouse_square(mouse2) == i:
                    return True
            return False
        return False

    #takes the piece list and puts the pieces on the board
    def position(screen, mouses,clicked):
        global change_bg
        global turn
        #takes the last two inputs and puts the piece where we want it
        global pieces_cords
        global captures_white
        global captures_black
        global check_counter
        if len(mouses) % 2 == 0 and len(mouses) != 0 and clicked:
            start = pieces.mouse_square(mouses[-2])
            end = pieces.mouse_square(mouses[-1])
            if pieces.possible_move(pieces_cords[start[1]][start[0]],mouses[-2],mouses[-1]):

                if turn == "White" and pieces_cords[end[1]][end[0]] in blacks:
                    captures_white.append(pieces_cords[end[1]][end[0]])
                    captures_white = sorted(captures_white)
                    pygame.mixer.Sound.play(capture_sound)
                elif turn == "Black" and pieces_cords[end[1]][end[0]] in whites:
                    captures_black.append(pieces_cords[end[1]][end[0]])
                    captures_black = sorted(captures_black)
                    pygame.mixer.Sound.play(capture_sound)
                else:
                    pygame.mixer.Sound.play(move_sound)
                pieces_cords[end[1]][end[0]] = pieces_cords[start[1]][start[0]]
                pieces_cords[start[1]][start[0]] = 0
                condition = False
                change_bg = False

                if turn == "White":

                    turn = "Black"
                else:
                    turn = "White"


        elif clicked or change_bg:
            try:
                piece = pieces_cords[pieces.mouse_square(mouses[-1])[1]][pieces.mouse_square(mouses[-1])[0]]
            except:
                piece = 0
            if piece != 0 and (pieces.possible_next_moves(piece,mouses[-1])) != 0:
                for i in pieces.possible_next_moves(piece,mouses[-1]):
                    #if statement here so outside the board doesnt change color
                    if i[0] >= 0 and i[1] >= 0 and i[0] <= 7 and i[1] <= 7:
                        if (i[0] + i[1]) % 2 == 0:
                            pygame.draw.rect(screen, config.light_possible_next_color,
                                             [config.x_border + config.screen_size[1] * i[0] / 8, config.screen_size[1] * i[1] / 8,
                                              config.screen_size[1] / 8, config.screen_size[1] / 8])
                        else:
                            pygame.draw.rect(screen, config.dark_possible_next_color,
                                             [config.x_border + config.screen_size[1] * i[0] / 8,
                                              config.screen_size[1] * i[1] / 8,
                                              config.screen_size[1] / 8, config.screen_size[1] / 8])
                change_bg = True
            else:
                mouses.pop(-1)

        for i in range(8):
            for j in range(8):
                if pieces_cords[i][j] == 0:
                    pass
                else:
                     screen.blit(piece_dict.get(pieces_cords[i][j]), (config.x_border + j*config.screen_size[1]/8, i*config.screen_size[1]/8))

        for i in range(len(captures_white)):
            k = i
            ysize = 7*config.screen_size[1]/8
            if i >= 16:
                k = i - 16
                ysize = 3 * config.screen_size[1] / 8
            elif i >= 12:
                k = i - 12
                ysize = 4 * config.screen_size[1] / 8
            elif i >= 8:
                k = i - 8
                ysize = 5 * config.screen_size[1] / 8
            elif i >= 4:
                k = i - 4
                ysize = 6 * config.screen_size[1] / 8
            screen.blit(piece_dict.get(captures_white[i]),[k*config.screen_size[0]/20 - 5,ysize])

        for i in range(len(captures_black)):
            k = i
            ysize = 0
            if i >= 16:
                k = i - 16
                ysize = 4 * config.screen_size[1] / 8
            elif i >= 12:
                k = i - 12
                ysize = 3 * config.screen_size[1] / 8
            elif i >= 8:
                k = i - 8
                ysize = 2 * config.screen_size[1] / 8
            elif i >= 4:
                k = i - 4
                ysize = 1 * config.screen_size[1] / 8
            screen.blit(piece_dict.get(captures_black[i]),[k*config.screen_size[0]/20 - 5,ysize])
