

class Board  (object):

    #
    def __init__(self,size):
        self.board=[]
        self.size=size
        for i in xrange(size[0]):
            self.board.append([])
            for j in xrange(size[1]):
                self.board[i].append("???")
        return self.board


    # not relevant i need to recevie the coordinate from the submarines

    def disply_board(self):

        display=''
        for i in xrange(self.size[0]):
            for j in xrange(self.size[1]):
                display += self.board[i][j]
            display += "\n"
        print display


class Submarine (object):
    def __init__(self):

        self.lifeParts=[]
        self.coordinates = []
        self.size = int(raw_input(" put the size of your submarine: "))
        # request input from  the player for it's coordinates and size
        print ("put the coridinates of your submarine one piece at a time. \n" /
                              " for example : 3,4")
        for i in self.size :
            self.coordinates.append(raw_input("put your cordinate: "))
            self.lifeParts.append(False)
        print "You have finished to place your submarine"

    def status (self,attackCoordinate):
        for i in self.coordinates:
            if self.coordinates[i]== attackCoordinate:
                self.lifeParts[i] = True
                if False not in self.lifeParts:
                    return "The Submarine destroyed"
                else:
                    return "This was a Hit"
        return "This was a miss!!"




class Player (object):

    def __init__(self,numUnits):
        self.score=0
        self.numUnits = numUnits
        self.submarines = []
        self.name = raw_input("Enter your name: ")


    def place_units(self):
        for i in self.numUnits:
            self.submarines.append(Submarine())


    def attack(self):
        coordinate = raw_input("put the cordinate of your attack: ")

class Game (object):
    def __init__(self):
        self.numUnits = raw_input("Enter number of maximun units to each player: ")
        self.board_size = raw_input("Enter the size of the board like this \n 5,5 or 6,3")
        self.player1 = Player(self.numUnits)
        self.player2 = Player(self.numUnits)
        self.board = Board(self.board_size)




        


def main(self):
    game = Game()




if __name__ == '__main__':
    main()