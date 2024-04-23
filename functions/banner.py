import os
def banner():
    print("*************************************************************")
    print("*              Google Maps Scraper Software 1.0             *")
    print("*             Developer: Avishka Hansana Bandara            *")
    print("*             E-mail: avishkah.bandara@gmail.com            *")
    print("*  Contact: +94 (0) 702096735| Location: Colombo, Sri Lanka *")
    print("*               web:https://www.avishka.online              *")
    print("*         Copyright © 2023-2024.All Right Reserved          *")
    print("*************************************************************")
    print("\n")

def press_enter_to_continue():
    print("Press Enter to continue...")
    input()

def directory(folder_path):
    file_names = os.listdir(folder_path)
    return file_names