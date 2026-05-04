Amount = int(input("Please enter the amount of money:"))
note_1 = Amount//100
note_2 = (Amount % 100)//50
note_3 = ((Amount % 100) % 50)//10
print("Notes of rupees 100:", note_1, "\n")
print("Notes of rupees 50:", note_2, "\n")
print("Notes of rupees 10:", note_3, "\n")
