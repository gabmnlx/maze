# Mon Gabriel F. Lagustan
# 192706
# October 3, 2019

# I have not discussed the Python language code in my program 
# with anyone other than my instructor or the teaching assistants 
# assigned to this course.

# I have not used Python language code obtained from another student, 
# or any other unauthorized source, either modified or unmodified.

# If any Python language code or documentation used in my program 
# was obtained from another source, such as a textbook or website, 
# that has been clearly noted with a proper citation in the comments 
# of my program.

# this is level 1
def column1_row1():
    maze1 =[  "┌───┬───────┐",
              "│ o │       │", 
              "│       ────┤",
              "│           │",
              "│   ┌───    │",
              "│   │     x │",
              "└───┴───────┘",
            ]
    for i in maze1:
        print(i)
    print("Available Directions: South ")
    print("Which direction will you take?")
    
def column1_row2():
    maze1 =[  "┌───┬───────┐",
              "│   │       │", 
              "│       ────┤",
              "│ o         │",
              "│   ┌───    │",
              "│   │     x │",
              "└───┴───────┘",
            ]
    for i in maze1:
        print(i)
    print("Available Directions: North South East ")
    print("Which direction will you take?")
def column1_row3():
    maze1 =[  "┌───┬───────┐",
              "│   │       │", 
              "│       ────┤",
              "│           │",
              "│   ┌───    │",
              "│ o │     x │",
              "└───┴───────┘",
            ]
    for i in maze1:
        print(i)
    print("Available Directions: North ")
    print("Which direction will you take?")
def column2_row1():
    maze1 =[  "┌───┬───────┐",
              "│   │ o     │", 
              "│       ────┤",
              "│           │",
              "│   ┌───    │",
              "│   │     x │",
              "└───┴───────┘",
            ]
    for i in maze1:
        print(i)
    print("Available Directions: East South ")
    print("Which direction will you take?")
def column2_row2():
    maze1 =[  "┌───┬───────┐",
              "│   │       │", 
              "│       ────┤",
              "│     o     │",
              "│   ┌───    │",
              "│   │     x │",
              "└───┴───────┘",
            ]
    for i in maze1:
        print(i)
    print("Available Directions: North East West ")
    print("Which direction will you take?")
def column2_row3():
    maze1 =[  "┌───┬───────┐",
              "│   │       │", 
              "│       ────┤",
              "│           │",
              "│   ┌───    │",
              "│   │ o   x │",
              "└───┴───────┘",
            ]
    for i in maze1:
        print(i)
    print("Available Directions: East ")
    print("Which direction will you take?")
def column3_row1():
    maze1 =[  "┌───┬───────┐",
              "│   │     o │", 
              "│       ────┤",
              "│           │",
              "│   ┌───    │",
              "│   │     x │",
              "└───┴───────┘",
            ]
    for i in maze1:
        print(i)
    print("Available Directions: West ")
    print("Which direction will you take?")
def column3_row2():
    maze1 =[  "┌───┬───────┐",
              "│   │       │", 
              "│       ────┤",
              "│         o │",
              "│   ┌───    │",
              "│   │     x │",
              "└───┴───────┘",
            ]
    for i in maze1:
        print(i)
    print("Available Directions: West South ")
    print("Which direction will you take?")
def column3_row3():
    maze1 =[  "┌───┬───────┐",
              "│   │       │", 
              "│       ────┤",
              "│           │",
              "│   ┌───    │",
              "│   │     x │",
              "└───┴───────┘",
            ]
    for i in maze1:
        print(i)
def bye():
    print("Found the exit!")
    print("Goodbye.")
def quit():
    print("Try again next time.")
    print("Goodbye.")
