BaseGeometry =__import__("5-base_geometry").BaseGeometry
class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        if self.integer_validator("width",width):
            self.width = width
        if self.integer_validator("height",height):
            self.height = height 
    def area(self):     
        return self.width*self.height  
    def __str__(self):
        return "[rectangle] {}/{}".format(self.width,self.height)
    