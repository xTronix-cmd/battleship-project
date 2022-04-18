class BattleShip:
    show_player_ship = False # Set this to True if you want to see where the ships on the grid.
    game_over = False
    player_one_sunk = 0
    player_two_sunk = 0

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
        self.ship_direction  = ""

        self.num_of_ships = int(input("Enter number of ships for the game: "))
        self.ships_length = int(input("Enter the length of all the ships: "))
        self.player_turn = int(input("Who would like to go first? (1 or 2) "))

    def start_game(self):
        for players in range(self.num_of_players):
            print("\nIt's Player {}'s turn".format(self.player_turn))
            while ships_entered < self.num_of_ships:
                start_x = int(input("Enter X: "))
                start_y = int(input("Enter Y: "))
                end_x, end_y = start_x+1, start_y+1

                self.ship_direction = input("Which direction (up,down, left, or right) would you like to place your ship? ")
                self.ship_direction = self.ship_direction.casefold()

                if self.ship_direction == "up":
                    if start_x - self.ships_length < 0:
                        print("Sorry, placement is out of grid's boundary")
                    start_x = start_x - self.ships_length + 1

                elif self.ship_direction == "down":
                    if start_x + self.ships_length >= self.grid_size:
                        print("Sorry, placement is out of grid's boundary")
                    end_x = start_x + self.ships_length

                elif self.ship_direction == "left":
                    if start_y - self.ships_length < 0:
                        print("Sorry, placement is out of grid's boundary")
                    start_y = start_y - self.ships_length + 1
                elif self.ship_direction == "right":
                    if start_y + self.ships_length >= self.grid_size:
                        print("Sorry, placement is out of grid's boundary")
                    end_y = start_y + self.ships_length
                else:
                    print("Please choose up, down, left, or right for direction")

                self.ships_coordinates.append([start_x, end_x, start_y,end_y])
                self.ships_entered += 1

            # Create Grid
            for x in range(self.row):
                rows = []
                for y in range(self.col):
                    rows.append(".")
                self.grid.append(rows)

            for ships in range(self.num_of_ships):
                for x in range(self.ships_coordinates[ships][0], self.ships_coordinates[ships][1]):
                    for y in range(self.ships_coordinates[ships][2], self.ships_coordinates[ships][3]):
                        self.grid[x][y] = "[]"

            temp_turn = self.player_turn
            if temp_turn == 1:
                self.player_one_coordinates = self.ships_coordinates
                self.player_one_grid = self.grid
                self.grid = []
                self.ships_coordinates = []
                print("\nPlayer 1's grid\n")
                
                for x in range(len(self.player_one_grid)):
                    for y in range(len(self.player_one_grid[x])):
                        if self.player_one_grid[x][y] == "[]":
                            if self.show_player_ship:
                                print("[]", end="")
                            else:
                                print(".", end=" ")
                        else:
                            print(self.player_one_grid[x][y], end=" ")
                    print("")
                self.player_turn = 2 # Switch Player
                self.ships_entered = 0
                continue

            if temp_turn == 2:
                self.player_two_coordinates = self.ships_coordinates
                self.player_two_grid = self.grid
                self.grid = []
                self.ships_coordinates = []
                print("\nPlayer 2's grid\n")

                for x in range(len(self.player_two_grid)):
                    for y in range(len(self.player_two_grid[x])):
                        if self.player_two_grid[x][y] == "[]":
                            if self.show_player_ship:
                                print("[]", end="")
                            else:
                                print(".", end=" ")
                        else:
                            print(self.player_two_grid[x][y], end=" ")
                    print("")
                self.player_turn = 1 # Switch Player
                self.ships_entered = 0
                continue
            print("")

    def proccess_game(self):
        while game_over == False:
            if self.player_turn == 1:
                self.grid = self.player_two_grid
                self.ships_coordinates = self.player_two_coordinates
            elif self.player_turn == 2:
                self.grid = self.player_one_grid
                self.ships_coordinates = self.player_one_coordinates
            
            print("Player {}'s turn, enter coordinates to fire upon.".format(self.player_turn))
            bullet_x = int(input("X: "))
            bullet_y = int(input("Y: "))

            # Marks where the bullet landed on the player's grid
            if self.grid[bullet_x][bullet_y] == ".":
                self.grid[bullet_x][bullet_y] = "X"
            elif self.grid[bullet_x][bullet_y] == "[]":
                self.grid[bullet_x][bullet_y] = "+"
                if self.player_turn == 1:
                    self.player_two_grid = self.grid
                elif self.player_turn == 2:
                    self.player_one_grid = self.grid

                # Check if ship is sunk
                for ships in range(self.num_of_ships):
                    hit = 0
                    if self.ships_coordinates[ships][0]  <= bullet_x <= self.ships_coordinates[ships][1] and self.ships_coordinates[ships][2] <= bullet_y <= self.ships_coordinates[ships][3]:
                        for x in range(self.ships_coordinates[ships][0], self.ships_coordinates[ships][1]):
                            for y in range(self.ships_coordinates[ships][2], self.ships_coordinates[ships][3]):
                                if self.grid[x][y] == "+":
                                    hit += 1
                            if hit == self.ships_length:
                                print("Player {} sunk a ship".format(self.player_turn))
                                self.ship_sunk = 1
                                if self.player_turn == 1:
                                    self.player_one_sunk += self.ship_sunk
                                elif self.player_turn == 2:
                                    self.player_two_sunk += self.ship_sunk

                # Checks if P1 or P2 sunk all the ships of the other player
                if self.player_one_sunk == self.num_of_ships or self.player_two_sunk == self.num_of_ships:
                    game_over = True
                    print("Game Over")
                    print("Player {} wins!".format(self.player_turn))
            # Switch Player
            temp_turn = self.player_turn
            if temp_turn == 1:
                self.player_turn = 2
            elif temp_turn == 2:
                self.player_turn = 1

            # Print Grid
            print("\nPlayer {}'s grid".format(self.player_turn))
            for x in range(len(self.grid)):
                for y in range(len(self.grid[x])):
                    if self.grid[x][y] == "[]":
                        if self.show_player_ship:
                            print("[]", end="")
                        else:
                            print(".", end=" ")
                    else:
                        print(self.grid[x][y], end=" ")
                print("")
            print("")