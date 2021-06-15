import pywhatkit as kit
try:
    user_image = r"C:\Users\Dell\Downloads\LGM.png"
    output_image = r"C:\Users\Dell\Downloads\Output.txt"
    kit.image_to_ascii_art(user_image, output_image)
except:
    print("No result found")
