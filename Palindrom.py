# Definicja sprawdzająca czy słowo jest palindromem

# Pobierz słowo od urzytkownika
word = input()
print(word)
letters = []
letters_revers = []
answer = None
# Przeliteruj słowo
for letter in word.lower():
    letters.append(letter)
    letters_revers.append(letter)
print(letters)
# Sprawdz liczbę liter
number_of_letters = len(letters)
print(number_of_letters)
# Stwórz liste i ją odwruć
letters_revers.reverse()
print(letters_revers)
# Sprawdz czy listy są sobie równe
if letters == letters_revers:
    answer = "jest"
else:
    answer = "nie jest"
# Wyświetl informacje True \ False
print("Twoje słowo: {}, {} palindromem.\nCzy chcesz spróbować jeszcze raz?(Y/N)".format(word, answer))