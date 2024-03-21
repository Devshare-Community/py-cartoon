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

	def meme(self, x, y):
		self.t.penup()
		self.t.goto(x, y)
		self.t.pendown()

	def aankha1(self, x, y):
		self.meme(x, y)
		t = self.t
		t.seth(0)
		t.fillcolor('#333333')
		t.begin_fill()
		t.circle(22)
		t.end_fill()

		self.meme(x, y + 10)
		t.fillcolor('#000000')
		t.begin_fill()
		t.circle(10)
		t.end_fill()

		self.meme(x + 6, y + 22)
		t.fillcolor('#ffffff')
		t.begin_fill()
		t.circle(10)
		t.end_fill()

	def aankha2(self, x, y):
		self.meme(x, y)
		t = self.t
		t.seth(0)
		t.fillcolor('#333333')
		t.begin_fill()
		t.circle(22)
		t.end_fill()

		self.meme(x, y + 10)
		t.fillcolor('#000000')
		t.begin_fill()
		t.circle(10)
		t.end_fill()

		self.meme(x - 6, y + 22)
		t.fillcolor('#ffffff')
		t.begin_fill()
		t.circle(10)
		t.end_fill()

	def mukh(self, x, y):
		self.meme(x, y)
		t = self.t

		t.fillcolor('#88141D')
		t.begin_fill()

		l1 = []
		l2 = []
		t.seth(190)
		a = 0.7
		for i in range(28):
			a += 0.1
			t.right(3)
			t.fd(a)
			l1.append(t.position())

		self.meme(x, y)

		t.seth(10)
		a = 0.7
		for i in range(28):
			a += 0.1
			t.left(3)
			t.fd(a)
			l2.append(t.position())

		t.seth(10)
		t.circle(50, 15)
		t.left(180)
		t.circle(-50, 15)

		t.circle(-50, 40)
		t.seth(233)
		t.circle(-50, 55)
		t.left(180)
		t.circle(50, 12.1)
		t.end_fill()

		self.meme(17, 54)
		t.fillcolor('#DD716F')
		t.begin_fill()
		t.seth(145)
		t.circle(40, 86)
		t.penup()
		for pos in reversed(l1[:20]):
			t.goto(pos[0], pos[1] + 1.5)
		for pos in l2[:20]:
			t.goto(pos[0], pos[1] + 1.5)
		t.pendown()
		t.end_fill()

		self.meme(-17, 94)
		t.seth(8)
		t.fd(4)
		t.back(8)

	def gaala1(self, x, y):
		turtle.tracer(False)
		t = self.t
		self.meme(x, y)
		t.seth(300)
		t.fillcolor('#DD4D28')
		t.begin_fill()
		a = 2.3
		for i in range(120):
			if 0 <= i < 30 or 60 <= i < 90:
				a -= 0.05
				t.lt(3)
				t.fd(a)
			else:
				a += 0.05
				t.lt(3)
				t.fd(a)
		t.end_fill()
		turtle.tracer(True)

	def gaala2(self, x, y):
		t = self.t
		turtle.tracer(False)
		self.meme(x, y)
		t.seth(60)
		t.fillcolor('#DD4D28')
		t.begin_fill()
		a = 2.3
		for i in range(120):
			if 0 <= i < 30 or 60 <= i < 90:
				a -= 0.05
				t.lt(3)
				t.fd(a)
			else:
				a += 0.05
				t.lt(3)
				t.fd(a)
		t.end_fill()
		turtle.tracer(True)

	def kaan1(self, x, y):
		t = self.t
		self.meme(x, y)
		t.fillcolor('#000000')
		t.begin_fill()
		t.seth(330)
		t.circle(100, 35)
		t.seth(219)
		t.circle(-300, 19)
		t.seth(110)
		t.circle(-30, 50)
		t.circle(-300, 10)
		t.end_fill()
