class chess_piece:
    def __init__(self, piece_type, row, column):
        self.color = 'w' if piece_type.isupper() else 'b'
        self.piece_type = piece_type.lower()
        self.position = [row,column]
        self.is_checking_king = False
        self.attacker = None
        self.is_protected = False
    
    def __str__(self):
        return self.piece_type

class empty_space:
    def __init__(self, row, column):
        self.position = [row, column]
        self.control = None
    def __str__(self):
        return '.'

def main():
    cases = int(input())

    for case in range(cases):
        # Uppercase letters represent white pieces
        # Lowercase letters represent black pieces
        # Periods represent blank spaces 
        input_board = [list(input()) for row in range(8)]

        # For each square on the board, Create an object with data
        board_reign = []
        for row_num, row in enumerate(input_board):
            new_row = []
            for square_num, square in enumerate(row):
                if square != '.':
                    square = chess_piece(square, row_num, square_num)
                else:
                    square = empty_space(row_num, square_num)
                new_row.append(square)
            board_reign.append(new_row)
        
        #For each piece on the baord, establish their reign (spaghetti time)
        for row in board_reign:
            for square in row:
                if type(square) is chess_piece:
                    calculating_reign = True
                    current_increase_index = 1
                    while calculating_reign:
                        if square.piece_type == 'r':
                            
                            right_pos = square.position[1] + current_increase_index
                            left_pos = square.position[1] - current_increase_index
                            up_pos = square.position[0] - current_increase_index
                            down_pos = square.position[0] + current_increase_index
                            
                            if right_pos < len(row):
                                next_square = board_reign[square.position[0]][right_pos]

                                if type(next_square) is empty_space and next_square.control == None:
                                    next_square.control = square.color
                                elif type(next_square) is empty_space and next_square.control != None:
                                    next_square.control = 'both'
                                elif type(next_square) is chess_piece and next_square.color != square.color:
                                    if next_square.piece_type == 'k':
                                        square.is_checking_king = True
                                    next_square.attacker = square
                                elif type(next_square) is chess_piece and next_square.color == square.color:
                                    next_square.is_protected = True
                            else:
                                right_pos = -1
                            
                            if left_pos > -1:
                                
                                next_square = board_reign[square.position[0]][left_pos]    

                                if type(next_square) is empty_space and next_square.control == None:
                                    next_square.control = square.color
                                elif type(next_square) is empty_space and next_square.control != None:
                                    next_square.control = 'both'
                                elif type(next_square) is chess_piece and next_square.color != square.color:
                                    if next_square.piece_type == 'k':
                                        square.is_checking_king = True
                                    next_square.attacker = square
                                elif type(next_square) is chess_piece and next_square.color == square.color:
                                    next_square.is_protected = True
                            else:
                                left_pos = -1
                            
                            if up_pos > -1:
                                next_square = board_reign[up_pos][square.position[1]]

                                if type(next_square) is empty_space and next_square.control == None:
                                    next_square.control = square.color
                                elif type(next_square) is empty_space and next_square.control != None:
                                    next_square.control = 'both'
                                elif type(next_square) is chess_piece and next_square.color != square.color:
                                    if next_square.piece_type == 'k':
                                        square.is_checking_king = True
                                    next_square.attacker = square
                                elif type(next_square) is chess_piece and next_square.color == square.color:
                                    next_square.is_protected = True
                            else:
                                up_pos = -1
                            
                            if down_pos < len(board_reign):
                                next_square = board_reign[down_pos][square.position[1]]

                                if type(next_square) is empty_space and next_square.control == None:
                                    next_square.control = square.color
                                elif type(next_square) is empty_space and next_square.control != None:
                                    next_square.control = 'both'
                                elif type(next_square) is chess_piece and next_square.color != square.color:
                                    if next_square.piece_type == 'k':
                                        square.is_checking_king = True
                                    next_square.attacker = square
                                elif type(next_square) is chess_piece and next_square.color == square.color:
                                    next_square.is_protected = True
                            else:
                                down_pos = -1
                                
                            if right_pos == -1 and left_pos == -1 and right_pos == -1 and down_pos == -1:
                                calculating_reign = False

                        elif square.piece_type == 'n':
                            break
                            pass
                        elif square.piece_type == 'p':
                            break
                            pass
                        elif square.piece_type == 'b':
                            break
                            pass
                        elif square.piece_type == 'q':
                            break
                            pass
                        elif square.piece_type == 'k':
                            break
                        current_increase_index += 1
        

        reign_board = []
        for row in board_reign:
            n_row = []
            for square in row:
                if type(square) is chess_piece:
                    n_row.append(square.attacker if square.attacker == None else square.attacker.color)
                elif type(square) is empty_space:
                    n_row.append(square.control)
            reign_board.append(n_row)
        for x in reign_board:
            print(x)
        
if __name__ == '__main__':
    main()