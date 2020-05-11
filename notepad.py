"""
notepad.py: a simple tkinter notepad app
"""

import tkinter

class GUI:
     """ Notepad app GUI class object."""

     def __init__(self, root_object):
          self.root = root.object
          self.root.columnconfigure(0, weight=1)
          self.root.rowconfigure(0, weight=1)

          self.main_frame = tkinter.Frame(self.root, background="blue")
          self.main_frame.grid(column=0, row=0, sticky=('N', 'S', 'E', 'W'))

          self.main_frame.columnconfigure(0, weight=1)
          self.main_frame.rowconfigure(1, weight=0)

          self.main_frame.rowconfigure(3, weight=0)
          self.open_button=tkinter.Button(self.main_frame,
                                          text="Open File",
                                          command=self.openButtonPressed)
          self.open_button.grid(row=3, column=0, sticky=('E', 'W'))

          self.save_button = tkinter.Button(self.main_frame,
                                            text = "Save File",
                                            command=self.saveButtonPressed)
          self.save_button_grid(row=2, column=0, sticky=('E', 'W'))
          
          self.clear_button = tkinter.Button(self.main_frame,
                                             text="Clear Text",
                                             command=self.clearButtonPressed)
          self.clear_button.grid(row=1, column=0, sticky=('E', 'W'))

          self.text_area = tkinter.Text(self.main_frame, height=15, width=40)
          self.text_area.grid(row=0, column=0, sticky=('N', 'S', 'E', 'W'))

     def openButtonPressed(self):
          print("Open button pressed.")
          from tkinter import filedialog
          file_name = filedialog.askopenfilename()
          with open(file_name, 'r') as f:
               content = f.read()
          self.text_area.insert('1.0', content)

     def saveButtonPressed(self):
          print("Save Button pressed.")
          content = self.text_area.get('1.0', 'end')
          print(content)

          from tkinter import filedialog
          self.filePath = filedialog.asksaveasfile(title="FILE DIALOG")
          self.filePath.write(content)
          self.filePath.close()

     def clearButtonPressed(self):
          print("Clear button pressed.")
          self.text_area_delete('1.0', 'end')

root = tkinter.Tk()
root.title("Python Notepad")
root.mainloop()
