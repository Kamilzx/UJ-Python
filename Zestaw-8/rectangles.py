# Kamil Nowak, Grupa 2
# 02.12.2022r.
# Python 2022/2023
# rectangles.py


from points import Point

class Rectangle:
	"""Klasa reprezentująca prostokąty na płaszczyźnie."""

	def __init__(self, x1=0, y1=0, x2=0, y2=0):
		# Chcemy, aby x1 < x2, y1 < y2.
		self.pt1 = Point(x1, y1)
		self.pt2 = Point(x2, y2)

	def __str__(self):              # "[(x1, y1), (x2, y2)]"
		return "[{0}, {1}]".format(self.pt1, self.pt2)

	def __repr__(self):             # "Rectangle(x1, y1, x2, y2)"
		return "Rectangle({0}, {1}, {2}, {3})".format(self.pt1.x, 
			self.pt1.y, self.pt2.x, self.pt2.y)

	def __eq__(self, other):   # obsługa rect1 == rect2
		return isinstance(other, Rectangle) and self.pt1 == other.pt1 and self.pt2 == other.pt2

	def __ne__(self, other):        # obsługa rect1 != rect2
		return not self == other

	def center(self):               # zwraca środek prostokąta
		return Point((self.pt1.x + self.pt2.x)/2, (self.pt1.y + self.pt2.y)/2)

	def area(self):                 # pole powierzchni
		return abs((self.pt1.x - self.pt2.x) * (self.pt1.y - self.pt2.y))

	def move(self, x, y):           # przesunięcie o (x, y)
		self.pt1 = self.pt1 + Point(x, y)
		self.pt2 = self.pt2 + Point(x, y)

	def intersection(self, other):  # część wspólna prostokątów
		p1x = max(self.pt1.x, other.pt1.x)
		p1y = max(self.pt1.y, other.pt1.y)
		p2x = min(self.pt2.x, other.pt2.x)
		p2y = min(self.pt2.y, other.pt2.y)
		if(p1x > p2x or p1y > p2y):
			raise ValueError("no intersection between rectangles")
		return Rectangle(p1x, p1y, p2x, p2y)

	def cover(self, other):         # prostąkąt nakrywający oba
		p1x = min(self.pt1.x, other.pt1.x)
		p1y = min(self.pt1.y, other.pt1.y)
		p2x = max(self.pt2.x, other.pt2.x)
		p2y = max(self.pt2.y, other.pt2.y)
		return Rectangle(p1x, p1y, p2x, p2y)

	def make4(self):                # zwraca krotkę czterech mniejszych
		if(self == Rectangle()):
			raise ValueError("can't divide by zero")
		return (Rectangle(self.pt1.x, self.pt1.y, (self.pt2.x + self.pt1.x)/2, (self.pt2.y + self.pt1.x)/2),
				Rectangle((self.pt2.x + self.pt1.x)/2, self.pt1.y, self.pt2.x, (self.pt2.y + self.pt1.y)/2),
				Rectangle(self.pt1.x, (self.pt2.y + self.pt1.y)/2, (self.pt2.x + self.pt1.x)/2, self.pt2.y),
				Rectangle((self.pt2.x + self.pt1.x)/2, (self.pt2.y + self.pt1.y)/2, self.pt2.x, self.pt2.y))

	@classmethod
	def from_points(cls, points): # cls to access it as parameter not as an instance
		point1, point2 = points
		if not (isinstance(point2, Point) and isinstance(point1, Point)):
			raise ValueError("Argument not iterable")
		return cls(point1.x, point1.y, point2.x, point2.y)

	@property
	def top(self):
		return self.pt2.y

	@property
	def left(self):
		return self.pt1.x

	@property
	def bottom(self):
		return self.pt1.y

	@property
	def right(self):
		return self.pt2.x

	@property
	def width(self):
		return self.pt2.x - self.pt1.x

	@property
	def height(self):
		return self.pt2.y - self.pt1.y



	@property
	def topleft(self):
		return Point(self.pt1.x, self.pt2.y)

	@property
	def bottomleft(self):
		return Point(self.pt1.x, self.pt1.y)

	@property
	def topright(self):
		return Point(self.pt2.x, self.pt2.y)

	@property
	def bottomright(self):
		return Point(self.pt2.x, self.pt1.y)