#introduction 
print("Welcome to the Maze!")
difficulty = input("Select a Level: 1, 2, or 3 ")
position = int(input("Starting point: "))
if difficulty == "1":
    while position > 0:        
        if position == 1:
            column1_row1()
            move1 = input().lower()
            if move1 == "south":
                column1_row2()
                position+=1
            elif move1 == "quit":
                quit()
                break
            else:
                print("Please choose an available direction.")                
        elif position == 2:
        #end of move 1
            column1_row2()
            move2 = input().lower()
            if move2 == "east":
                column2_row2()
                position+= 3
            elif move2 == "south":
                column1_row3()
                position+=1
            elif move2 == "north":
                column1_row1()
                position-=1
            elif move2 == "quit": 
                quit()
                break
            else:
                print("Please choose an available direction.")
        #end of move 2
        elif position == 3:
            column1_row3()
            move3 = input().lower()
            if move3 == "north":
                column1_row2()    
                position-=1
            elif move3 == "quit":
                quit()
                break
            else:
                print("Please choose an available direction.")
        #end of move 3
        elif position == 4:
            column2_row1()
            move4 = input().lower()
            if move4 == "south":
                column2_row2()  
                position+=1
            elif move4 == "east":
                column3_row1()
                position+=3
            elif move4 == "quit":
                quit()
                break
            else: 
                print("Please choose an available direction.")
        #end of move 4
        elif position == 5:
            column2_row2()
            move5 = input().lower()
            if move5 == "north":
                column2_row1()
                position-=1
            elif move5 == "west":
                column1_row2()
                position-=3
            elif move5 == "east":
                column3_row2()
                position+=3
            elif move5 == "quit":
                quit()
                break
            else:
                print("Please choose an available direction.")
        #end of move 5
        elif position == 6:
            column2_row3()
            move6 = input().lower()
            if move6 == "east":
                column3_row3()
                position+=3
            elif move6 == "quit":
                quit()
                break
            else:
                print("Please choose an available direction.")
        #end of move 6
        elif position == 7:
            column3_row1()
            move7 = input().lower()
            if move7 == "west":
                column2_row1()
                position-=3
            elif move7 == "quit":
                quit()
                break
            else:
                print("Please choose an available direction.")
        #end of move 7
        elif position == 8:
            column3_row2()
            move8 = input().lower()
            if move8 == "south":
                column3_row3()
                bye()
                break
            elif move8 == "west":
                column2_row2()
                position-=3
            elif move8 == "quit":
                quit()
                break
            else:
                print("Please choose an available direction.")
        #end of move 8 
        
        #end of level 1
#============================================================================================  level 2     
def c1_r1():
    maze2 = ["╓──────────────────╖",
             "╫ o                ╫",  
             "╫    ──────────┐   ╫",
             "╫              │   ╫",
             "╫   ┌────┬─────┘   ╫",
             "╫   │    │         ╫",
             "╫        │         ╫",
             "╫        │     │ x ╫",  
             "╙────────┴─────┴───╜"
             ]
    for i in maze2:
        print(i)
    print("Available Directions: South ")
    print("Which direction will you take?")
def c1_r2():
    maze2 = ["╓──────────────────╖",
             "╫                  ╫",  
             "╫    ──────────┐   ╫",
             "╫ o            │   ╫",
             "╫   ┌────┬─────┘   ╫",
             "╫   │    │         ╫",
             "╫        │         ╫",
             "╫        │     │ x ╫",  
             "╙────────┴─────┴───╜"
             ]
    for i in maze2:
        print(i)
    print("Available Directions: North South East")
    print("Which direction will you take?")
def c1_r3():
    maze2 = ["╓──────────────────╖",
             "╫                  ╫",  
             "╫    ──────────┐   ╫",
             "╫              │   ╫",
             "╫   ┌────┬─────┘   ╫",
             "╫ o │    │         ╫",
             "╫        │         ╫",
             "╫        │     │ x ╫",  
             "╙────────┴─────┴───╜"
             ]
    for i in maze2:
        print(i)
    print("Available Directions: North South ")
    print("Which direction will you take?")
def c1_r4():
    maze2 = ["╓──────────────────╖",
             "╫                  ╫",  
             "╫    ──────────┐   ╫",
             "╫              │   ╫",
             "╫   ┌────┬─────┘   ╫",
             "╫   │    │         ╫",
             "╫        │         ╫",
             "╫ o      │     │ x ╫",  
             "╙────────┴─────┴───╜"
             ]
    for i in maze2:
        print(i)
    print("Available Directions: North East ")
    print("Which direction will you take?")
def c2_r1():
    maze2 = ["╓──────────────────╖",
             "╫      o           ╫",  
             "╫    ──────────┐   ╫",
             "╫              │   ╫",
             "╫   ┌────┬─────┘   ╫",
             "╫   │    │         ╫",
             "╫        │         ╫",
             "╫        │     │ x ╫",  
             "╙────────┴─────┴───╜"
             ]
    for i in maze2:
        print(i)
    print("Available Directions: West East")
    print("Which direction will you take?")
def c2_r2():
    maze2 = ["╓──────────────────╖",
             "╫                  ╫",  
             "╫    ──────────┐   ╫",
             "╫      o       │   ╫",
             "╫   ┌────┬─────┘   ╫",
             "╫   │    │         ╫",
             "╫        │         ╫",
             "╫        │     │ x ╫",  
             "╙────────┴─────┴───╜"
             ]
    for i in maze2:
        print(i)
    print("Available Directions: East West")
    print("Which direction will you take?")
