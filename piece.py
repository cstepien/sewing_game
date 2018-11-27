from kivy.uix.scatter import Scatter
from kivy.uix.image import Image
from kivy.properties import StringProperty
from kivy.graphics import *
from kivy.graphics.instructions import InstructionGroup

class Piece(Scatter):

	def __init__(self, source, **kwargs):
		super(Piece, self).__init__(**kwargs)
		self.auto_bring_to_front = False
		self.source = source # consider using StringProperty later so we can update redraw with new sources
		self.image = Image(source=self.source)
		# why did we do scale again? 
		self.scale = self.image.texture_size[0]/self.size[0]
		self.do_scale = False	
		self.add_widget(self.image)
		
		self.instructions = InstructionGroup()
		self.canvas.add(self.instructions)

		self.stitch_coords = []
		print("Self size:", self.size, "texture size:", self.image.texture_size, "Scale:", self.scale)
		#self.end_stitch((self.center_x, self.center_y))

		'''with self.canvas:
			Color(1,1,1)
			Line(points = [self.center_x, self.center_y, 0, 0])
		'''

	def start_stitch(self, coord):
		self.stitch_coords.append(coord)

		# end_stitch currently can't deal with rotating the piece - it breaks the drawing function
		# Probably due to coordinates being messed up relative to the screen
		# there are options in Scatter to translate coordinates to scattered position
	def end_stitch(self, coord):
		self.stitch_coords.append(coord)
		self.instructions.add(Line(points=[self.stitch_coords[-2][0]/self.scale, 
			self.stitch_coords[-2][1]/self.scale, 
			self.stitch_coords[-1][0]/self.scale,
			self.stitch_coords[-1][1]/self.scale]))

	def add_stitch_coord(self, coord):
		if len(self.stitch_coords)%2==0:
			self.start_stitch(coord)
		else:
			self.end_stitch(coord)

		print(self.stitch_coords)
