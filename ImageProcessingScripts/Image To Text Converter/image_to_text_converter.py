import io
import os
import PySimpleGUI as sg
from PIL import Image
import pytesseract

file_types = [
    ("PNG (*.png)", "*.png"),
    ("JPEG (*.jpg)", "*.jpg"),
    ("All files (*.*)", "*.*")
]


def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    pytesseract.pytesseract.tesseract_cmd = r'<Put your tessract-ocr exe path here>'
    text = pytesseract.image_to_string(Image.open(filename))
    return text


def main():
    col1 = [[sg.Image(key="-IMAGE-")]]
    col2 = [[
        sg.Text("Image File"),
        sg.Input(size=(25, 1), key="-FILE-"),
        sg.FileBrowse(file_types=file_types),
        sg.Button("Load Image"),
    ]]
    layout = [[
        sg.Column(col1, element_justification='c'),
        sg.Column(col2, element_justification='c'),
        [
            sg.Button("Load Text"),
            sg.Multiline(size=(100, 10), key="-TEXTBOX-")
        ]
    ]]

    window = sg.Window("Image 2 Text", layout, margins=(
        50, 50), size=(1000, 500), resizable=True)

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "Load Image":
            filename = values["-FILE-"]
            if os.path.exists(filename):
                image = Image.open(values["-FILE-"])
                image.thumbnail((400, 400))
                bio = io.BytesIO()
                image.save(bio, format="PNG")
                window["-IMAGE-"].update(data=bio.getvalue())
        if event == "Load Text":
            filename = values["-FILE-"]
            if os.path.exists(filename):
                window["-TEXTBOX-"].update(ocr_core(filename))

    window.close()


if __name__ == "__main__":
    main()
