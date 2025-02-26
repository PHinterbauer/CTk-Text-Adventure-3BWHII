# ====================================
# © Paul Hinterbauer 2025 @ TGM Vienna

# ./gui/interaction.py
# Interacting with the GUI
# ====================================

try:
    from gui.design import MainWindow, InventoryWindow
except ImportError:
    from design import MainWindow, InventoryWindow

def open_main_window(start_window_instance):
    start_window_instance.withdraw()
    MainWindow(start_window_instance, open_inventory, open_start_menu)

def open_start_menu(main_window_instance):
    main_window_instance.master.deiconify()
    main_window_instance.destroy()

def open_inventory(main_window_instance):
    main_window_instance.withdraw()
    InventoryWindow(main_window_instance, close_inventory)

def close_inventory(inventory_window_instance):
    inventory_window_instance.master.deiconify()
    inventory_window_instance.destroy()

def confirm_player_name(start_window_instance, running_main):
    start_window_instance.player_name = start_window_instance.player_name_entry.get()
    if running_main:
        start_window_instance.player_name = "<THIS IS RUNNING IN 'design.py' NOT 'main.py'>"