def c2_r3():
    maze2 = ["╓──────────────────╖",
             "╫                  ╫",  
             "╫    ──────────┐   ╫",
             "╫              │   ╫",
             "╫   ┌────┬─────┘   ╫",
             "╫   │  o │         ╫",
             "╫        │         ╫",
             "╫        │     │ x ╫",  
             "╙────────┴─────┴───╜"
             ]
    for i in maze2:
        print(i)
    print("Available Directions: South ")
    print("Which direction will you take?")
        
def c2_r4():
    maze2 = ["╓──────────────────╖",
             "╫                  ╫",  
             "╫    ──────────┐   ╫",
             "╫              │   ╫",
             "╫   ┌────┬─────┘   ╫",
             "╫   │    │         ╫",
             "╫        │         ╫",
             "╫      o │     │ x ╫",  
             "╙────────┴─────┴───╜"
             ]
    for i in maze2:
        print(i)
    print("Available Directions: North West")
    print("Which direction will you take?")
def c3_r1():
    maze2 = ["╓──────────────────╖",
             "╫           o      ╫",  
             "╫    ──────────┐   ╫",
             "╫              │   ╫",
             "╫   ┌────┬─────┘   ╫",
             "╫   │    │         ╫",
             "╫        │         ╫",
             "╫        │     │ x ╫",  
             "╙────────┴─────┴───╜"
             ]
    for i in maze2:
        print(i)
    print("Available Directions: East West")
    print("Which direction will you take?")
def c3_r2():
    maze2 = ["╓──────────────────╖",
             "╫                  ╫",  
             "╫    ──────────┐   ╫",
             "╫           o  │   ╫",
             "╫   ┌────┬─────┘   ╫",
             "╫   │    │         ╫",
             "╫        │         ╫",
             "╫        │     │ x ╫",  
             "╙────────┴─────┴───╜"
             ]
    for i in maze2:
        print(i)
    print("Available Directions: West")
    print("Which direction will you take?")
def c3_r3():
    maze2 = ["╓──────────────────╖",
             "╫                  ╫",  
             "╫    ──────────┐   ╫",
             "╫              │   ╫",
             "╫   ┌────┬─────┘   ╫",
             "╫   │    │  o      ╫",
             "╫        │         ╫",
             "╫        │     │ x ╫",  
             "╙────────┴─────┴───╜"
             ]
    for i in maze2:
        print(i)
    print("Available Directions: South East")
    print("Which direction will you take?")
def c3_r4():
    maze2 = ["╓──────────────────╖",
             "╫                  ╫",  
             "╫    ──────────┐   ╫",
             "╫              │   ╫",
             "╫   ┌────┬─────┘   ╫",
             "╫   │    │         ╫",
             "╫        │         ╫",
             "╫        │  o  │ x ╫",  
             "╙────────┴─────┴───╜"
             ]
    for i in maze2:
        print(i)
    print("Available Directions: North")
    print("Which direction will you take?")
def c4_r1():
    maze2 = ["╓──────────────────╖",
             "╫                o ╫",  
             "╫    ──────────┐   ╫",
             "╫              │   ╫",
             "╫   ┌────┬─────┘   ╫",
             "╫   │    │         ╫",
             "╫        │         ╫",
             "╫        │     │ x ╫",  
             "╙────────┴─────┴───╜"
             ]
    for i in maze2:
        print(i)
    print("Available Directions: West South ")
    print("Which direction will you take?")
def c4_r2():
    maze2 = ["╓──────────────────╖",
             "╫                  ╫",  
             "╫    ──────────┐   ╫",
             "╫              │ o ╫",
             "╫   ┌────┬─────┘   ╫",
             "╫   │    │         ╫",
             "╫        │         ╫",
             "╫        │     │ x ╫",  
             "╙────────┴─────┴───╜"
             ]
    for i in maze2:
        print(i)
    print("Available Directions: North South ")
    print("Which direction will you take?")
def c4_r3():
    maze2 = ["╓──────────────────╖",
             "╫                  ╫",  
             "╫    ──────────┐   ╫",
             "╫              │   ╫",
             "╫   ┌────┬─────┘   ╫",
             "╫   │    │       o ╫",
             "╫        │         ╫",
             "╫        │     │ x ╫",  
             "╙────────┴─────┴───╜"
             ]
    for i in maze2:
        print(i)
    print("Available Directions: South West")
    print("Which direction will you take?")
def c4_r4():
    maze2 = ["╓──────────────────╖",
             "╫                  ╫",  
             "╫    ──────────┐   ╫",
             "╫              │   ╫",
             "╫   ┌────┬─────┘   ╫",
             "╫   │    │         ╫",
             "╫        │         ╫",
             "╫        │     │ x ╫",  
             "╙────────┴─────┴───╜"
             ]
    for i in maze2:
        print(i)        
