show_player_ship = False # Set this to True if you want to see where the ships on the grid.
game_over = False
player_one_sunk = 0
player_two_sunk = 0

num_of_ships = int(input("Enter number of ships for the game: "))
ships_length = int(input("Enter the length of all the ships: "))
player_turn = int(input("Who would like to go first? (1 or 2) "))

class BattleShip:
    def __init__(self):
        self.ship_sunk = 0
        self.ships_coordinates = []
        self.grid = [] 
        self.grid_size = 10
        self.row, self.col = 0, 0
        self.ships_entered = 0
        self.player_one_coordinates = []
        self.player_two_coordinates = []
        self.player_one_grid = []
        self.player_two_grid = []
        self.num_of_players = 2
        self.temp_turn = 0       

    def start_game(self):
        for players in range(self.num_of_players):
            print("\nIt's Player {}'s turn".format(player_turn))
            while ships_entered < num_of_ships:
                start_x = int(input("Enter X: "))
                start_y = int(input("Enter Y: "))
                end_x, end_y = start_x+1, start_y+1

                ship_direction = input("Which direction (up,down, left, or right) would you like to place your ship? ")
                ship_direction = ship_direction.casefold()

                if ship_direction == "up":
                    if start_x - ships_length < 0:
                        print("Sorry, placement is out of grid's boundary")
                    start_x = start_x - ships_length + 1

                elif ship_direction == "down":
                    if start_x + ships_length >= grid_size:
                        print("Sorry, placement is out of grid's boundary")
                    end_x = start_x + ships_length

                elif ship_direction == "left":
                    if start_y - ships_length < 0:
                        print("Sorry, placement is out of grid's boundary")
                    start_y = start_y - ships_length + 1
                elif ship_direction == "right":
                    if start_y + ships_length >= grid_size:
                        print("Sorry, placement is out of grid's boundary")
                    end_y = start_y + ships_length
                else:
                    print("Please choose up, down, left, or right for direction")

                ships_coordinates.append([start_x, end_x, start_y,end_y])
                ships_entered += 1

            # Create Grid
            for x in range(row):
                rows = []
                for y in range(col):
                    rows.append(".")
                grid.append(rows)

            for ships in range(num_of_ships):
                for x in range(ships_coordinates[ships][0], ships_coordinates[ships][1]):
                    for y in range(ships_coordinates[ships][2], ships_coordinates[ships][3]):
                        grid[x][y] = "[]"

            temp_turn = player_turn
            if temp_turn == 1:
                player_one_coordinates = ships_coordinates
                player_one_grid = grid
                grid = []
                ships_coordinates = []
                print("\nPlayer 1's grid\n")
                
                for x in range(len(player_one_grid)):
                    for y in range(len(player_one_grid[x])):
                        if player_one_grid[x][y] == "[]":
                            if show_player_ship:
                                print("[]", end="")
                            else:
                                print(".", end=" ")
                        else:
                            print(player_one_grid[x][y], end=" ")
                    print("")
                player_turn = 2 # Switch Player
                ships_entered = 0
                continue

            if temp_turn == 2:
                player_two_coordinates = ships_coordinates
                player_two_grid = grid
                grid = []
                ships_coordinates = []
                print("\nPlayer 2's grid\n")

                for x in range(len(player_two_grid)):
                    for y in range(len(player_two_grid[x])):
                        if player_two_grid[x][y] == "[]":
                            if show_player_ship:
                                print("[]", end="")
                            else:
                                print(".", end=" ")
                        else:
                            print(player_two_grid[x][y], end=" ")
                    print("")
                player_turn = 1 # Switch Player
                ships_entered = 0
                continue
            print("")

    def proccess_game(self):
        while game_over == False:
            if player_turn == 1:
                grid = player_two_grid
                ships_coordinates = player_two_coordinates
            elif player_turn == 2:
                grid = player_one_grid
                ships_coordinates = player_one_coordinates
            
            print("Player {}'s turn, enter coordinates to fire upon.".format(player_turn))
            bullet_x = int(input("X: "))
            bullet_y = int(input("Y: "))

            # Marks where the bullet landed on the player's grid
            if grid[bullet_x][bullet_y] == ".":
                grid[bullet_x][bullet_y] = "X"
            elif grid[bullet_x][bullet_y] == "[]":
                grid[bullet_x][bullet_y] = "+"
                if player_turn == 1:
                    player_two_grid = grid
                elif player_turn == 2:
                    player_one_grid = grid

                # Check if ship is sunk
                for ships in range(num_of_ships):
                    hit = 0
                    if ships_coordinates[ships][0]  <= bullet_x <= ships_coordinates[ships][1] and ships_coordinates[ships][2] <= bullet_y <= ships_coordinates[ships][3]:
                        for x in range(ships_coordinates[ships][0], ships_coordinates[ships][1]):
                            for y in range(ships_coordinates[ships][2], ships_coordinates[ships][3]):
                                if grid[x][y] == "+":
                                    hit += 1
                            if hit == ships_length:
                                print("Player {} sunk a ship".format(player_turn))
                                ship_sunk = 1
                                if player_turn == 1:
                                    player_one_sunk += ship_sunk
                                elif player_turn == 2:
                                    player_two_sunk += ship_sunk

                # Checks if P1 or P2 sunk all the ships of the other player
                if player_one_sunk == num_of_ships or player_two_sunk == num_of_ships:
                    game_over = True
                    print("Game Over")
                    print("Player {} wins!".format(player_turn))
            # Switch Player
            temp_turn = player_turn
            if temp_turn == 1:
                player_turn = 2
            elif temp_turn == 2:
                player_turn = 1

            # Print Grid
            print("\nPlayer {}'s grid".format(player_turn))
            for x in range(len(grid)):
                for y in range(len(grid[x])):
                    if grid[x][y] == "[]":
                        if show_player_ship:
                            print("[]", end="")
                        else:
                            print(".", end=" ")
                    else:
                        print(grid[x][y], end=" ")
                print("")
            print("")