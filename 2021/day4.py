def solve(lines):
    draws = lines[0].split(",")
    boards = []
    board = []
    i = -1
    n = 0
    for line in lines[2:]:
        if line == "":
            boards.append(board)
            board = []
        else:
            board.append(list(filter(None, line.split(" "))))
    boards.append(board)
    return (lvl1(draws, boards), lvl2(draws, boards))


def get_score(board, draw):
    score = 0
    for row in board:
        for elem in filter(None, row):
            score += int(elem)
    return score * int(draw)


def check_board(board):
    for i, row in enumerate(board):
        col = [board[n][i] for n in range(len(board))]
        if any([all(map(lambda x: x is None, row)), all(map(lambda x: x is None, col))]):
            return True
    return False


def mark_boards(draw, boards):
    for board in boards:
        for i, row in enumerate(board):
            for j, elem in enumerate(row):
                if elem == draw:
                    board[i][j] = None


def winner(boards):
    for board in boards:
        if check_board(board):
            return board
    return None


def has_winner(boards):
    return winner(boards) is not None


def lvl1(draws, boards):
    for draw in draws:
        mark_boards(draw, boards)
        if has_winner(boards):
            return get_score(winner(boards), draw)
    return None


def lvl2(draws, boards):
    wins = []
    last_score = 0
    for draw in draws:
        mark_boards(draw, boards)
        for k, board in enumerate(boards):
            if check_board(board) and not k in wins:
                wins.append(k)
                last_score = get_score(board, draw)
    return last_score

