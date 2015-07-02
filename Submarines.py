
        
class Board :

    # This function gets size of  a requested board game as a tuple
    # and returns the board as list of lists
    def __init__(self):
        self.board=[]
        self.dead = '1'
        self.alive = '2'
        self.empty = '0'
        self.attack = '3'
        self.place = '4'

    def create_Board(self,size):
        self.size=size
        for i in xrange(size[0]):
            display=''
            self.board.append([])
            for j in xrange(size[1]):
                self.board[i].append(self.empty)
                #print self[i][j]
                display += self.board[i][j]
            print display
            print "\n"
        print self.board[3][4]
        return self.board
    def disply_board(self):
        display=''
        for i in xrange(self.size[0]):
            for j in xrange(self.size[1]):
                display += self.board[i][j]
            display += "\n"
        print display



    # This function gets the Points of the start and the end of the submarine
    # and takes an action to attack or place it.
    def take_action(self,start_point,end_point,action):
         if self.check_position(start_point,end_point) == self.empty:
             if start_point.getY() - end_point.getY() != 0 :
                 for i in xrange(start_point.getY(),end_point.getY()+1):
                     self.board[start_point.getX()][i]=action
             elif start_point.getX() - end_point.getX() != 0 :
                 for i in xrange(start_point.getX(),end_point.getX()+1):
                     self.board[start_point.getY()][i]=action

    def attack_unit (self, ):

        Point start
        startX= raw_input('put the start point of your unit: ')

        self.Point end = raw_input('put the end point of your unit: ')
        self.take_action(start,end,self.attack)
    def place_unit(self):
        self.take_action(start,end,self.place)

    # This function gets start , end point and size of the submrine.
    # the function returns if it alive,dead or empty.
    def check_position(self,start_point,end_point):
         if start_point.getX()==end_point.getX():
             for i in xrange(start_point.getY(),end_point.getY()+1):
                 if self.board[start_point.getX()][i] == self.alive:
                     return self.alive
                 elif self.board[start_point.getX()][i] ==self.dead:
                     return self.dead
             return self.empty
         elif start_point.getY()==end_point.getY():
                for i in xrange(start_point.getX(),end_point.getX()+1):
                 if self.board[start_point.getX()][i] == self.alive :
                     return self.alive
                 elif self.board[start_point.getX()][i] ==self.dead:
                    return self.dead
         else:
              raise ValueError('Enter two points in same x or y cordinates')
         return self.empty




class Point ():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX (self):
        return self.x

    def getY (self):
        return self.y

    def setX (self,x):
        self.x = x

    def setY (self,y):
        self.y =y

        

class main:
    b1 = Board()
    b1.create_Board((5, 5))
    b1.unit_position(Point ( 1, 1), Point  ( 1, 4) )
    b1.disply_board()
    print (type (1))

if __name__ == '__main__':
        main()
