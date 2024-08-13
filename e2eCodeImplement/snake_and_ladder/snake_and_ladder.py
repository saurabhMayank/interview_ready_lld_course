import random


class PlayerModel:
    def __init__(self, name):
        self.name = name
        # signify player position & movement using grid number
        # easier to deal with in code
        self.position = 1

    def update_position(self, pos):
        self.pos = pos


    def update_name(self, name):
        self.name = name  


"""
Singleton Class Board
"""

class BoardSingelton:
    # class instance
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(BoardSingelton, cls).__new__(cls)
            # Additional initialization can be done here
        return cls._instance


    def __init__(self, board_size):
        if not hasattr(self, '_initialized'):
            # board will always be square size
            self.board_size = board_size

            # board_size -> 10 * 10, num_of_grids = 100
            self.total_grids = self.board_size * self.board_size
            # for snakes start_pos > end_pos
            # because when snake bites in game
            # player comes to lower position
            # start_pos is a grid number & end_pos is a grid number
            self.snake_pos_map = {} # key -> start_pos, val -> end_pos
            # for ladder start_pos < end_pos
            # because players climbs ladder
            # players goes to higher position
            self.ladder_pos_map = {} # key -> start_pos, val -> end_pos
            self.dice_number = 0
            self._initialized = True

    def add_dice(self, dice_num):
        self.dice_number = dice_num
    
    def add_snake_pos(self, grid_pos):
        # grid_pos -> tuple
        self.ladder_pos_map[grid_pos[0]] = grid_pos[1]
    

    def add_ladder_pos(self, ladder_pos):
        # ladder_pos -> tuple
        self.ladder_pos_map[ladder_pos[0]] = ladder_pos[1]



class ObstacleFactoryService:
    def __init__(self):
        pass

    def add_snakes_in_board(self, board_obj, snake_pos_list):
        for curr_snake_pos in snake_pos_list:
            board_obj.add_snake_pos(curr_snake_pos)
    

    def add_ladders_in_board(self, board_obj, ladder_pos_list):
        for curr_ladder_pos in ladder_pos_list:
            board_obj.add_ladder_pos(curr_ladder_pos)
    

class PlayerService:
    def __init__(self):
        pass
    
    def add_player(self, name):
        player_obj = PlayerModel(name)

        return player_obj

    def update_player(self, player_obj, name):
        player_obj.update_name(name)
    

class DiceService:
    def __init__(self):
        pass
    
    def roll_dice(self, board_obj):
        dice_number = board_obj.dice_number


        dice_values = []
        while len(dice_values) < dice_number:
            num = random.randint(1, 6)
            if num not in dice_values:
                dice_values.append(num)

        return dice_values



class GameService:
    def __init__(self):
        self.players = []
        self.curr_player_index = 0
    

    def add_players_in_game(self, player_obj_list):
        for player_obj in player_obj_list:
            self.players.append(player_obj)
    
    
    def curr_turn_player(self):
        """
        initially player at 0th index will start
        at every turn index will be updated
        when index hits players list size then
        again index is reset to 0
        """
        self.curr_player_index = self.curr_player_index + 1
        if self.curr_player_index > len(self.players)-1:
            # chance will again go to the first player
            self.curr_player_index = 0

        print(f"curr player index: {self.curr_player_index }")
        player_obj = self.players[self.curr_player_index]
        return player_obj
        
    

    def update_player_pos(self, board_obj, player_obj, dice_values):
        sum = 0
        # take sum from val of all dices rolled
        for val in dice_values:
            sum = sum + val
        
        # add sum to current player pos -> player will move
        # that much grids ahead
        player_obj.position = player_obj.position + sum

        if player_obj.position > board_obj.total_grids:
            # if sum has exceeded player's pos from total grids
            # reset it back to the grid
            player_obj.position = board_obj.total_grids
        

        # see if player's position coincides with any snake start pos
        if player_obj.position in board_obj.snake_pos_map:
            # reset player_obj position to end of snake_pos
            print(f"player: {player_obj.name} bitten by snake")
            print(f"player: {player_obj.name} current pos {player_obj.position}")
            print(f"player: {player_obj.name} new pos {player_obj.position}")
            player_obj.position = board_obj.snake_pos_map[player_obj.position]
            print("\n")
        

        # see if player's position coincides with any ladder start pos
        if player_obj.position in board_obj.ladder_pos_map:
            # reset player_obj position to end of ladder pos
            print(f"player: {player_obj.name} climbing the ladder")
            print(f"player: {player_obj.name} current pos {player_obj.position}")
            
            player_obj.position = board_obj.ladder_pos_map[player_obj.position]
            print(f"player: {player_obj.name} new pos {player_obj.position}")
            print("\n")

        return player_obj


def main():
    # 10* 10 board_size -> 100 grids
    board_obj = BoardSingelton(10)

    # add obstacles in the board -> snakes, ladders
    obstacle_fac_service_obj = ObstacleFactoryService()

    # add snakes
    # start_grid -> snake head
    # end_grid -> snake tail
    # (start_grid, end_grid)
    # (start_grid > end_grd) as in actual game
    snake_pos_list = [(10, 4), (20, 10), (30, 15), (18, 12), (25, 15), (75, 60), (87, 78)]
    obstacle_fac_service_obj.add_snakes_in_board(board_obj, snake_pos_list)


    # add ladders
    # in ladder start_pos < end_pos
    # start_grid -> lower part of ladder
    # end_grid -> upper part of ladder
    ladder_pos_list = [(4, 15), (20, 30), (70, 90)]
    obstacle_fac_service_obj.add_ladders_in_board(board_obj, ladder_pos_list)

    # add dices in the board
    board_obj.add_dice(2)


    game_obj = GameService()

    # add players

    player_service_obj = PlayerService()
    player1_obj = player_service_obj.add_player("mayank")
    player2_obj = player_service_obj.add_player("mohit")

    game_obj.add_players_in_game([player1_obj, player2_obj])


    while True:
        player_obj = game_obj.curr_turn_player()

        print(f"player whose turn: {player_obj.name}")

        dice_service = DiceService()

        dice_values = dice_service.roll_dice(board_obj)

        print(f"rolled dice val: {dice_values}")

        player_obj = game_obj.update_player_pos(board_obj, player_obj, dice_values)

        print(f"curr player position {player_obj.position}")

        if player_obj.position == board_obj.total_grids:
            print(f"Player: {player_obj.name} wins")
            # break the while loop
            break
        
        print("---continue to next turn---")
        print("\n")




if __name__ == "__main__":
    main()


                


        


    


    




    


