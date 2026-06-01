from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class TradingBot(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text="Bot Status: Ready")
        btn = Button(text="Run Trading Simulation")
        btn.bind(on_press=self.run_bot)
        layout.add_widget(self.label)
        layout.add_widget(btn)
        return layout

    def run_bot(self, instance):
        self.label.text = "Bot Running: Analyzing Market..."

if __name__ == '__main__':
    TradingBot().run()

