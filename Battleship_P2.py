class BattleShip:
    show_player_ship = True # Set this to True if you want to see where the ships on the grid.
    game_over = False
    player_one_sunk = 0
    player_two_sunk = 0

    def __init__(self):
        self.ship_sunk = 0
        self.ships_coordinates = []
        self.grid = [] 
        self.grid_size = 10
        self.row, self.col = 10, 10
        self.ships_entered = 0
        self.player_one_coordinates = []
        self.player_two_coordinates = []
        self.player_one_grid = []
        self.player_two_grid = []
        self.num_of_players = 2
        self.temp_turn = 0       
        self.ship_direction  = ['u', 'd', 'l', 'r']
        self.row_alphabet = []

        # Create the row alphabet
        for char in range(65, 65 + self.grid_size):
            self.row_alphabet.append(chr(char))

    # Initialize/creates an emptry grid of 10x10
    def empty_grid(self):
        self.grid = []
        # for loop to make the blank grid 10x10 matrix
        for x in range(self.row):
            rows = []
            for y in range(self.col):
                rows.append(".")
            self.grid.append(rows)
        
    def start_game(self):
        self.num_of_ships = int(input("Enter number of ships for the game: "))
        self.ships_length = int(input("Enter the length of all the ships: "))
        self.player_turn = int(input("Who would like to go first? (1 or 2) "))

        for player in range(self.num_of_players):  # self.num_of_players = 2
            print("\nIt's Player {}'s turn".format(self.player_turn))

            
            self.empty_grid()  # creates an empty grid

            # This is to label the columns of the grid 0-9
            print(" ", end=" ")
            for column_label in range(self.grid_size):
                print(column_label, end=" ")
            
            print()

            for x in range(len(self.grid)):  # x is row
                print(self.row_alphabet[x], end=" ")
                for y in range(len(self.grid[x])):  # y is column
                    print(self.grid[x][y], end=" ")
                print("")  # prints a newline after each row of the grid

            player_turn = self.player_turn
            if player_turn == 1:
                self.player_one_coordinates = self.enter_ship()
                self.player_turn = 2
            elif player_turn == 2:
                self.player_two_coordinates = self.enter_ship()
                self.player_turn = 1
            
        print("\nPlayer 1's grid\n")
        self.player_one_grid = self.create_grid(self.player_one_coordinates.copy())
        print(f"Player one coordinates: {self.player_one_coordinates}")

        print("\nPlayer 2's grid\n")
        self.player_two_grid = self.create_grid(self.player_two_coordinates.copy())
        print(f"Player two coordinates: {self.player_two_coordinates}")

        self.proccess_game()

    # Place ships on the grid
    def enter_ship(self):
        player_coordinates = []
        for ship in range(self.num_of_ships):
            # CAPTURE user input error! /* must be fixed */
            # This block of code is to take the coordinate input for the ships
            chosen_coordinates = input(": ")  # ie. A4 would be 0, 4 on the x,y coordinate
            chosen_coordinates = chosen_coordinates.upper()
            start_x = self.row_alphabet.index(chosen_coordinates[0])
            start_y = int(chosen_coordinates[1])
            end_x, end_y = start_x+1, start_y+1

            chosen_direction = input("Which direction (U, D, L, R) would you like to place your ship? ")
            chosen_direction = chosen_direction.casefold()
            if chosen_direction in self.ship_direction:
                if chosen_direction == "u" and start_x - self.ships_length >= 0:
                    start_x = start_x - self.ships_length + 1

                elif chosen_direction == "d" and start_x + self.ships_length < self.grid_size:
                    end_x = start_x + self.ships_length

                elif chosen_direction == "l" and start_y - self.ships_length >= 0:
                    start_y = start_y - self.ships_length + 1

                elif chosen_direction == "r" and start_y + self.ships_length < self.grid_size:
                    end_y = start_y + self.ships_length
                else:
                    print("Sorry, placement is out of grid's boundary")
            else:
                print("Please choose up, down, left, or right for direction")

            player_coordinates.append([start_x, end_x, start_y,end_y])
        
        return player_coordinates

    # Create Grid
    def create_grid(self, ships_coordinates):
        # Making the blank grid
        self.empty_grid()
        
        # Placing the ships on the grid 
        for ships in range(self.num_of_ships):
            for x in range(ships_coordinates[ships][0], ships_coordinates[ships][1]):  # self.ships_coordinates[#ship][start_x] self.ships_coordinates[#ship][end_x]
                for y in range(ships_coordinates[ships][2], ships_coordinates[ships][3]): # self.ships_coordinates[#ship][start_y] self.ships_coordinates[#ship][end_y]
                    self.grid[x][y] = "O"  # updates the grid with ships in placed

        print(" ", end=" ")
        for column_label in range(self.grid_size):
            print(column_label, end=" ")
        
        print()
        
        # Printing the ships on the grid
        for x in range(len(self.grid)):  # x is row
            print(self.row_alphabet[x], end=" ")
            for y in range(len(self.grid[x])):  # y is column
                if self.grid[x][y] == "O":
                    if self.show_player_ship:
                        print("D", end=" ")
                    else:
                        print(".", end=" ")
                else:
                    print(self.grid[x][y], end=" ")
            print("")  # prints a newline after each row of the grid
            
        return self.grid

    def proccess_game(self):
        while self.game_over == False:
            # copies player's grid to game's grid and player's coordinates to ships coordinates
            if self.player_turn == 1:
                self.grid = self.player_two_grid
                self.ships_coordinates = self.player_two_coordinates
            elif self.player_turn == 2:
                self.grid = self.player_one_grid
                self.ships_coordinates = self.player_one_coordinates
            
            print("Player {}'s turn, enter coordinates to fire upon.".format(self.player_turn))
            coordinates = input(": ")
            coordinates = coordinates.upper()
            bullet_x = self.row_alphabet.index(coordinates[0])
            bullet_y = int(coordinates[1])

            # Marks where the bullet landed on the player's grid
            if self.grid[bullet_x][bullet_y] == ".":
                self.grid[bullet_x][bullet_y] = "X"  # Shot Missed
            elif self.grid[bullet_x][bullet_y] == "O":
                self.grid[bullet_x][bullet_y] = "/"  # Shot Hit
                # This marks where the bullet hit on the player's grid
                if self.player_turn == 1:
                    self.player_two_grid = self.grid  
                elif self.player_turn == 2:
                    self.player_one_grid = self.grid

                # Check if ship is sunk
                for ships in range(self.num_of_ships):
                    hit = 0
                    # Check if the bullet hit part of the ship
                    if self.ships_coordinates[ships][0]  <= bullet_x <= self.ships_coordinates[ships][1] and self.ships_coordinates[ships][2] <= bullet_y <= self.ships_coordinates[ships][3]:
                        for x in range(self.ships_coordinates[ships][0], self.ships_coordinates[ships][1]):
                            for y in range(self.ships_coordinates[ships][2], self.ships_coordinates[ships][3]):
                                if self.grid[x][y] == "/":
                                    hit += 1
                        if hit == self.ships_length:
                            hit = 0
                            print("Player {} sunk a ship".format(self.player_turn))

                            # This is to count how many ships a player sunk already
                            if self.player_turn == 1:
                                self.player_one_sunk += 1  
                            elif self.player_turn == 2:
                                self.player_two_sunk += 1 

                # Checks if P1 or P2 sunk all the ships of the other player
                if self.player_one_sunk == self.num_of_ships or self.player_two_sunk == self.num_of_ships:
                    self.game_over = True
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

            print(" ", end=" ")
            for column_label in range(self.grid_size):
                print(column_label, end=" ")
            
            print()  # Prints new line after the column label printed

            for x in range(len(self.grid)):
                print(self.row_alphabet[x], end=" ")
                for y in range(len(self.grid[x])):
                    if self.grid[x][y] == "O":
                        if self.show_player_ship:
                            print("D", end=" ")
                        else:
                            print(".", end=" ")
                    else:
                        print(self.grid[x][y], end=" ")
                print("")
            print("")

game = BattleShip()
game.start_game()