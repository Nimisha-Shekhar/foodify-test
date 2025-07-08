import json
def load_menu(filepath="menu.json"):
    try:
        with open(filepath,'r') as file:
            menu=json.load(file)
            return menu
    except FileNotFoundError:
        print(f"Error:The File {filepath} is not found.")
        return{}
def display_menu(menu_data):
    for category, items in menu_data.items():
        print(f"{category}")
        for item in items:
            print(f"{item['Name']}: ₹ {item['Price']}")
if __name__=="__main__":
    menu=load_menu()
    if menu:
        display_menu(menu)


    
