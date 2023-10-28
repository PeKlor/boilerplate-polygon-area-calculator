class Rectangle:

  width = 0
  height = 0

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** 0.5

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    else:
      picture = ""
      for i in range(self.height):
        for j in range(self.width):
          picture += "*"
        picture += "\n"
      return picture

  def get_amount_inside(self, shape):
    if self.width < shape.width or self.height < shape.height:
      return 0
    else:
      return (self.width // shape.width) * (self.height // shape.height)

  def __str__(self):
    return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"
    

class Square(Rectangle):

  def __init__(self, side):
    self.side = side
    super().__init__(side, side)

  def set_side(self, side):
    self.side = side
    super().set_width(self.side)
    super().set_height(self.side)

  def set_width(self, width):
    self.set_side(width)

  def set_height(self, height):
    self.set_side(height)

  def __str__(self):
    return "Square(side=" + str(self.side) + ")"

