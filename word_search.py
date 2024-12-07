
class WordSearch:
    # These arrays are used to get row and column
    # numbers of 8 neighboursof a given cell
    dd = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx != 0 or dy != 0:
                dd.append((dx, dy))
    def __init__(self, board, word):
        self.board = board
        self.word = word
        self.paths = []
        self.row = len(board)
        self.col = len(board[0])
        self.counter = 0
    def find_words(self):
        ans = 0
        for i in range(self.row):
            for j in range(self.col):
                for d in self.dd:
                    ans += self.has_xmas(i,j,d)
        return ans
    def find_words(self):
        ans = 0
        for i in range(self.row):
            for j in range(self.col):
                ans += self.has_x_cross_mas(i,j)
        return ans
    
    def has_xmas(self, i, j, d):
        dx, dy = d
        for k, x in enumerate(self.word):
            ii = i + k * dx
            jj = j + k * dy
            if not (0 <= ii < self.row and 0 <= jj < self.col):
                return False
            if self.board[ii][jj] != x:
                return False
        return True
    def has_x_cross_mas(self, i,j):
        if not (1 <= i < self.row - 1 and 1 <= j < self.col - 1):
            return False
        if self.board[i][j] != "A":
            return False

    # Check both diagonals
        diag_1 = f"{self.board[i-1][j-1]}{self.board[i+1][j+1]}"
        diag_2 = f"{self.board[i-1][j+1]}{self.board[i+1][j-1]}"

        return diag_1 in ["MS", "SM"] and diag_2 in ["MS", "SM"]
        
def main():
    string = '''MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX'''
    magic = []
    for data in string.splitlines():
        magic.append(list(data))
    
    word = "XMAS"
    ws = WordSearch(magic, word)
    print(ws.find_words())
    
if __name__ == "__main__":
    main()
    

        