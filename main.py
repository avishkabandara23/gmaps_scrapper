import scrapmaps
import populer_time
import os
import DataVisualization
from functions import banner

banner.banner()
while True:
    print (" 1. Gather Data From Google Maps.\n 2. Analize Populer Times.\n 3. Visualize Populer Times.\n 0. Exit\n ")
    value = int(input("Enter Your Value: "))
    if value == 1:
        link = input("Enter Your Google Map's Link: ")
        print("Sending Data....")
        result = scrapmaps.scraper(link)
        print(result)
        banner.press_enter_to_continue()
        os.system('cls')
        banner.banner()
    elif value == 2:
        print("Available Dataset in the Directory\n")
        #scan Direcrtory
        folder_path = "datasets/"
        file_names = banner.directory(folder_path)
        print(file_names)
        print("\n")
        location = input("Enter file Name want to Analize or press Enter to Quit:  ")
        if not location:
            break
        else:
            print("Data Analizing...\n")
            print("*********************************************************************")
            result = populer_time.analize(location)
            print(result)
            banner.press_enter_to_continue()
            os.system('cls')
            banner.banner()
    elif value == 3:
        print("Available Dataset in the Directory\n")
        #scan Direcrtory
        folder_path = "csv/"
        file_names = banner.directory(folder_path)
        print(file_names)
        print("\n")
        location = input("Enter CSV(.csv) File want to Visuzlizing or press Enter to Quit: ")
        if not location:
            break
        else:
            print("Data Visuzlizing...\n")
            result = DataVisualization.visualize(location)
    elif value == 0:
        os.system('cls')
        break