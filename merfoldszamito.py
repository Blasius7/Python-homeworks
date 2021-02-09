print("Üdv, ez egy km-t mérföldbe átváltó program :)")

kilos = float(input("Adj meg egy értéket: "))
miles = 1.6
yes = "igen"
no = "nem"

print("Értéked: ", kilos * miles, "mérföld")

while True:
    guess = input("Szeretnéd folytatni? Igen vagy nem? ")

    if guess == no:
        print("Szia, szép napot!")
        break

    elif guess == yes:
        print("Folytassuk")
        kilos = float(input("Adj meg egy értéket: "))
        miles = 1.6
        yes = "igen"
        no = "nem"
        print("Értéked: ", kilos * miles, "mérföld")

    else:
        print("Felelj igennel vagy nemmel!")
