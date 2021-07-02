from kivy.app import App
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
import os

#setting the whole grid through kivy
KV = """
FloatLayout:
    canvas:
        Color: 
            rgba: [1,0.5,0.3,1]
        Rectangle:
            pos: self.pos
            size: self.size
    Label:
        text: " image displayer ".upper()
        bold: True
        font_size: "50sp"
        size: self.texture_size
        size_hint: [None, None]
        pos_hint: {"top":0.95, "center_x":0.5}
        canvas.before:
            Color:
                rgba: [1,0,0,1]
            Rectangle:
                pos: self.pos
                size: self.size

    Button:
        text: "select an image"
        background_normal: ""
        background_color: [1,0,0,1]
        color: [1,1,1,1]
        size_hint: [0.7, None]
        height: 30
        pos_hint: {"top":0.8, "center_x":0.5}
        on_release:
            app.show_explorer()
    Button:
        id: btn1
        text: "<"
        font_size: "30sp"
        bold: True
        background_normal: ""
        color: [0,0,0,1]
        background_color: [1,0,0,1]
        size_hint: [None, 0.6]
        width: 30
        pos_hint: {"top":0.5, "x":0}
        on_release:
            app.change_image(img.source, -1)

    Image:
        id: img
        source: ""
        allow_stretch: True
        keep_rotio: False
        size_hint: [0.8, 0.5]
        pos_hint: {"top":0.5, "center_x":0.5}
    Button
        id: btn2
        text: ">"
        font_size: "30sp"
        bold: True
        background_normal: ""
        color: [0,0,0,1]
        background_color: [1,0,0,1]
        size_hint: [None, 0.6]
        width: 30
        pos_hint: {"top":0.5, "right":1}
        on_release:
            app.change_image(img.source, 1)
"""

#for fetching the photo
class ExplorerPopup(Popup):
    def __init__(self, **kwargs):
        super(ExplorerPopup, self).__init__(**kwargs)
        self.title = "navigate to the file location"
        self.title_align: "center"
        self.size_hint = [0.7, 0.9]
        self.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        # content
        container = FloatLayout()
        container.add_widget(Explorer(pos_hint={"top": 0.9, "center_x": 0.5}))
        container.add_widget(Button(on_press=self.dismiss, height=10, pos_hint={"top": 0.97, "x": 0.02},
                                    text="X", size_hint=[None, None], size=[20, 30]))
        self.add_widget(container)

#for selecting the photo
class Explorer(FileChooserListView):
    def on_submit(self, selection, touch):
        app.selected(selection)

#finally displaying the image
class MyApp(App):
    def build(self):
        Window.size = [500, 550]
        return Builder.load_string(KV)

    def show_explorer(self):
        explorer_popup = ExplorerPopup()
        explorer_popup.open()

    def selected(self, seletion):
        try:
            image_path = self.format(seletion[0])
            self.add_image(image_path)
        except:
            pass

    def add_image(self, path):
        self.root.ids.img.source = path

#for previewing the other image we can go back
    def change_image(self, img_source, direction):
        parts = img_source.split("/")
        img = parts.pop()
        path = "/".join(parts)
        if os.path.exists(path):
            all_imgs = [x for x in os.listdir(path)]
            current_index = all_imgs.index(img)
            index = current_index + direction
            if index <= 0 or index >= len(all_imgs) - 1:
                self.add_image(path + "/" + all_imgs[current_index])
                self.disable_btn(direction)
            else:
                self.add_image(path + "/" + all_imgs[index])
                self.root.ids.btn1.disabled = False
                self.root.ids.btn2.disabled = False

    def disable_btn(self, d):
        if d == -1:
            self.root.ids.btn1.disabled = True
        else:
            self.root.ids.btn2.disabled = True

    def format(self, path):
        formatted_path = ""
        for char in path:
            if char.isalpha() or char.isnumeric() or char == "." or char == ":":
                formatted_path += char
            else:
                formatted_path += "/"
        return formatted_path


if __name__ == "__main__":
    app = MyApp()
    app.run()