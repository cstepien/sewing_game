from kivy.uix.scatter import Scatter
from kivy.uix.image import Image
from kivy.properties import StringProperty

class Piece(Scatter):

	def __init__(self, source, **kwargs):
		super(Piece, self).__init__(**kwargs)
		self.auto_bring_to_front = False
		self.source = source # consider using StringProperty later so we can update redraw with new sources
		self.image = Image(source=self.source)
		self.scale = self.image.texture_size[0]/self.size[0]
		self.do_scale = False	
		self.add_widget(self.image)