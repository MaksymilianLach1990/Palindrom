# Definicja sprawdzająca czy słowo jest palindromem
while True:
    # Pobierz słowo od urzytkownika
    word = input()
    letters = []
    letters_revers = []
    answer = None
    # Przeliteruj słowo
    for letter in word.lower():
        letters.append(letter)
        letters_revers.append(letter)

    # Sprawd z liczbę liter
    number_of_letters = len(letters)

    # Stwórz liste i ją odwruć
    letters_revers.reverse()

    # Sprawdz czy listy są sobie równe
    if letters == letters_revers:
        answer = "jest"
    else:
        answer = "nie jest"
    # Wyświetl informacje True \ False
    if number_of_letters % 2 != 0:
        answer = "nie jest"
    print("Twoje słowo: {}, {} palindromem.\nCzy chcesz spróbować jeszcze raz?(Y/N)".format(word, answer))
    decision = input()
    if decision == 'Y':
        continue
    elif decision == 'N':
        break