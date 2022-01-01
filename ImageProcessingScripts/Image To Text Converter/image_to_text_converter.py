import io
import os
import PySimpleGUI as sg
from PIL import Image
import pytesseract

# include the file types that should be allowed in your app
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
    # the function 'image_to_string' extracts all the text from the image
    text = pytesseract.image_to_string(Image.open(filename))
    return text

# the ui is rendered as a function call and anything defined inside the function is rendered in the window
def main():
    col1 = [[sg.Image(key="-IMAGE-")]]
    col2 = [[
        sg.Text("Image File"),
        sg.Input(size=(25, 1), key="-FILE-"),
        sg.FileBrowse(file_types=file_types),
        sg.Button("Load Image"),
    ]]
    # see the readme for understanding Layout
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
            # if the load image button is clicked
            filename = values["-FILE-"]
            if os.path.exists(filename):
                image = Image.open(values["-FILE-"])
                image.thumbnail((400, 400))
                # convert the image to bytestream
                bio = io.BytesIO()
                # save the image as PNG
                image.save(bio, format="PNG")
                # update the ui to show the loaded image
                window["-IMAGE-"].update(data=bio.getvalue())
        if event == "Load Text":
            # The image is taken and its file path is passed into the ocr_core() function
            filename = values["-FILE-"]
            if os.path.exists(filename):
                # update the text based on the returned value of the function
                window["-TEXTBOX-"].update(ocr_core(filename))

    window.close()


if __name__ == "__main__":
    main()
