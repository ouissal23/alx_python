BaseGeometry =__import__("5-base_geometry").BaseGeometry
class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        if self.integer_validator("width",width):
            self.width = width
        if self.integer_validator("height",height):
            self.height = height 