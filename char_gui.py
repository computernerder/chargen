import customtkinter as ctk
from constants import CharacterConstants as cc



class Character:
    def __init__(self, attributes):
        if not isinstance(attributes, list):
            raise ValueError("Attributes must be a list")
        self.attributes = attributes
        
 



class CharGui(ctk.CTk):
    frames = {}
    current = None
    bg = ""


    def __init__(self):
        super().__init__()
        self.title("Character Creator")
        self.geometry("800x800")

        print(self.attributes)
        print(cc.attributes)
        print(self.skills)
        print(cc.skills)
        print(self.biographics)
        print(cc.biographics)

        
        # Row Configuration
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        #Column Configuration
        self.columnconfigure(0, weight=1)   
        self.columnconfigure(1, weight=1)

        #Create Widgets
        self.create_widgets()




    #  header
    #  ------------------ 
    #
    #

    def create_widgets(self):
        self.header = ctk.CTkLabel(self, text="Character Creator",font=("Arial", 48), fg_color="blue")
        self.header.grid(row=0, column=0, sticky= "new", columnspan=2)
        self.attribute_frame()
        self.create_skills()
        self.create_buttons()

    def create_buttons(self):
        self.button_frame = ctk.CTkFrame(self, width=400, height=400)
        self.button_frame.grid(row=2, column=0, columnspan=2)

        self.change_frame = ctk.CTkButton(self.button_frame, text="Change Frame", command=self.change_frame)
        self.change_frame.grid(row=0, column=0)

        self.restore_frame = ctk.CTkButton(self.button_frame, text="Restore Frame", command=self.restore_frame)
        self.restore_frame.grid(row=0, column=1)

    def change_frame(self):
        self.attributes_frame.tkraise()

    def restore_frame(self):
        self.skills_frame.tkraise()



    def create_skills(self):
        self.skills_frame = ctk.CTkFrame(self, width=400, height=400)
        self.skills_frame.grid(row=1, column=1, sticky="nesw")

        for index, each in enumerate(self.skills):
            self.skill_label = ctk.CTkLabel(self.skills_frame, text=each)
            self.skill_label.grid(row=index+1, column=0)

            self.skill_entry = ctk.CTkEntry(self.skills_frame)
            self.skill_entry.grid(row=index+1, column=1)

    def attribute_frame(self):

        self.attributes_frame = ctk.CTkFrame(self, width=400, height=400)
        self.attributes_frame.grid(row=1, column=1, sticky="nesw")

        for index, each in enumerate(self.attributes):
            self.name_label = ctk.CTkLabel(self.attributes_frame, text=each)
            self.name_label.grid(row=index+1, column=0)

            self.name_entry = ctk.CTkEntry(self.attributes_frame)
            self.name_entry.grid(row=index+1, column=1)






if __name__ == "__main__":

    fred = Character(cc.attributes)
    print(fred)
    app = CharGui()
    app.mainloop()