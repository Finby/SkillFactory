import random

DEBUG_LEVEL = 'FATAL'   # DEBUG, FATAL


def logging(message, debug_level=DEBUG_LEVEL):
    if debug_level == 'DEBUG':
        print(message)


FIELD_SIZE = 6
MAX_SHIP_LENGTH = 3
DIRECTIONS = {'L': (0, -1), 'R': (0, 1), 'D': (1, 0), 'U': (-1, 0)}


class Dot:
    def __init__(self, x, y):
        # dot represents cell coordinates and sign in this position
        self.x = x
        self.y = y

    def __eq__(self, dot_to_compare):
        return self.x == dot_to_compare.x and self.y == dot_to_compare.y

    def __repr__(self):
        return f"({self.x}, {self.y})"


class Ship:

    def __init__(self, start_pos_: Dot, len_: int, direction_: str):
        # direction_: L, R, U, D from DIRECTIONS
        self.start_pos = start_pos_
        self.direction = direction_
        # self.direction_1 = 'H' if direction_.upper() in ('L', 'R') else 'V'
        dx, dy = DIRECTIONS[direction_.upper()]
        self.life = len_
        self.__ship_coords = [(Dot(self.start_pos.x + dx * i, self.start_pos.y + dy * i)) for i in range(self.life)]

    def ship_is_alive(self):
        return self.life > 0

    def ship_is_shooten(self, dot_):
        self.life -= 1
        return dot_ in self.__ship_coords

    def dots(self):
        return self.__ship_coords

    def __repr__(self):
        return f"ship with start ({self.start_pos.x}, {self.start_pos.y}) and length {self.life}"


class BoardExceptions(Exception):
    pass


class ImpossibleShipPosition(BoardExceptions):
    def __init__(self, ship_: Ship):
        self.ship = ship_

    def __str__(self):
        return f"such ship can't be settled. {self.ship.start_pos} and len={self.ship.life}"


class AlreadyShot(BoardExceptions):
    def __str__(self):
        return f"You have shot this position."


class DotIsOutOfBoard(BoardExceptions):
    def __str__(self):
        return f"Both coordinates of dot must be in range 0-{FIELD_SIZE}"


class Board:
    EMPTY_CELL = 'O'
    SHOT_CELL = 'T'
    SHIP_ALIVE = '■'
    SHIP_HIT = 'X'
    SHIP_CONTOUR = '.'

    def __init__(self, hidden_=False, fs_=FIELD_SIZE):
        self.field_size = fs_
        self.hidden = hidden_
        empty_board = [[self.EMPTY_CELL] * self.field_size for _ in range(self.field_size)]
        self.board = empty_board.copy()
        self.board_ships = []       # to store player ships when 0 then lose
        self.busy_cells = []        # used to store busy cell while settling ships

    def add_ship(self, ship_):
        if not self.__ship_is_valid(ship_):
            raise ImpossibleShipPosition(ship_)
        else:
            self.__add_ship_on_board(ship_)
        return True

    def change_cell(self, coord: Dot, sign_):
        self.board[coord.x][coord.y] = sign_

    def get_empty_cells(self) -> list:
        # return list of board dots with value EMPTY_CELL
        empty_cells_list = []
        for i in range(self.field_size):
            for j in range(self.field_size):
                if self.board[i][j] == self.EMPTY_CELL:
                    empty_cells_list.append(Dot(i, j))
        return empty_cells_list

    def mark_ship_contour(self, ship_: Ship):
        dxy = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        for dot_ in ship_.dots():
            for dx, dy in dxy:
                temp_dot = Dot(dot_.x + dx, dot_.y + dy)
                if temp_dot not in self.busy_cells and not self.out_of_board(temp_dot):
                    self.change_cell(temp_dot, self.SHIP_CONTOUR)
                    # self.board[temp_dot.x][temp_dot.y] = self.SHIP_CONTOUR
                    self.busy_cells.append(temp_dot)

    def out_of_board(self, dot_):
        return not (0 <= dot_.x < self.field_size and 0 <= dot_.y < self.field_size)

    def print_board(self):
        if self.hidden:
            return None
        print(f' | {" ".join([str(i) for i in range(self.field_size)])}')
        print('-' * (self.field_size * 2 + 3))
        for i in range(self.field_size):
            print(f'{i}| {" ".join([self.board[i][k] for k in range(self.field_size)])}')
        print()

    def __add_ship_on_board(self, ship_: Ship):
        for d_ in ship_.dots():
            self.change_cell(d_, self.SHIP_ALIVE)
            self.busy_cells.append(d_)

        self.board_ships.append(ship_)
        # self.mark_ship_contour(ship_)
        # self.print_board()

    def __ship_is_valid(self, ship_to_check: Ship):
        for dot_ in ship_to_check.dots():
            logging(dot_)
            if self.out_of_board(dot_) or dot_ in self.busy_cells:
                return False
        return True


