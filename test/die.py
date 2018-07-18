from random import randint


class Die():
	"""模拟骰子"""
	def __init__(self, num_sides):
		self.num_sides = num_sides

	def roll(self):
		return randint(1, self.num_sides)
		

