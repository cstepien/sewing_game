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
		Clock.schedule_interval(self.needle_down, 2)
		Clock.schedule_interval(self.detect_foot_on_pattern, 2)

		self.bind(size=self.adapt)

		self.foot = foot.Foot()
		self.add_widget(self.foot)
		self.foot.center_foot(self.center)

		# I think the foot and the pattern are on different coord systems
		# they are always colliding
		# to debug, print out position of the foot vs. position of the pattern
		# may need to do translation, or put the pattern on a different layer/parent
	
	def detect_foot_on_pattern(self, *args):
		if self.foot.collide_widget(self.piece.pattern):
			print('\n---- COLLISION! ---\n')
		else:
			print('no collision')
	
	def adapt(self, Inst, size):
		self.foot.center_foot(self.center)

	def needle_down(self, dt):
		self.piece.add_stitch_coord(self.center)


class SewingApp(App):
	def build(self):
		return SewingGame()


if __name__ == '__main__':
	SewingApp().run()