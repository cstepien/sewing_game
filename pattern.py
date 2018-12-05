from kivy.uix.widget import Widget
from kivy.graphics import *
from kivy.core.window import Window

class Pattern(Widget):

	verteces = [50, 50, 
		-50, 50, 
		-50, -50, 
		50, -50]

	def __init__(self, **kwargs):
		super(Pattern, self).__init__(**kwargs)

		with self.canvas:
			Color(1.0, 1.0, 1.0)
			self.Lines = Line(points= self.verteces, close=True)