if difficulty == "2":
    while position > 0:
        if position == 1:
            c1_r1()
            move1 = input().lower()
            if move1 == "south":
                position+=1
            if move1 == "east":
                position+=4
            elif move1 == "quit":
                quit()
                break
            else:
                print("Please choose an available direction")
        elif position == 2:
            c1_r2()
            move2 = input().lower()
            if move2 == "north":
                position-=1
            elif move2 == "east":
                position+=4
            elif move2 == "south":
                position+=1
            elif move2 == "quit":
                quit()
                break
            else:
                print("Please choose an available direction.")
        elif position == 3:
            c1_r3()
            move3 = input().lower()
            if move3 == "north":
                position-=1
            elif move3 == "south":
                position+=1
            elif move3 == "quit":
                quit()
                break
            else:
                print("Please choose an available direction.")
        elif position == 4:
            c1_r4()
            move4 = input().lower()
            if move4 == "north":
                position-=1
            elif move4 == "east":
                position+=4
            elif move4 == "quit":
                quit()
                break
            else:
                print("Please choose an available direction.")
        elif position == 5:
            c2_r1()
            move5 = input().lower()
            if move5 == "east":
                position+=4
            elif move5 == "west":
                position-=4
            elif move5 == "quit":
                quit()
                break
            else:
                print("Please choose an available direction.")
        elif position == 6:
            c2_r2()
            move6 = input().lower()
            if move6 == "west":
                position-=4
            elif move6 == "east":
                position+=4
            elif move6 == "quit":
                quit()
                break
            else:
                print("Please choose an available direction.")
        elif position == 7:
            c2_r3()
            move7 = input().lower()
            if move7 == "south":
                position+=1
            elif move7 == "quit":
                quit()
                break
            else:
                print("Please choose an available direction.")
        elif position == 8:
            c2_r4()
            move8 = input().lower()
            if move8 == "north":
                position-=1
            elif move8 == "west":
                position-=4
            elif move8 == "quit":
                quit()
                break
            else:
                print("Please choose an available direction.")
        elif position == 9:
            c3_r1()
            move9 = input().lower()
            if move9 == "east":
                position+=4
            elif move9 == "west":
                position-=4
            elif move9 == "quit":
                quit()
                break
            else:
                print("Please choose an available direction.")
        elif position == 10:
            c3_r2()
            move10 = input().lower()
            if move10 == "west":
                position-=4
            elif move10 == "quit":
                quit()
                break
            else:
                print("Please choose an available direction.")
        elif position == 11:
            c3_r3()
            move11 = input().lower()
            if move11 == "east":
                position+=4
            elif move11 == "south":
                position+=1
            elif move11 == "quit":
                quit()
                break
            else: 
                print("Print choose an available direction.")
        elif position == 12:
            c3_r4()
            move12 = input().lower()
            if move12 == "north":
                position-=1
            elif move12 == "quit":
                quit()
                break
            else:
                print("Please choose an available direction.")
        elif position == 13:
            c4_r1()
            move13 = input().lower()
            if move13 == "west":
                position-=4
            elif move13 == "south":
                position+=1
            elif move13 == "quit":
                quit()
                break
            else:
                print("Please choose an available direction.")
        elif position == 14:
            c4_r2()
            move14 = input().lower()
            if move14 == "north":
                position-=1
            elif move14 == "south":
                position+=1
            elif move14 == "quit":
                quit()
                break
            else:
                print("Please choose an available direction.")
        elif position == 15:
            c4_r3()
            move15 = input().lower()
            if move15 == "south":
                position+=1
            elif move15 == "west":
                position-=4
            elif move15 == "north":
                position-=1
            elif move15 == "quit":
                quit()
                break
            else:
                print("Please choose an available direction.")
        elif position == 16:
            c4_r4()
            print("Found the exit!")
            print("Goodbye.")
            break
#=======================================================================================level 3
def col1_r1():
    maze3 = ["┌───────────────────┬─────┐",
			 "│ o                 │     │",
			 "│    ─────┐               │",
			 "│         │    │          │",
			 "├─────────┘    │     ─────┤",
			 "│              │          │",
			 "│          ────┼────      │",
			 "│    │         │          │",
			 "│    └────┐    │     ─────┤",
			 "│         │    │        x │",
			 "└─────────┴────┴──────────┘",
			 ]
    for i in maze3:
        print(i)
    print("Available Directions: South East")
    print("Which direction will you take?")
