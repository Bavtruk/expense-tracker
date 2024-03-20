#   _____                                       _____               _             
#  | ____|_  ___ __   ___ _ __  ___  ___  ___  |_   _| __ __ _  ___| | _____ _ __ 
#  |  _| \ \/ / '_ \ / _ \ '_ \/ __|/ _ \/ __|   | || '__/ _` |/ __| |/ / _ \ '__|
#  | |___ >  <| |_) |  __/ | | \__ \  __/\__ \   | || | | (_| | (__|   <  __/ |   
#  |_____/_/\_\ .__/ \___|_| |_|___/\___||___/   |_||_|  \__,_|\___|_|\_\___|_|   
#             |_|                                                                 

#
# Uzdevums:
# Uzrakstīt programmu, kas ļauj
# - ievadīt izdevumus: nosaukumu, summu un kategoriju
# - atspoguļot uz ekrāna visus izdevumus
# iespēja atlasīt 10 lielākus izdevumus  
 #- iespēja atlasīt 10 mazākus izdevumus
 #- iespēja apskatīt vidējo izdevumu summu 
# [!] Programmai jaglabā izdevumu stāvokli kad programma ir izslēgta palaista no jauna
#

expenses = []
import json
# load expenses from expenses.json file here
# https://www.geeksforgeeks.org/read-write-and-parse-json-using-python/ (Python read JSON file)
pass

while True:
    command = input("\nChoose command:")
    if command == "1":
        print("Uz ko patereji")
        nosaukums = input("nosaukums")
        summa = input("summa")
        kategorija = input("kategorija")
        izdevumi = {"nosaukums" : nosaukums, "summa" : summa,  "kategorija" : kategorija}
        expenses.append(izdevumi)
        pass
    if command == "2":
        expenses.append(izdevumi)
        with open("sample.json", "w") as outfile:
            json.dump(expenses, outfile)
        pass
    if command == "e":
        print("Exiting...")
        break

# save expenses to expenses.json file here
# https://www.geeksforgeeks.org/read-write-and-parse-json-using-python/ (Writing JSON to a file in Python)
pass

