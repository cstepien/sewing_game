from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.anchorlayout import AnchorLayout
import foot
from kivy.core.window import Window
from kivy.graphics import Line

class SewingGame(Widget):
	def __init__(self, **kwargs):
		super(SewingGame, self).__init__(**kwargs)
		self.size = Window.size

		self.bind(size=self.adapt)
		#self.on_size = self.adapt

		self.foot = foot.Foot()
		self.add_widget(self.foot)
		self.foot.center_foot((self.center_x, self.center_y))
		
	def adapt(self, Inst, size):
		self.foot.center_foot((self.center_x, self.center_y))

class SewingApp(App):
	def build(self):
		return SewingGame()


if __name__ == '__main__':
	SewingApp().run()