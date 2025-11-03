from tkinter import Tk, Button, Label, filedialog, messagebox
from PIL import Image
import os
import webbrowser


class ImageToPDFApp:
    """A simple Interface to convert images into a PDF file."""

    def __init__(self, root):
        self.root = root
        self.root.title("Image to PDF Converter")
        self.root.geometry("420x260")
        self.root.config(bg="#f4f4f4")

        self.files = []

        self.label = Label(
            root,
            text="Upload your images to convert to PDF",
            bg="#f4f4f4",
            font=("Arial", 12)
        )
        self.label.pack(pady=15)

        self.upload_btn = Button(
            root,
            text=" Upload Images",
            command=self.upload_files,
            bg="#4285F4",
            fg="white",
            width=25
        )
        self.upload_btn.pack(pady=10)

        self.convert_btn = Button(
            root,
            text="Convert to PDF",
            command=self.convert_to_pdf,
            bg="#34A853",
            fg="white",
            width=25
        )
        self.convert_btn.pack(pady=10)

    def upload_files(self):
        """Open a file dialog to select image files."""
        self.files = filedialog.askopenfilenames(
            title="Select Images",
            filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
        )

        if self.files:
            messagebox.showinfo("Files Selected", f"{len(self.files)} image(s) selected.")
        else:
            messagebox.showwarning("No File", "Please select at least one image.")

    def convert_to_pdf(self):
        """Convert selected images into a single PDF and open it."""
        if not self.files:
            messagebox.showerror("Error", "No images selected.")
            return

        output_name = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf")],
            title="Save PDF As"
        )

        if output_name:
            images = [Image.open(f).convert("RGB") for f in self.files]
            images[0].save(output_name, save_all=True, append_images=images[1:])

            messagebox.showinfo(
                "Success",
                f" PDF saved successfully!\n\n Location:\n{output_name}"
            )

            # Automatically open the PDF after saving
            try:
                webbrowser.open_new(rf"file://{os.path.abspath(output_name)}")
            except Exception as e:
                messagebox.showwarning(
                    "Open File",
                    f"PDF saved but couldn't open automatically.\nError: {e}"
                )
        else:
            messagebox.showwarning("Cancelled", "Save operation cancelled.")


if __name__ == "__main__":
    root = Tk()
    app = ImageToPDFApp(root)
    root.mainloop()