def col1_r2():
    maze3 = ["┌───────────────────┬─────┐",
             "│                   │     │",
             "│    ─────┐               │",
             "│ o       │    │          │",
             "├─────────┘    │     ─────┤",
             "│              │          │",
             "│          ────┼────      │",
             "│    │         │          │",
             "│    └────┐    │     ─────┤",
             "│         │    │          │",
             "└─────────┴────┴──────────┘",
             ]
    for i in maze3:
        print(i)
    print("Available Directions: North East ")
    print("Which direction will you take?")
def col1_r3():
    maze3 = ["┌───────────────────┬─────┐",
             "│                   │     │",
             "│    ─────┐               │",
             "│         │    │          │",
             "├─────────┘    │     ─────┤",
             "│ o            │          │",
             "│          ────┼────      │",
             "│    │         │          │",
             "│    └────┐    │     ─────┤",
             "│         │    │        x │",
             "└─────────┴────┴──────────┘",
             ]
    for i in maze3:
        print(i)
    print("Available Directions: South East")
    print("Which direction will you take?")
def col1_r4():
    maze3 = ["┌───────────────────┬─────┐",
             "│                   │     │",
             "│    ─────┐               │",
             "│         │    │          │",
             "├─────────┘    │     ─────┤",
             "│              │          │",
             "│          ────┼────      │",
             "│ o  │         │          │",
             "│    └────┐    │     ─────┤",
             "│         │    │        x │",
             "└─────────┴────┴──────────┘",
             ]
    for i in maze3:
        print(i)
    print("Available Directions: North South ")
    print("Which direction will you take?")
def col1_r5():
    maze3 = ["┌───────────────────┬─────┐",
             "│                   │     │",
             "│    ─────┐               │",
             "│         │    │          │",
             "├─────────┘    │     ─────┤",
             "│              │          │",
             "│          ────┼────      │",
             "│    │         │          │",
             "│    └────┐    │     ─────┤",
             "│ o       │    │        x │",
             "└─────────┴────┴──────────┘",
             ]
    for i in maze3:
        print(i)
    print("Available Directions: South West ")
    print("Which direction will you take?")
def col2_r1():
    maze3 = ["┌───────────────────┬─────┐",
             "│       o           │     │",
             "│    ─────┐               │",
             "│         │    │          │",
             "├─────────┘    │     ─────┤",
             "│              │          │",
             "│          ────┼────      │",
             "│    │         │          │",
             "│    └────┐    │     ─────┤",
             "│         │    │        x │",
             "└─────────┴────┴──────────┘",
             ]
    for i in maze3:
        print(i)
    print("Available Directions: East West ")
    print("Which direction will you take?")
def col2_r2():
    maze3 = ["┌───────────────────┬─────┐",
             "│                   │     │",
             "│    ─────┐               │",
             "│       o │    │          │",
             "├─────────┘    │     ─────┤",
             "│              │          │",
             "│          ────┼────      │",
             "│    │         │          │",
             "│    └────┐    │     ─────┤",
             "│         │    │        x │",
             "└─────────┴────┴──────────┘",
             ]
    for i in maze3:
        print(i)
    print("Available Directions: West ")
    print("Which direction will you take?")
def col2_r3():
    maze3 = ["┌───────────────────┬─────┐",
             "│                   │     │",
             "│    ─────┐               │",
             "│         │    │          │",
             "├─────────┘    │     ─────┤",
             "│       o      │          │",
             "│          ────┼────      │",
             "│    │         │          │",
             "│    └────┐    │     ─────┤",
             "│         │    │        x │",
             "└─────────┴────┴──────────┘",
             ]
    for i in maze3:
        print(i)
    print("Available Directions: East West ")
    print("Which direction will you take?")
def col2_r4():
    maze3 = ["┌───────────────────┬─────┐",
             "│                   │     │",
             "│    ─────┐               │",
             "│         │    │          │",
             "├─────────┘    │     ─────┤",
             "│              │          │",
             "│          ────┼────      │",
             "│    │  o      │          │",
             "│    └────┐    │     ─────┤",
             "│         │    │        x │",
             "└─────────┴────┴──────────┘",
             ]
    for i in maze3:
        print(i)
    print("Available Directions: North East ")
    print("Which direction will you take?")
def col2_r5():
    maze3 = ["┌───────────────────┬─────┐",
             "│                   │     │",
             "│    ─────┐               │",
             "│         │    │          │",
             "├─────────┘    │     ─────┤",
             "│              │          │",
             "│          ────┼────      │",
             "│    │         │          │",
             "│    └────┐    │     ─────┤",
             "│       o │    │        x │",
             "└─────────┴────┴──────────┘",
             ]
    for i in maze3:
        print(i)
    print("Available Directions: West ")
    print("Which direction will you take?")
