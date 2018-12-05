from kivy.uix.widget import Widget
from kivy.graphics import *
from kivy.core.window import Window

class Pattern(Widget):

# may need to give this a size that is smaller than the widget somehow..100x100 widget
# means that this widget is always overlapping with other same-sized widgets
# may also have to brute force it - like write our own collide function to see if 
# the foot is within a certain buffer zone of points, then redraw the pattern with 
# the part that has been sewn already missing
# we may not even need to make the pattern disappear - it doesn't do that in real life...

	verteces = [50, 50, 
		25, 50, 
		25, 25, 
		50, 25]

	def __init__(self, **kwargs):
		super(Pattern, self).__init__(**kwargs)

		with self.canvas:
			Color(1.0, 1.0, 1.0)
			self.Lines = Line(points= self.verteces, close=True)