import random
attempts = 0
end_num = [5,15,50]
while True:
    difficulty = input("Milyen nehézségi fokon játszanád a játékot? \n (Könnyű, közepes vagy nehéz):  \n")
    if difficulty == "könnyű":
        end_num = 5
        break
    elif difficulty == "közepes":
        end_num = 15
        break
    elif difficulty == "nehéz":
        end_num = 50
        break
    else:
        print("Nem jó, adj meg egy nehézségi fokozatot!")
secret = random.randint(1, end_num)
with open("score.txt", "r") as score_file:
        best_score = int(score_file.read())
        print("Top score: " + str(best_score))
while True:
    guess = int(input("Találd ki a titkos számot 1 és " + str(end_num) + "között "))
    attempts += 1
    if guess == secret:
        print("Gratulálok, kitaláltad! Ez a szám: " + str(secret))
        print("Kísérletek száma: " + str(attempts))
        if best_score > attempts:
            with open("score.txt", "w") as score_file:
                score_file.write(str(attempts))
        break
    elif guess > secret:
        print("Próbáld kisebbel")
        print("Kísérletek száma: " + str(attempts))
    elif guess < secret:
        print("Próbáld nagyobbal")
        print("Kísérletek száma: " + str(attempts))