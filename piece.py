from kivy.uix.scatter import Scatter
from kivy.uix.image import Image
from kivy.core.image import Image as CoreImage
from kivy.properties import StringProperty
from kivy.graphics import *
from kivy.graphics.instructions import InstructionGroup

class Piece(Scatter):

	def __init__(self, source, **kwargs):
		super(Piece, self).__init__(**kwargs)
		self.auto_bring_to_front = False
		self.source = source # consider using StringProperty later so we can update redraw with new sources
		self.pattern = CoreImage.load(filename=self.source, keep_data=True)
		self.image = Image(texture=self.pattern.texture)
		self.scale = self.image.texture_size[0]/self.size[0]
		self.do_scale = False	
		self.add_widget(self.image)
		
		self.instructions = InstructionGroup()
		self.canvas.add(self.instructions)
		# get where the foot is, scale it up to the piece coords, round down (floor) to nearest pixels, 
		# get rgba of that pixel coord
		# if a is <1, don't do needle_down() - or skip adding stitches like in case of no movement of foot
		self.stitch_coords = []
		print("Self size:", self.size, "texture size:", self.image.texture_size, "Scale:", self.scale)
		print("Pattern size:", self.pattern.size)

	def get_rgba(self, coord):
		pixel_rgba = self.pattern.read_pixel(coord[0], coord[1])
		print(pixel_rgba)

	def start_stitch(self, coord):
		self.stitch_coords.append(coord)

	def end_stitch(self, coord):
		self.stitch_coords.append(coord)
		self.instructions.add(Line(points=[self.stitch_coords[-2][0], 
			self.stitch_coords[-2][1], 
			self.stitch_coords[-1][0],
			self.stitch_coords[-1][1]]))

	def add_stitch_coord(self, coord, piece_coord):
		local_coord = self.to_local(coord[0], coord[1])
		# self.get_rgba(local_coord)
		# the two methods of calculating pattern coordinates give different results when piece is rotated
		# next step: skip stitch drawing when alpha = 0, to see which set of pattern coords is correct
		pattern_coord = (int(coord[0] - piece_coord[0]), int(coord[1] - piece_coord[1]))
		abs_pattern_coord_test = (int(abs(local_coord[0])*self.scale), int(abs(local_coord[1])*self.scale))
		if pattern_coord == abs_pattern_coord_test:
			print('\n ---- \n SAME RESULT \n ---- \n')
		else:
			print('\n ---- \n DIFFERENT RESULT \n ---- \n')
		print('scatter size:', self.size, '\nstarting coord:', coord, '\nlocal coord:', 
				local_coord, '\npattern coordinates:', pattern_coord, '\nabsolute pattern coords:', abs_pattern_coord_test)
		if len(self.stitch_coords)%2==0:
			self.start_stitch(local_coord)
		else:
			# check if end stitch is the same as prior stitch_coord - if yes, delete last stitch_coord
			# and don't add current coord
			self.end_stitch(local_coord)

		print(self.stitch_coords)