def col3_r1():
    maze3 = ["┌───────────────────┬─────┐",
             "│            o      │     │",
             "│    ─────┐               │",
             "│         │    │          │",
             "├─────────┘    │     ─────┤",
             "│              │          │",
             "│          ────┼────      │",
             "│    │         │          │",
             "│    └────┐    │     ─────┤",
             "│         │    │        x │",
             "└─────────┴────┴──────────┘",
             ]
    for i in maze3:
        print(i)
    print("Available Directions: South West East ")
    print("Which direction will you take?")
def col3_r2():
    maze3 = ["┌───────────────────┬─────┐",
             "│                   │     │",
             "│    ─────┐               │",
             "│         │  o │          │",
             "├─────────┘    │     ─────┤",
             "│              │          │",
             "│          ────┼────      │",
             "│    │         │          │",
             "│    └────┐    │     ─────┤",
             "│         │    │        x │",
             "└─────────┴────┴──────────┘",
             ]
    for i in maze3:
        print(i)
    print("Available Directions: North South ")
    print("Which direction will you take?")
def col3_r3():
    maze3 = ["┌───────────────────┬─────┐",
             "│                   │     │",
             "│    ─────┐               │",
             "│         │    │          │",
             "├─────────┘    │     ─────┤",
             "│            o │          │",
             "│          ────┼────      │",
             "│    │         │          │",
             "│    └────┐    │     ─────┤",
             "│         │    │        x │",
             "└─────────┴────┴──────────┘",
             ]
    for i in maze3:
        print(i)
    print("Available Directions: West North ")
    print("Which direction will you take?")
def col3_r4():
    maze3 = ["┌───────────────────┬─────┐",
             "│                   │     │",
             "│    ─────┐               │",
             "│         │    │          │",
             "├─────────┘    │     ─────┤",
             "│              │          │",
             "│          ────┼────      │",
             "│    │       o │          │",
             "│    └────┐    │     ─────┤",
             "│         │    │        x │",
             "└─────────┴────┴──────────┘",
             ]
    for i in maze3:
        print(i)
    print("Available Directions: West South ")
    print("Which direction will you take?")
def col3_r5():
    maze3 = ["┌───────────────────┬─────┐",
             "│                   │     │",
             "│    ─────┐               │",
             "│         │    │          │",
             "├─────────┘    │     ─────┤",
             "│              │          │",
             "│          ────┼────      │",
             "│    │         │          │",
             "│    └────┐    │     ─────┤",
             "│         │  o │        x │",
             "└─────────┴────┴──────────┘",
             ]
    for i in maze3:
        print(i)
    print("Available Directions: North ")
    print("Which direction will you take?")
def col4_r1():
    maze3 = ["┌───────────────────┬─────┐",
             "│                 o │     │",
             "│    ─────┐               │",
             "│         │    │          │",
             "├─────────┘    │     ─────┤",
             "│              │          │",
             "│          ────┼────      │",
             "│    │         │          │",
             "│    └────┐    │     ─────┤",
             "│         │    │        x │",
             "└─────────┴────┴──────────┘",
             ]
    for i in maze3:
        print(i)
    print("Available Directions: West South ")
    print("Which direction will you take?")
def col4_r2():
    maze3 = ["┌───────────────────┬─────┐",
             "│                   │     │",
             "│    ─────┐               │",
             "│         │    │  o       │",
             "├─────────┘    │     ─────┤",
             "│              │          │",
             "│          ────┼────      │",
             "│    │         │          │",
             "│    └────┐    │     ─────┤",
             "│         │    │        x │",
             "└─────────┴────┴──────────┘",
             ]
    for i in maze3:
        print(i)
    print("Available Directions: North South East ")
    print("Which direction will you take?")
def col4_r3():
    maze3 = ["┌───────────────────┬─────┐",
             "│                   │     │",
             "│    ─────┐               │",
             "│         │    │          │",
             "├─────────┘    │     ─────┤",
             "│              │  o       │",
             "│          ────┼────      │",
             "│    │         │          │",
             "│    └────┐    │     ─────┤",
             "│         │    │        x │",
             "└─────────┴────┴──────────┘",
             ]
    for i in maze3:
        print(i)
    print("Available Directions: North East ")
    print("Which direction will you take?")
