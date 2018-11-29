from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.anchorlayout import AnchorLayout
import foot
import piece
from kivy.core.window import Window
from kivy.graphics import Line
from kivy.clock import Clock

class SewingGame(Widget):
	def __init__(self, **kwargs):
		super(SewingGame, self).__init__(**kwargs)
		self.size = Window.size

		self.piece = piece.Piece("assets/CCDBlueTee.png")
		self.add_widget(self.piece)
		Clock.schedule_interval(self.needle_down, .1)

		self.bind(size=self.adapt)
		#self.on_size = self.adapt

		self.foot = foot.Foot()
		self.add_widget(self.foot)
		self.foot.center_foot(self.center)
	
	def adapt(self, Inst, size):
		self.foot.center_foot(self.center)

	def needle_down(self, dt):
		#pass the center to self.piece.add_stitch_coord()
		self.piece.add_stitch_coord(self.center)


class SewingApp(App):
	def build(self):
		return SewingGame()


if __name__ == '__main__':
	SewingApp().run()