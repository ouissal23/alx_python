Rectangle = __import__("7-rectangle").Rectnagle
class Square(Rectangle):
    """defines square class"""
    def __init__(self, size):
        self.integer_validator("size",size)
        self.size = size
        super().__ini__(size,size)
    def __str__(self) :
        return "[Square] {}/{}".format(self.size,self.size)     
        