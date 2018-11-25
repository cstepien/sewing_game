from kivy.uix.scatter import Scatter
from kivy.uix.image import Image
from kivy.properties import StringProperty

class Piece(Scatter):

	def __init__(self, source, **kwargs):
		super(Piece, self).__init__(**kwargs)
		self.source = StringProperty(None)
		self.add_widget(Image(source="assets/CCDBlueTee.png"))