def col4_r4():
    maze3 = ["┌───────────────────┬─────┐",
             "│                   │     │",
             "│    ─────┐               │",
             "│         │    │          │",
             "├─────────┘    │     ─────┤",
             "│              │          │",
             "│          ────┼────      │",
             "│    │         │  o       │",
             "│    └────┐    │     ─────┤",
             "│         │    │        x │",
             "└─────────┴────┴──────────┘",
             ]
    for i in maze3:
        print(i)
    print("Available Directions: East South ")
    print("Which direction will you take?")
def col4_r5():
    maze3 = ["┌───────────────────┬─────┐",
             "│                   │     │",
             "│    ─────┐               │",
             "│         │    │          │",
             "├─────────┘    │     ─────┤",
             "│              │          │",
             "│          ────┼────      │",
             "│    │         │          │",
             "│    └────┐    │     ─────┤",
             "│         │    │  o     x │",
             "└─────────┴────┴──────────┘",
             ]
    for i in maze3:
        print(i)
    print("Available Directions: North East ")
    print("Which direction will you take?")
def col5_r1():
    maze3 = ["┌───────────────────┬─────┐",
             "│                   │  o  │",
             "│    ─────┐               │",
             "│         │    │          │",
             "├─────────┘    │     ─────┤",
             "│              │          │",
             "│          ────┼────      │",
             "│    │         │          │",
             "│    └────┐    │     ─────┤",
             "│         │    │        x │",
             "└─────────┴────┴──────────┘",
             ]
    for i in maze3:
        print(i)
    print("Available Directions: South ")
    print("Which direction will you take?")
def col5_r2():
    maze3 = ["┌───────────────────┬─────┐",
             "│                   │     │",
             "│    ─────┐               │",
             "│         │    │       o  │",
             "├─────────┘    │     ─────┤",
             "│              │          │",
             "│          ────┼────      │",
             "│    │         │          │",
             "│    └────┐    │     ─────┤",
             "│         │    │        x │",
             "└─────────┴────┴──────────┘",
             ]
    for i in maze3:
        print(i)
    print("Available Directions: North West ")
    print("Which direction will you take?")
def col5_r3():
    maze3 = ["┌───────────────────┬─────┐",
             "│                   │     │",
             "│    ─────┐               │",
             "│         │    │          │",
             "├─────────┘    │     ─────┤",
             "│              │       o  │",
             "│          ────┼────      │",
             "│    │         │          │",
             "│    └────┐    │     ─────┤",
             "│         │    │        x │",
             "└─────────┴────┴──────────┘",
             ]
    for i in maze3:
        print(i)
    print("Available Directions: South West ")
    print("Which direction will you take?")
def col5_r4():
    maze3 = ["┌───────────────────┬─────┐",
             "│                   │     │",
             "│    ─────┐               │",
             "│         │    │          │",
             "├─────────┘    │     ─────┤",
             "│              │          │",
             "│          ────┼────      │",
             "│    │         │       o  │",
             "│    └────┐    │     ─────┤",
             "│         │    │        x │",
             "└─────────┴────┴──────────┘",
             ]
    for i in maze3:
        print(i)
    print("Available Directions: North West ")
    print("Which direction will you take?")
def col5_r5():
    maze3 = ["┌───────────────────┬─────┐",
             "│                   │     │",
             "│    ─────┐               │",
             "│         │    │          │",
             "├─────────┘    │     ─────┤",
             "│              │          │",
             "│          ────┼────      │",
             "│    │         │          │",
             "│    └────┐    │     ─────┤",
             "│         │    │       x  │",
             "└─────────┴────┴──────────┘",
             ]
    for i in maze3:
        print(i)
def invalid():
    print("Please choose an available direction.")
