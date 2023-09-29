"""
A Python module for the Gomoku game.

Implements the Gomoku game. Two players on an 8x8 grid take turns
to try and get 5 of their pieces in a row, either vertically,
horizontally or diagonally.
"""
from copy import deepcopy



def newGame(player1, player2):
    """
    Function to initialise new game by creating a dictionary
    of necessary components.

    Parameters
    ----------
    player1 : str
        The name of player 1
    player2 : str
        The name of player 2

    Returns
    -------
    game: dict
        A dictionary used to initialise the game.
        Holds the names of player 1 and 2, whose turn it currently is
        and the gameboard.

    """
    board = [[0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0]]
    game = {
        'player1' : player1,
        'player2' : player2,
        'who' : 1,
        'board' : board
        }
    
    return(game)



def printBoard(board):
    """
    Function to print the gameboard in a more visually
    appealing format.

    Parameters
    ----------
    board : list
        The gameboard to be played on. It is a nested list.

    """
    print("  |a|b|c|d|e|f|g|h|")
    print(" ","+-"*8+"+")
    for a in range (0,8):
        print(a+1,"|",end="")
        for b in range (0,8):
            if board[a][b] == 1:
                print("X",end="")
            elif board[a][b] == 2:
                print("O",end="")
            else:
                print(" ",end="")
            print("|",end="")
        print("")
    print(" ","+-"*8+"+")



def posToIndex(s):
    """
    Function to convert string of position to tuple form or
    an integer (for row) and a letter (for column).

    Parameters
    ----------
    s : str
        holds the row and column position of the move
        to be made

    Raises
    ------
    ValueError
        Raised when the length of the variable 's' is
        not 2.
        If length is 2, raised also if either both of
        the characters/digits in 's' are both strings 
        or both are integers
        Also raised if the digit in 's' is not between 1-8
        or if the characters in 's' is not between a-h.

    Returns
    -------
    (news[0]-1,letterIndex) : Tuple
        A tuple which returns the row and column position
        of the move as indices, where 'news[0]-1' is the 
        row and letterIndex is the column.

    """
    newS = s.replace(" ","")
    if len(newS) != 2:
        raise ValueError
    newS = newS.lower()
    newS = list(newS)
    
    try:
        newS[0] = int(newS[0])
        newS[1] = int(newS[1])
    except Exception:
        try:
            newS[1] = int(newS[1])
        except Exception:
            if isinstance(newS[0], int) == False and isinstance(newS[0], int) == False:
                raise ValueError
            pass
    if isinstance(newS[0], int) == True and isinstance(newS[1], int) == True:
        raise ValueError
    
    if isinstance(newS[0], str) == True:
        temp = newS[0]
        newS[0] = newS[1]
        newS[1] = temp
    letterList = ["a","b","c","d","e","f","g","h"]
    if newS[0] > 0 and newS[0] < 9 and newS[1] in letterList:
        letterIndex = letterList.index(newS[1])
        return (newS[0]-1,letterIndex)
    else:
        raise ValueError



def indexToPos(t):
    """
    Function to convert tuple of indices position to string 
    format.

    Parameters
    ----------
    t : Tuple
        Tuple of the form (r,c) with r corresponding to
        row index and c corresponding to column index.

    Returns
    -------
    letter+str(t[0]+1) : str
        A string of the corresponding to the board column
        and row, with a letter from a-h and a digit from 1-8

    """
    letterList = ["a","b","c","d","e","f","g","h"]
    letter = letterList[t[1]]
    return letter+str(t[0]+1)



def loadGame(filename):
    """
    Function takes a file, attempts to open it and load a game.

    Parameters
    ----------
    filename : str
        The name of the text file

    Raises
    ------
    FileNotFoundError
        If the file cannot be accessed, a FileNotFoundError is raised
    ValueError
        If the text file is not correctly formatted, with player1 or player2
        being empty strings or who not equal to 1 or 2, then a ValueError 
        is raised.

    Returns
    -------
    myDict : dict
        A dictionary used to initialise the game.
        Holds the names of player 1 and 2, whose turn it currently is
        and the gameboard.

    """
    try:    
        loadedFile = open(filename,mode="rt",encoding="utf8")
    except Exception:
        raise FileNotFoundError
    
    try:
        myDict = {}
        fileLines = loadedFile.readlines()
        player1 = str(fileLines[0].strip())
        player2 = str(fileLines[1].strip())
        who = int(fileLines[2].strip())
        if player1 == "" or player2 == "" or (who != 1 and who != 2):
            raise ValueError
        board=[]
        for a in range(3,11):
            line = fileLines[a].strip()
            line = line.split(",")
            board.append([])
            
            for b in range(0,8):
                line[b] = int(line[b])
                board[a-3].append(line[b])
        
        myDict["player1"] = player1
        myDict["player2"] = player2
        myDict["who"] = who
        myDict["board"] = board
        loadedFile.close()
        return myDict
    
    except Exception:
        raise ValueError



def getValidMoves(board):
    """
    Function gets a list of all valid moves available on the
    gameboard.

    Parameters
    ----------
    board : list
        The gameboard to be played on. It is a nested list.

    Returns
    -------
    movesList : list
        A list of tuples of all possible moves available to be chosen
        by the player.

    """
    movesList = []
    for x in range(0,8):
        for y in range (0,8):
            if board[x][y] == 0:
                movesList.append((x,y))
    return movesList



