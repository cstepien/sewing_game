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

	def end_stitch(self, coord):
		self.stitch_coords.append(coord)
		self.instructions.add(Line(points=[self.stitch_coords[-2][0], 
			self.stitch_coords[-2][1], 
			self.stitch_coords[-1][0],
			self.stitch_coords[-1][1]]))

	def add_stitch_coord(self, coord):
		coord = self.to_local(coord[0], coord[1])
		if len(self.stitch_coords)%2==0:
			self.start_stitch(coord)
		else:
			# check if end stitch is the same as prior stitch_coord - if yes, delete last stitch_coord
			# and don't add current coord
			self.end_stitch(coord)

		print(self.stitch_coords)
