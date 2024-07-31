class Point:
    '''Represent a poin in a Euclidean Plane'''
    def __init__(self, x_coor,y_coor): ### init is the first method for a class
        self.x=x_coor
        self.y=y_coor
    def coordinates(self):
        '''Return a tuple of the x,y coordinates of a point'''
        return(self.x,self.y)
    def move_to(self,x_coor,y_coor):
        self.x=x_coor
        self.y=y_coor