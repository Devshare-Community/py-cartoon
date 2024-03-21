import turtle


def gajurel(x, y):
	turtle.setx(x)
	turtle.sety(y)
	print(x, y)

class Cartoon:

	def __init__(self):
		self.t = turtle.Turtle()
		t = self.t
		t.pensize(3)
		t.speed(9)
		t.ondrag(gajurel)
