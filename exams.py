from pystyle import Write, Colors
import os
import time
import pyphisher
time.sleep(2)
print('''___________________________________''')
print()
os.system("figlet exams | lolcat")
print()
print('''___________________________________''')
print()
Write.Print(f"coded by hackertool", Colors.red_to_blue, interval=0.05)
print()
Write.Print(f"this program for calculating grade student", Colors.red_to_blue, interval=0.05)
print()
math = input("type your math grade : ")
E = input("type your English grade : ")
A = input("type your arabic grade : ")
h = input("type your history grade : ")
i = input("type your islamy grade : ")
s = input("type your science grade : ")
your_final = "the result of your final exams is"
logic = float(math) + float(E) + float(A) + float(h) + float(i) + float(s) / 100
print(Colors.purple + your_final +" "+ str(logic))
