import customtkinter as ctk




class Character:
    def __init__(self, attributes):
        if not isinstance(attributes, list):
            raise ValueError("Attributes must be a list")
        self.attributes = attributes
        
 



class CharGui(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Character Creator")
        self.geometry("400x400")
        self.attributes = ['Strength','Intelligence','Wisdom','Dexterity','Constitution','Charisma', 'Luck', 'Agility', 'Perception']
        
        self.rowconfigure(0, weight=4)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        

        self.columnconfigure(0, weight=1)   
        self.columnconfigure(1, weight=1)

        self.create_widgets()
        self.progress = ctk.CTkProgressBar(self, width=400, height=20)
        self.progress.grid(row=1, column=0)

        # Progress Buttons
        self.progressup_buttt = ctk.CTkButton(self, text="Progress", command=self.progress_up)
        self.progressup_buttt.grid(row=2, column=0)

        self.progressdown_buttt = ctk.CTkButton(self, text="Progress Down", command=self.progress_down)
        self.progressdown_buttt.grid(row=2, column=1)

    def progress_up(self):
        self.progress.step()
        self.progress.update()
        print(self.progress.get())
    
    def progress_down(self):
        self.progress.step()
        self.progress.update()
        print(self.progress.get())
        


    def create_widgets(self):
        
        self.attribute_frame()
        



    def attribute_frame(self):

        self.attributes_frame = ctk.CTkFrame(self, width=400, height=400)
        self.attributes_frame.grid(row=0, column=0)

        for index, each in enumerate(self.attributes):
            self.name_label = ctk.CTkLabel(self.attributes_frame, text=each)
            self.name_label.grid(row=index, column=0)

            self.name_entry = ctk.CTkEntry(self.attributes_frame)
            self.name_entry.grid(row=index, column=1)






if __name__ == "__main__":
    app = CharGui()
    app.mainloop()