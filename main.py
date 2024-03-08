from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.core.window import Window

class SnakeGame(Widget):
    def __init__(self, **kwargs):
        super(SnakeGame, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

        self.snake_body = [(Window.width / 2, Window.height / 2)]
        self.snake_direction = Vector(1, 0)
        self.food_position = self.generate_food_position()
        self.speed = 5
        Clock.schedule_interval(self.update, 1.0 / self.speed)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'up':
            self.snake_direction = Vector(0, 1)
        elif keycode[1] == 'down':
            self.snake_direction = Vector(0, -1)
        elif keycode[1] == 'left':
            self.snake_direction = Vector(-1, 0)
        elif keycode[1] == 'right':
            self.snake_direction = Vector(1, 0)

    def generate_food_position(self):
        return (
            (Window.width * 0.2 + (Window.width * 0.6 * (self.random() % 10))),
            (Window.height * 0.2 + (Window.height * 0.6 * (self.random() % 10)))
        )

    def update(self, dt):
        head = self.snake_body[0]
        new_head = (head[0] + self.snake_direction[0], head[1] + self.snake_direction[1])

        if new_head == self.food_position:
            self.snake_body.append(new_head)
            self.food_position = self.generate_food_position()
        else:
            self.snake_body.pop()
            self.snake_body.insert(0, new_head)

class SnakeApp(App):
    def build(self):
        game = SnakeGame()
        return game

if __name__ == '__main__':
    SnakeApp().run()