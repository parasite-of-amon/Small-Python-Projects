import customtkinter 
import tkinter
from PIL import Image
import os

class MainApplication(customtkinter.CTk):
   width = 400
   height = 400

   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)

      self.title("Master Key")
      self.geometry(f"{self.width}x{self.height}")
      self.resizable(False, False)
      self.current_path = os.path.dirname(os.path.realpath(__file__))

      current_path = os.path.dirname(os.path.realpath(__file__))

      self.bg_image = customtkinter.CTkImage(Image.open(r"D:\# Python Projects\CustomTkinter-master\examples\test_images\bg_gradient.jpg"),size=(self.width, self.height))
      self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image)
      self.bg_image_label.grid(row=0, column=0)

      self.login_frame = customtkinter.CTkFrame(self, corner_radius=0)
      self.login_frame.grid(row=0, column=0, sticky="ns")
      
      self.main_canvas = tkinter.Canvas(self.login_frame, height=200, width=200)
      self.main_image = tkinter.PhotoImage(Image.open(r"D:\# Python Projects\CustomTkinter-master\examples\test_images\bg_gradient.jpg"))
      self.main_canvas.create_image(0, 0, anchor="nw", image=self.main_image)

      self.login_label = customtkinter.CTkLabel(self.login_frame, text="Login Page",font=customtkinter.CTkFont(size=20, weight="bold"))
      self.login_label.grid(row=1, column=0, padx=30, pady=(150, 15))
      self.username_entry = customtkinter.CTkEntry(self.login_frame, width=200, placeholder_text="Username")
      self.username_entry.grid(row=2, column=0, padx=30, pady=(15, 15))
      self.password_entry = customtkinter.CTkEntry(self.login_frame, width=200, show="*", placeholder_text="Passowrd")
      self.password_entry.grid(row=3, column=0, padx=30, pady=(0, 15))
      self.login_button = customtkinter.CTkButton(self.login_frame, text="Login", width=200)
      self.login_button.grid(row=4, column=0, padx=30, pady=(15, 15))



if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