def makeMove(board,move,who):
    """
    Function applies the move of the player to the board and
    returns the updated board.

    Parameters
    ----------
    board : list
        The gameboard to be played on. It is a nested list.
    move : tuple
        contains the row and column index of the move to be made.
    who : int
        Holds an integer corresponding to whose turn it is.

    Returns
    -------
    printBoard(board) : function
        returns the function printBoard(board) which will print
        out a nicely formatted board.

    """
    if who == 1:
        board[move[0]][move[1]] = 1
    else:
        board[move[0]][move[1]] = 2
    return printBoard(board)

    
    
def hasWon(board,who):
    """
    Function checks if the player has won by checking if they have
    5 positions in a row.

    Parameters
    ----------
    board : list
        The gameboard to be played on. It is a nested list.
    who : tuple
        contains the row and column index of the move to be made.

    Returns
    -------
    bool
        If there are player1/player2 occupies 5 adjacent positions
        horizontally, vertically or diagonally, the function returns
        True. Otherwise the function returns False.

    """
    for u in range (0,8):
        for v in range (0,4):
            
                    for a in range (0,5):
                        if board[u][v] == board[u][v+a]:
                            if a == 4 and board[u][v] == who:
                                return True
                        else:
                            break
                        
    for w in range (0,4):
        for x in range (0,8):
            
                    for b in range (0,5):
                        if board[w][x] == board[w+b][x]:
                            if b == 4 and board[w][x] == who:
                                return True
                        else:
                            break
                        
    for y in range (0,4):
        for z in range (0,4):
            
                    for c in range (0,5):
                        if board[y][z] == board[y+c][z+c]:
                            if c == 4 and board[y][z] == who:
                                return True
                        else:
                            break
                        
    return False
    


def suggestMove1(board,who):
    """
    Function used to suggest moves for the computer player.
    Checks if computer has any immediate winning positions or 
    losing positions, otherwise defaults to the first available
    position.

    Parameters
    ----------
    board : list
        The gameboard to be played on. It is a nested list.
    who : tuple
        Contains the row and column index of the move to be made.

    Returns
    -------
    possibleMoves[a] : tuple
        A tuple of the position that should be selected by the computer
        for them to win (getting 5 in a row)
    possibleMoves[b] : tuple
        A tuple of the position that should be selected by the computer
        to prevent the other player winning (getting 5 in a row).
    possibleMoves[0] : tuple
        A tuple of the first available position.
        

    """
    possibleMoves = list(getValidMoves(board))
    
    for a in range (0,len(possibleMoves)):
        board2 = deepcopy(board)
        board2[possibleMoves[a][0]][possibleMoves[a][1]] = who
        if hasWon(board2, who) == True:
            return(possibleMoves[a])
        else:
            board2[possibleMoves[a][0]][possibleMoves[a][1]] = 0
    
    if who == 1:
        who = 2
    else:
        who = 1
    
    for b in range (0,len(possibleMoves)):
        board3 = deepcopy(board)
        board3[possibleMoves[b][0]][possibleMoves[b][1]] = who
        if hasWon(board3, who) == True:
            return(possibleMoves[b])
        else:
            board3[possibleMoves[b][0]][possibleMoves[b][1]] = 0
    
    return(possibleMoves[0])

    

def play():
    """
    Function used to play the game.
    Asks for names of player1 and player2 and creates new 'game'
    dictionary to initialise game.
    If user wants to load a game then they will be asked for the
    file name of the game and attempt to load it.
    Asks the player for their move and checks if it is a valid move.
    If valid, applies the move, returns the updated board and checks
    if the player has won.
    This is repeated for the other player until a player has won.
    If there are no more available positions and nobody has won,
    a draw is declared.

    """
    print("*"*55)
    print("***"+" "*8+"WELCOME TO YASIN'S GOMOKU!"+" "*8+"***")
    print("*"*55,"\n")
    print("Enter the players' names, or type 'C' or 'L'.\n")
    player1 = ""
    player2 = ""
    while player1 == "":
        player1 = input("Player 1: ").capitalize()
        
    if player1 == "L":
        filename = input("Enter file name: ")
        if filename == "":
            filename = "game.txt"
        
        try:
            myDict = loadGame(filename)
            player1 = myDict["player1"]
            player2 = myDict["player2"]
            turn = myDict["who"]
            if turn == 1:
                currentPlayer = player1
            else:
                currentPlayer = player2
                
        except Exception:
            print("File cannot be loaded.")
        
    else:
        while player2 == "":
            player2 = input("Player 2: ").capitalize()
        myDict = newGame(player1,player2)
    
        currentPlayer = player1
    
    while True:
        
        if currentPlayer != "C":
            s = input("\nEnter your move: ")
            found = False
            while found == False:
                try:
                    move = posToIndex(s)
                    availableMoves = getValidMoves(myDict["board"])
                    
                    while (move in availableMoves) == False:
                        s = input("Enter a valid move: ")
                        move = posToIndex(s)
                        
                    found = True

                except Exception:
                    s = input("Enter a valid move: ")
                    
            print("")
            makeMove(myDict["board"], move, myDict["who"])
            
        elif currentPlayer == "C":
           move = suggestMove1(myDict["board"], myDict["who"])
           print("")
           makeMove(myDict["board"], move, myDict["who"])
        
        if hasWon(myDict["board"], myDict["who"]) == True:
            print("\n",currentPlayer, "has won!")
            break
        elif getValidMoves(myDict["board"]) == []:
            print("\nThe game is a draw!")
            break
        
        if myDict["who"] == 1:
            myDict["who"] = 2
        else:
            myDict["who"] = 1
        
        if currentPlayer == player1:
            currentPlayer = player2
        else:
            currentPlayer = player1
       


if __name__ == '__main__' or __name__ == 'builtins':
 play()
