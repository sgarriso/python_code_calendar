class Player:
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    OBJECT = "#"
    PLAYER = "^"
    
    def __init__(self, board, direction = UP):
        self.x, self.y = self.find_player(board)
        self.column = len(board)
        self.row = len(board[0])
        self.direction = direction
        self.path = {}
        self.path[(self.x, self.y)] = ""
    def find_player(self, board:list[list:str]):
        for x_index, row in enumerate(board):
            for y_index, item in enumerate(row):
                if item == self.PLAYER:
                    return x_index, y_index
    def rotate(self):
        self.direction = self.direction + 1
        if self.direction == 4:
            self.direction = 0
    def rotate_check(self, board):
            return board[self.x][self.y] == self.OBJECT
    def board_check(self):
        return not (self.x >= self.column - 1  or self.x <= 0 or self.y >= self.row - 1 or self.y <= 0)
    def moving(self, board):
        while(self.board_check()):
            match self.direction:
                case self.UP:
                    self.x = self.x - 1
                    if self.rotate_check(board):
                        self.rotate()
                        self.x = self.x + 1 
                    else:
                        self.path[(self.x, self.y)] = ""
                case self.LEFT:
                    self.y = self.y - 1
                    if self.rotate_check(board):
                        self.rotate()
                        self.y = self.y + 1 
                    else:
                       self.path[(self.x, self.y)] = ""
                case self.DOWN:
                    self.x = self.x + 1
                    if self.rotate_check(board):
                        self.rotate()
                        self.x = self.x - 1 
                    else:
                        self.path[(self.x, self.y)] = ""
                case self.RIGHT:
                    self.y = self.y  + 1
                    if self.rotate_check(board):
                        self.rotate()
                        self.y = self.y - 1 
                    else:
                        self.path[(self.x, self.y)] = ""
                
def main():
    board = '''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...'''
    data = []
    for i in board.splitlines():
        data.append(list(i))








    player = Player(data)
    player.moving(data)
    print(player.x , player.y)
    print((len(player.path.keys())))