if difficulty == "3":
 while position > 0:
    if position == 1:
        col1_r1()
        move1 = input().lower()
        if move1 == "south":
            position+=1
        elif move1 == "east":
            position+=5
        elif move1 == "quit":
            quit()
            break
        else:
            invalid()
    elif position == 2:
        col1_r2()
        move2 = input().lower()
        if move2 == "north":
            position-=1
        elif move2 == "east":
            position+=5
        elif move2 == "quit":
            quit()
            break
        else:
            invalid()
    elif position == 3:
        col1_r3()
        move3 = input().lower()
        if move3 == "south":
            position+=1
        elif move3 == "east":
            position+=5
        elif move3 == "quit":
            quit()
            break
        else:
            invalid()
    elif position == 4:
        col1_r4()
        move4 = input().lower()
        if move4 == "north":
            position-=1
        elif move4 == "south":
            position+=1
        elif move4 == "quit":
            quit()
            break
        else:
            invalid()
    elif position == 5:
        col1_r5()
        move5 = input().lower()
        if move5 == "north":
            position-=1
        elif move5 == "east":
            position+=5
        elif move5 == "quit":
            quit()
            break
        else:
            invalid()
    elif position == 6:
        col2_r1()
        move6 = input().lower()
        if move6 == "east":
            position+=5
        elif move6 == "west":
            position-=5
        elif move6 == "quit":
            quit()
            break
        else:
            invalid()
    elif position == 7:
        col2_r2()
        move7 = input().lower()
        if move7 == "west":
            position-=5
        elif move7 == "quit":
            quit()
            break
        else:
            invalid()
    elif position == 8:
        col2_r3()
        move8 = input().lower()
        if move8 == "east":
            position+=5
        elif move8 == "west":
            position-=5
        elif move8 == "south":
            position+=1
        elif move8 == "quit":
            quit()
            break
        else:
            invalid()
    elif position == 9:
        col2_r4()
        move9 = input().lower()
        if move9 == "north":
            position-=1
        elif move9 == "east":
            position+=5
        elif move9 == "quit":
            quit()
            break
        else:
            invalid()
    elif position == 10:
        col2_r5()
        move10 = input().lower()
        if move10 == "west":
            position-=5
        elif move10 == "quit":
            quit()
            break
        else:
            invalid()
    elif position == 11:
        col3_r1()
        move11 = input().lower()
        if move11 == "south":
            position+=1
        elif move11 == "east":
            position+=5
        elif move11 == "west":
            position-=5
        elif move11 == "quit":
            quit()
            break
        else:
            invalid()
    elif position == 12:
        col3_r2()
        move12 = input().lower()
        if move12 == "north":
            position-=1
        elif move12 == "south":
            position+=1
        elif move12 == "quit":
            quit()
            break
        else:
            invalid()
    elif position == 13:
        col3_r3()
        move13 = input().lower()
        if move13 == "north":
            position-=1
        elif move13 == "west":
            position-=5
        elif move13 == "quit":
            quit()
            break
        else:
            invalid()
    elif position == 14:
        col3_r4()
        move14 = input().lower()
        if move14 == "west":
            position-=5
        elif move14 == "south":
            position+=1
        elif move14 == "quit":
            quit()
            break
        else:
            invalid()
    elif position == 15:
        col3_r5()
        move15 = input().lower()
        if move15 == "north":
            position-=1
        elif move15 == "quit":
            quit()
            break
        else:
            invalid()
    elif position == 16:
        col4_r1()
        move16 = input().lower()
        if move16 == "west":
            position-=5
        elif move16 == "south":
            position+=1
        elif move16 == "quit":
            quit()
            break
        else:
            invalid()
    elif position == 17:
        col4_r2()
        move17 = input().lower()
        if move17 == "north":
            position-=1
        elif move17 == "east":
            position+=5
        elif move17 == "south":
            position+=1
        elif move17 == "quit":
            quit()
            break
        else:
            invalid()
    elif position == 18:
        col4_r3()
        move18 = input().lower()
        if move18 == "north":
            position-=1
        elif move18 == "east":
            position+=5
        elif move18 == "quit":
            quit()
            break
        else:
            invalid()
    elif position == 19:
        col4_r4()
        move19 = input().lower()
        if move19 == "east":
            position+=5
        elif move19 == "south":
            position+=1
        elif move19 == "quit":
            quit()
            break
        else:
            invalid()
    elif position == 20:
        col4_r5()
        move20 = input().lower()
        if move20 == "north":
            position-=1
        elif move20 == "east":
            position+=5
        elif move20 == "quit":
            quit()
            break
        else:
            invalid()
    elif position == 21:
        col5_r1()
        move21 = input().lower()
        if move21 == "south":
            position+=1
        elif move21 == "quit":
            quit()
            break
        else:
            invalid()
    elif position == 22:
        col5_r2()
        move22 = input().lower()
        if move22 == "north":
            position-=1
        elif move22 == "west":
            position-=5
        elif move22 == "quit":
            quit()
            break
        else:
            invalid()
    elif position == 23:
        col5_r3()
        move23 = input().lower()
        if move23 == "south":
            position+=1
        elif move23 == "west":
            position-=5
        elif move23 == "quit":
            quit()
            break
        else:
            invalid()
    elif position == 24:
        col5_r4()
        move24 = input().lower()
        if move24 == "west":
            position-=5
        elif move24 == "north":
            position-=1
        elif move24 == "quit":
            quit()
            break
        else:
            invalid()
    elif position == 25:
        col5_r5()
        print("Found the exit!")
        print("Goodbye.")
        break
        
            
        
            
            
		


				

				

				

				

				

				

				

				

				

				

				

				
		

				

				

				

				

				

				

				

		
		

		

		
            
    