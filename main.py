import random
import time


password_characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

while True:
    # Pytamy użytkownika o długość hasła
    try:
        password_length = int(input("Enter the password length (min 6): "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue  # Jeśli użytkownik poda coś, co nie jest liczbą, zaczynamy od nowa
    
    # Sprawdzanie, czy długość hasła jest większa lub równa 6
    if password_length < 6:
        print("Password length must be at least 6 characters!")
        continue  # Jeśli długość hasła jest za mała, ponownie pytamy o długość
    
    password = ""  # Inicjalizujemy pustą zmienną na hasło
    print("Generating password...")
    
    # Generowanie hasła
    for i in range(password_length):
        generate = random.choice(password_characters)
        password += generate
    
    # Opóźnienie, aby dodać efekt generowania
    time.sleep(1)
    
    # Wyświetlenie wygenerowanego hasła
    print("Generated password:", password)
    
    # Pytanie, czy użytkownik chce zapisać hasło do pliku
    appending_password = input("Do you want to save the password to a file? (yes/no): ").strip().lower()
    
    if appending_password == "yes":
        # Otwarcie pliku do zapisu
        with open("password.txt", "a") as file:
            file.write(password + "\n")
        print("Password saved to password.txt")
    elif appending_password == "no":
        print("Password not saved.")
    else:
        print("Invalid input! Password not saved.")
    
    # Opcja zakończenia pętli po wygenerowaniu hasła
    end = input("Do you want to generate another password? (yes/no): ").strip().lower()
    if end == "no":
        break
    elif end != "yes":
        print("Invalid input! Exiting the program.")
        breakimport random
import time


password_characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

while True:
    # Pytamy użytkownika o długość hasła
    try:
        password_length = int(input("Enter the password length (min 6): "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue  # Jeśli użytkownik poda coś, co nie jest liczbą, zaczynamy od nowa
    
    # Sprawdzanie, czy długość hasła jest większa lub równa 6
    if password_length < 6:
        print("Password length must be at least 6 characters!")
        continue  # Jeśli długość hasła jest za mała, ponownie pytamy o długość
    
    password = ""  # Inicjalizujemy pustą zmienną na hasło
    print("Generating password...")
    
    # Generowanie hasła
    for i in range(password_length):
        generate = random.choice(password_characters)
        password += generate
    
    # Opóźnienie, aby dodać efekt generowania
    time.sleep(1)
    
    # Wyświetlenie wygenerowanego hasła
    print("Generated password:", password)
    
    # Pytanie, czy użytkownik chce zapisać hasło do pliku
    appending_password = input("Do you want to save the password to a file? (yes/no): ").strip().lower()
    
    if appending_password == "yes":
        # Otwarcie pliku do zapisu
        with open("password.txt", "a") as file:
            file.write(password + "\n")
        print("Password saved to password.txt")
    elif appending_password == "no":
        print("Password not saved.")
    else:
        print("Invalid input! Password not saved.")
    
    # Opcja zakończenia pętli po wygenerowaniu hasła
    end = input("Do you want to generate another password? (yes/no): ").strip().lower()
    if end == "no":
        break
    elif end != "yes":
        print("Invalid input! Exiting the program.")
        break