class Player:
    def __init__(self, name_=None, hidden_board=False):
        if name_ is not None:
            self.player_name = name_
        else:
            self.player_name = "Unknown_" + str(random.randint(range(200)))
        logging(f"Hello I'm player {self.player_name}")
        self.my_board = Board(hidden_=hidden_board)
        n_ = self.my_board.field_size
        self.left_cells_opp_board = [(x, y) for x in range(n_) for y in range(n_)]

        self.ships_left = {MAX_SHIP_LENGTH-i: 1+i for i in range(MAX_SHIP_LENGTH)}  # max_le=3 ship-> 3: 1, 2: 2 , 1: 3
        self.ship_locations = []
        self.put_ships_on_board()

        self.opponent_board = Board()

    def get_player_movement(self):
        raise NotImplementedError()

    def move(self):
        # 100 tries
        n = 100
        while True and n > 0:
            n -= 1
            try:
                dot_to_shot = self.get_player_movement()
            except DotIsOutOfBoard as e:
                print(e)
            except AlreadyShot as e:
                print(e)
            else:
                self.opponent_board.busy_cells.append(dot_to_shot)
                return dot_to_shot
        return None

    def put_ships_on_board(self):
        raise NotImplementedError()

    def process_opponent_move(self, coord: Dot):
        # None      - missed
        # Killed    - ship killed and removed from user list
        # Hil       - ship is hit but alive
        # self.my_board.busy_cells.append(Dot)
        for ship in self.my_board.board_ships:
            if coord in ship.dots() and self.my_board.board[coord.x][coord.y] == self.my_board.SHIP_ALIVE:
                ship.life -= 1
                self.my_board.board[coord.x][coord.y] = self.my_board.SHIP_HIT
                if ship.life == 0:
                    print(f"{ship} is killed")
                    self.my_board.board_ships.remove(ship)
                    return "killed"
                else:
                    return "hit"
        return None

    def update_opponent_board(self, dot_: Dot, hit=None):
        # update board that not to shot the same place
        # method get_empty_cells will return for game cell which were not shot
        # TODO: improve processing of killed and hit with marking surrounding cells - will improve AI level
        # human should control it by his self
        if hit is not None and hit.lower() in ("killed", "hit"):
            self.opponent_board.busy_cells.append(dot_)
            self.opponent_board.change_cell(dot_, self.opponent_board.SHIP_HIT)
        else:
            self.opponent_board.change_cell(dot_, self.opponent_board.SHOT_CELL)

    def is_there_ships(self):
        return len(self.my_board.board_ships) > 0

    def put_ships_on_board_random(self):
        # TODO: write random ship allocation
        # currently they are hardcoded ...
        ship_3_1 = Ship(Dot(0, 0), 3, 'R')
        ship_2_1 = Ship(Dot(2, 2), 2, 'D')
        ship_2_2 = Ship(Dot(4, 4), 2, 'U')
        ship_1_1 = Ship(Dot(5, 0), 1, 'U')
        ship_1_2 = Ship(Dot(0, 5), 1, 'U')
        ship_1_3 = Ship(Dot(3, 0), 1, 'U')

        for ship_ in (ship_3_1, ship_2_1, ship_2_2, ship_1_1, ship_1_2, ship_1_3):
            logging(ship_)
            logging(self.player_name)
            self.my_board.add_ship(ship_)

    def put_ships_on_board_input(self):
        # iterates self.ships_left and puts it on board
        # with logic to choose start position and direction for computer player - should be differentiate in children
        #
        for length, quantity in self.ships_left.items():
            for i in range(quantity):
                while True:
                    print("Your current board: ")
                    self.my_board.print_board()
                    x, y, d = input(f"Enter for {length}-length {i+1} \
                    ship start pos and direction (U, D, R, L). (Ex. 1 1 R): ").split()
                    x, y = int(x), int(y)
                    try:
                        if self.my_board.add_ship(Ship(start_pos_=Dot(x, y), len_=length, direction_=d)):
                            break
                    except ImpossibleShipPosition:
                        continue
        return None

    def print_player_state(self):
        print("-"*20)
        print(f"I'm {self.player_name}. My board")
        self.my_board.print_board()
        print("My opponent board ")
        self.opponent_board.print_board()
        print("-"*20)


