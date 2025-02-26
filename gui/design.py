# ====================================
# © Paul Hinterbauer 2025 @ TGM Vienna

# ./gui/design.py
# Design for the GUI
# ====================================

import customtkinter as cTk

RUNNING_AS_MAIN = False

class StartWindow(cTk.CTk):
    def __init__(self, open_main_window, confirm_player_name):
        """
        Create the start window
        """
        super().__init__()
        self.player_name = ""

        self.title("The Flying Humpty - Main Menu - © Paul Hinterbauer 2025 @ TGM Vienna")
        self.geometry("720x320")

        self.player_name_entry = cTk.CTkEntry(self, placeholder_text="Enter your name")
        self.player_name_entry.place(relx=0.5, rely=0.5, anchor="center")

        self.confirm_player_name_btn = cTk.CTkButton(self, text="Confirm Name", command=lambda: confirm_player_name(self, RUNNING_AS_MAIN))
        self.confirm_player_name_btn.place(relx=0.5, rely=0.6, anchor="center")

        self.open_main_btn = cTk.CTkButton(self, text="Start", command=lambda: open_main_window(self))
        self.open_main_btn.place(relx=0.5, rely=0.7, anchor="center")

class MainWindow(cTk.CTkToplevel):
    def __init__(self, master, open_inventory, open_start_menu):
        """
        Create the main window
        """
        super().__init__(master)
        self.player_name = master.player_name

        self.title(f"{master.player_name}'s adventure among the Flying Humpty - © Paul Hinterbauer 2025 @ TGM Vienna")
        self.geometry("1280x720")

        self.open_inventory_btn = cTk.CTkButton(self, text="Inventory", command=lambda: open_inventory(self))
        self.open_inventory_btn.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=10)

        self.open_menu_btn = cTk.CTkButton(self, text="Menu", command=lambda: open_start_menu(self))
        self.open_menu_btn.place(relx=0.0, rely=0.0, anchor="nw", x=10, y=10)

class InventoryWindow(cTk.CTkToplevel):
    def __init__(self, master, close_inventory):
        """
        Create the inventory window
        """
        super().__init__(master)
        self.player_name = master.player_name

        self.title(f"{self.player_name}'s Inventory - © Paul Hinterbauer 2025 @ TGM Vienna")
        self.geometry("800x600")

        self.close_inventory_btn = cTk.CTkButton(self, text="Close", command=lambda: close_inventory(self))
        self.close_inventory_btn.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=10)

if __name__ == "__main__":
    from interaction import open_main_window, confirm_player_name
    RUNNING_AS_MAIN = True
    root = StartWindow(open_main_window, confirm_player_name)
    root.player_name = "<THIS IS RUNNING IN 'design.py' NOT 'main.py'>"
    root.mainloop()