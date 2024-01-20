class  Square :
    """Write a class that defines a square by private instance attribute: size."""

    def __init__(self,size=0):
        if not isinstance(size,int):
            raise TypeError("size must be an integer")
        if size <0:
            raise ValueError("size must be>=0")

        self.size = size
    def area(self):
        return(self.size*self.size)
    @property
    def size(self):
        return(self.size)
    @size.setter
    def size(self, value):
        if not isinstance(value,int):
            raise TypeError("size must br an integer")
        if value <0:
            raise ValueError("size must be >=0")
        self.size = value 
    def my_print(self):    
        if self.size==0:
            print()
        for i in range(0,self.size):
            [print("#",end="") for j in range(self.size)]
            print("")


