from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.core.audio import SoundLoader
Window.size=(415,600)
Window.clearcolor=(1,1,1,1)
class WindowMain(Screen):
    pass

class WindowSignin(Screen):
    pass

class WindowSignup(Screen):
    pass

class MainApp(MDApp):
    music=None
    def __init__(self):
        super().__init__()
        self.menu=None
        self.screen=Builder.load_file("main.kv")
        
    def build(self):
        self.theme_cls.primary_palette ="Green"
        self.title='TGC'
        self.icon="logo.jpg"
        self.sound=SoundLoader.load('music.mp3')
        return self.screen
    def play_music(self):
        if not self.music:
            self.music=SoundLoader.load('music.mp3')
            if self.music:
                self.music.bind(on_stop=self.on_music_finish)
                self.music.play()
    def on_music_finish(self, instance):
        instance.seek(0)
        instance.play()
MainApp().run()