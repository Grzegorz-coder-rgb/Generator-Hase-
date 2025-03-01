import random

znaki = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
all_passwords = []

while True:
    dlugosc_hasla = int(input("Podaj długość hasła: "))
    password = ""
    
    for _ in range(dlugosc_hasla):
        password += random.choice(znaki)

    print("Wygenerowane hasło:", password)

    if input("Dodać do biblioteki? (tak/nie): ") == "tak":
        all_passwords.append(password)
        print(all_passwords)

    if input("Zakończyć? (tak/nie): ") == "tak":
        break
