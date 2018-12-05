from kivy.uix.scatter import Scatter
from kivy.uix.image import Image
from kivy.core.image import Image as CoreImage
from kivy.properties import StringProperty
from kivy.graphics import *
import pattern
from kivy.graphics.instructions import InstructionGroup

class Piece(Scatter):

	def __init__(self, source, **kwargs):
		super(Piece, self).__init__(**kwargs)
		self.auto_bring_to_front = False
		self.source = source # also look at StringProperty
		self.fabric = CoreImage.load(filename=self.source, keep_data=True)
		self.image = Image(texture=self.fabric.texture)
		self.scale = self.image.texture_size[0]/self.size[0]
		self.do_scale = False	
		self.add_widget(self.image)
		self.pattern = pattern.Pattern()
		self.add_widget(self.pattern)
		
		self.instructions = InstructionGroup()
		self.canvas.add(self.instructions)

		self.stitch_coords = []
		print("Self size:", self.size, "texture size:", self.image.texture_size, "Scale:", self.scale)
		print("Pattern size:", self.fabric.size)

	def get_alpha(self, coord):
		pixel_rgba = self.fabric.read_pixel(coord[0], coord[1])
		print('alpha:', pixel_rgba[-1])
		return pixel_rgba[-1]

	def start_stitch(self, coord):
		self.stitch_coords.append(coord)

	def end_stitch(self, coord):
		self.stitch_coords.append(coord)
		self.instructions.add(Line(points=[self.stitch_coords[-2][0], 
			self.stitch_coords[-2][1], 
			self.stitch_coords[-1][0],
			self.stitch_coords[-1][1]]))

	def add_stitch_coord(self, coord):
		local_coord = self.to_local(coord[0], coord[1])
		# The widget/app local coordinate (0,0) is in the lower left corner
		# But the original pattern has (0,0) in the upper left (is 'upside down') compared to local
		# Need to subtract scaled local coord from max y value of the pattern to make 'right side up'
		pattern_coord = (int(local_coord[0]*self.scale), self.fabric.size[1] - int(local_coord[1]*self.scale))
		alpha = self.get_alpha(pattern_coord)

		print('scatter size:', self.size, '\nstarting coord:', coord, '\nlocal coord:', 
				local_coord, '\npattern coordinates:', pattern_coord)
		
		# can probably refactor below to be better
		if alpha < 1:
			print('\n--- NOT FABRIC! \n---')
			if len(self.stitch_coords)%2==1:
				del(self.stitch_coords[-1])
		else:
			print('\n ---  FABRIC! \n---')
			if len(self.stitch_coords)%2==0:
				self.start_stitch(local_coord)
			else:
				if self.stitch_coords[-1] == local_coord:
					del(self.stitch_coords[-1])
				else: 
					self.end_stitch(local_coord)
		print(self.stitch_coords)
