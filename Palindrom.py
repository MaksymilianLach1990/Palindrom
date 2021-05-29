# Definicja sprawdzająca czy słowo jest palindromem
def palindrom(name):
    # Potrzebne zmienne
    word = name
    letters = []
    letters_revers = []
    # Przeliteruj słowo
    for letter in word.lower():
        letters.append(letter)
        letters_revers.append(letter)
    # Odwruć słowo
    letters_revers.reverse()
    # Sprawdz rezultat
    if letters == letters_revers:
        score = True
    else:
        score = False
    # Przekaż odpowiedz
    return score


# Rozpocznij zabawę
while True:
    # Przywitaj się
    print("Proszę o podanie słowa do sprawdzenia:")
    # Pobierz słowo od urzytkownika
    check_the_word = input()
    # Wyświetl informacje True \ False
    if palindrom(check_the_word) is True:
        answer = 'jest'
    else:
        answer = 'nie jest'
    print("Twoje słowo: {}, {} palindromem.\nCzy chcesz spróbować jeszcze raz?(Y/N)".format(check_the_word, answer))
    decision = input()
    if decision == 'Y':
        continue
    elif decision == 'N':
        print("Exit")
        break