class HumanPlayer(Player):
    def __init__(self, name_="Human"):
        super().__init__(name_)

    def put_ships_on_board(self):
        super().put_ships_on_board_random()
        # super().put_ships_on_board_input()

    def get_player_movement(self) -> Dot:
        while True:
            cords = input("your shot, enter (x, y) coordinate: ").split()
            if len(cords) != 2:
                print("should be 2 coordinates")
                continue
            x, y = cords
            if not (x.isdigit()) or not (y.isdigit()):
                print("Both coordinates must be digits")
                continue
            d_ = Dot(int(x), int(y))
            if self.opponent_board.out_of_board(d_):
                raise DotIsOutOfBoard
            if d_ not in self.opponent_board.get_empty_cells():
                raise AlreadyShot
            return d_


class ComputerPlayer(Player):
    def __init__(self, name_="Computer"):
        super().__init__(name_, hidden_board=True)
        # self.put_ships_on_board()

    def put_ships_on_board(self):
        super().put_ships_on_board_random()

    def get_player_movement(self) -> Dot:
        # d = Dot(random.randint(0,FIELD_SIZE-1), random.randint(0, FIELD_SIZE-1))
        empty_cells = self.opponent_board.get_empty_cells()
        d = random.choice(empty_cells)
        print(f"computer movement: {d}")
        return d


class SeaBattle:
    def __init__(self, p1=HumanPlayer(), p2=ComputerPlayer()):
        self.player_1 = p1
        self.player_2 = p2

    def play_game(self):
        players = [self.player_1, self.player_2]
        random.shuffle(players)
        current_player, next_player = players[0], players[1]
        while True:
            current_player.print_player_state()
            dot_to_shot = current_player.move()
            opponet_answer = next_player.process_opponent_move(dot_to_shot)
            current_player.update_opponent_board(dot_to_shot, hit=opponet_answer)  
            if opponet_answer is not None and next_player.is_there_ships():  # hit and opponent has alive ships
                print(f"!!! You {opponet_answer} ship. You have one more attempt !!!")
                continue
            elif next_player.is_there_ships():          # not hit and opponent has alive ships
                print("<<<---- You missed. Next Player turn ---->>>")
                current_player, next_player = next_player, current_player
            else:       # hit and opponent has not alive ships
                print(f"Player {current_player.player_name} WON !!!")
                return 0


game = SeaBattle(p1=HumanPlayer(name_='Human_Vasiya'), p2=ComputerPlayer(name_='Computer_Pety'))
game.play_game()
