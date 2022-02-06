SIGNS = ('X', '0')
FIELD_SIZE = 3
MAX_GAME_STEPS = FIELD_SIZE ** 2
INIT_FIELD = [['_'] * FIELD_SIZE for _ in range(FIELD_SIZE)]
PLAYERS = ['human', 'human']


def row_n(field_: list, n: int) -> list:
    return [field_[n][i] for i in range(len(field_[n]))]


def col_n(field_: list, n: int) -> list:
    return [field_[i][n] for i in range(len(field_))]


def main_diagonal(field_: list) -> list:
    return [field_[i][i] for i in range(len(field_))]


def anti_diagonal(field_: list) -> list:
    fl = len(field_)
    return [field_[i][fl-1 - i] for i in range(fl)]


def is_win(field_: list, sign_: str) -> bool:
    game_result = False
    winning_lines = [main_diagonal(field_), anti_diagonal(field_)]
    for i in range(FIELD_SIZE):
        winning_lines.append(row_n(field_, i))
        winning_lines.append(col_n(field_, i))
    winning_combination = [sign_] * FIELD_SIZE
    if winning_combination in winning_lines:
        game_result = True
    return game_result


def calculate_result(field_: list, sign_: str) -> tuple:
    is_win_ = is_win(field_, sign_)
    next_step_ = True
    result_message_ = ''
    if step >= MAX_GAME_STEPS and not is_win_:
        result_message_ = 'DRAW, friendship WON !!!'
        next_step_ = False
    elif is_win_:
        result_message_ = f'Congratulations "{sign_}" WON !!!'
        next_step_ = False
    return next_step_, result_message_


def do_step(field_: list, sign_: str, step_: int):
    # return function based on player type
    # human -> do_step_human
    # computer -> do_step_computer
    function_name = 'do_step_' + PLAYERS[(step_ - 1) % 2]
    return globals()[function_name](field_, sign_)


def do_step_computer(field_: list, sign_: str) -> list:
    # TODO: write computer player logic
    # currently computer resets all to his sign and wins
    print('!!! Computer cheats everything :))) !!!')
    return [[sign_] * FIELD_SIZE for _ in range(FIELD_SIZE)]


def do_step_human(field_: list, sign_: str) -> list:
    correct_step = False
    while not correct_step:
        print('Current field:')
        print_field(field_)
        x, y = map(int, input('Enter step coordinates in format "x y":').split())
        if x not in range(FIELD_SIZE) or y not in range(FIELD_SIZE):
            print('One of coordinated is out of range. Must be 0 or 1 or 2.')
        elif field_[x][y] == '_':
            field_[x][y] = sign_
            correct_step = True
            # print_field(field_)
        else:
            print('cell is already occupied, see filed')
    return field_


def print_field(field_: list) -> None:
    print(f' | {" ".join([str(i) for i in range(FIELD_SIZE)])}')
    print('-' * (FIELD_SIZE * 2 + 3))
    for i in range(FIELD_SIZE):
        print(f'{i}| {" ".join([field_[i][k] for k in range(FIELD_SIZE)])}')


def set_step_sign(step_: int) -> str:
    return SIGNS[(step_ - 1) % 2]


def next_step(step_: int) -> tuple:
    return step_ + 1, set_step_sign(step_ + 1)


step = 1
current_sign = set_step_sign(step)
field = INIT_FIELD
is_next_step = True
result_message = "Unknown. We haven't finished yet"
print('LET START GAME!!!')

while is_next_step:
    print(f'Step {step}')
    field = do_step(field, current_sign, step)
    is_next_step, result_message = calculate_result(field, current_sign)
    step, current_sign = next_step(step)

print_field(field)
print(result_message)
