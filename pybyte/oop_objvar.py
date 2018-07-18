class Robot(object):
	"""docstring for Robot"""

	# 一个类变量， 用来计数机器人的数量
	population = 0

	def __init__(self, name):
		# super(Robot, self).__init__()
		self.name = name
		print("(Initializing {})".format(self.name))
		# 当有人被创建时，机器人会增加人数
		Robot.population += 1

	def die(self):
		print("{} is being destroyed!".format(self.name))
		Robot.population -= 1
		if Robot.population == 0:
			print("{} was the last one.".format(self.name))
		else:
			print("There are still {} robots working.".format(Robot.population))

	def greet(self):
		print("Greetings, my masters call me {}".format(self.name))

	@classmethod
	def how_many(cls):
		print("We are {:d} robots.".format(cls.population))

droid1 = Robot("R2-D2")
droid1.greet()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.greet()
Robot.how_many()

print("Robots are working......")

print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()
Robot.how_many()
		