from kivy.uix.widget import Widget
from kivy.graphics import *
from kivy.core.window import Window

class Foot(Widget):

	verteces = [-15, 25, 
		15, 25, 
		15,-25, 
		3, -13, 
		3, -5, 
		10, -5, 
		10, 5, 
		-10, 5, 
		-10, -5, 
		-3, -5, 
		-3, -13, 
		-15, -25]

	def __init__(self, **kwargs):
		super(Foot, self).__init__(**kwargs)

		with self.canvas:
			Color(1.0, 1.0, 1.0)
			self.lines = Line(points= self.recentered_verteces((self.center_x, self.center_y)), 
						close=True)

	def center_foot(self, new_center):
		self.lines.points = self.recentered_verteces(new_center)

	def recentered_verteces(self, coord):
		#self.pos = coord
		new_points = []
		for index, num in enumerate(self.verteces):
			if index%2 == 0:
				new_points.append(num+coord[0])
			elif index%2 == 1:
				new_points.append(num+coord[1])

		return new_points