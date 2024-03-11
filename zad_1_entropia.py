import math

def wczytaj_dane(plik):
    tabela = []
    with open(plik, 'r') as file:
        for line in file:
            rekord = line.strip().split(',')
            tabela.append(rekord)
    return tabela

def oblicz_liczbe_wartosci(atrybut):
    unikalne_wartosci = set(atrybut)
    return len(unikalne_wartosci)

def oblicz_wystapienia(atrybut):
    wystapienia = {}
    for val in atrybut:
        if val in wystapienia:
            wystapienia[val] += 1
        else:
            wystapienia[val] = 1
    return wystapienia

def entropia(atrybut):
    wystapienia = oblicz_wystapienia(atrybut)
    n = sum(wystapienia.values())
    ent = 0
    for wyst in wystapienia.values():
        prawdopodobienstwo = wyst / n
        ent -= prawdopodobienstwo * math.log2(prawdopodobienstwo)
    return ent

def entropia_klasy_decyzyjnej(tabela_decyzyjna):
    klasy_decyzyjne = [rekord[-1] for rekord in tabela_decyzyjna]
    return entropia(klasy_decyzyjne)

def info_atrybutu(indeks_atrybutu, tabela_decyzyjna):
    atrybut = [rekord[indeks_atrybutu] for rekord in tabela_decyzyjna]
    m = oblicz_liczbe_wartosci(atrybut)
    info = 0
    for val in set(atrybut):
        Ti = [rekord[-1] for rekord in tabela_decyzyjna if rekord[indeks_atrybutu] == val]
        info += len(Ti) / len(tabela_decyzyjna) * entropia(Ti)
    return info

def gain(indeks_atrybutu, tabela_decyzyjna):
    info = info_atrybutu(indeks_atrybutu, tabela_decyzyjna)
    return entropia_klasy_decyzyjnej(tabela_decyzyjna) - info

def split_info_atrybutu(indeks_atrybutu, tabela_decyzyjna):
    atrybut = [rekord[indeks_atrybutu] for rekord in tabela_decyzyjna]
    wystapienia = oblicz_wystapienia(atrybut)
    n = len(tabela_decyzyjna)
    split_info = 0
    for wyst in wystapienia.values():
        p_i = wyst / n
        if p_i != 0:
            split_info -= p_i * math.log2(p_i)
    return split_info

def gain_ratio(indeks_atrybutu, tabela_decyzyjna):
    info = info_atrybutu(indeks_atrybutu, tabela_decyzyjna)
    split_info = split_info_atrybutu(indeks_atrybutu, tabela_decyzyjna)
    if split_info == 0:
        return 0
    else:
        return gain(indeks_atrybutu, tabela_decyzyjna) / split_info

def przygotuj_tabele_decyzyjna(plik):
    tabela_decyzyjna = wczytaj_dane(plik)
    return tabela_decyzyjna

def main():
    plik = "test2.txt"
    tabela_decyzyjna = przygotuj_tabele_decyzyjna(plik)

    print("Tabela decyzyjna:")
    for rekord in tabela_decyzyjna:
        print(rekord)

    print("\nLiczba możliwych wartości każdego atrybutu:")
    for i in range(len(tabela_decyzyjna[0]) - 1):
        atrybut = [rekord[i] for rekord in tabela_decyzyjna]
        liczba_wartosci = oblicz_liczbe_wartosci(atrybut)
        print(f"Atrybut {i + 1}: {liczba_wartosci}")

    print("\nWystąpienia każdej wartości każdego atrybutu:")
    for i in range(len(tabela_decyzyjna[0]) - 1):
        atrybut = [rekord[i] for rekord in tabela_decyzyjna]
        wystapienia = oblicz_wystapienia(atrybut)
        print(f"Atrybut {i + 1}: {wystapienia}")

    print("\nEntropia dla każdego atrybutu:")
    for i in range(len(tabela_decyzyjna[0]) - 1):
        atrybut = [rekord[i] for rekord in tabela_decyzyjna]
        ent = entropia(atrybut)
        print(f"Atrybut {i + 1}: {ent}")

    ent_klasy_decyzyjnej = entropia_klasy_decyzyjnej(tabela_decyzyjna)
    print(f"\nEntropia dla klasy decyzyjnej: {ent_klasy_decyzyjnej}")

    print("\nFunkcja informacji dla każdego atrybutu:")
    for i in range(len(tabela_decyzyjna[0]) - 1):
        info = info_atrybutu(i, tabela_decyzyjna)
        print(f"Atrybut {i + 1}: {info}")

    print("\nPrzyrost informacji (Gain) dla każdego atrybutu:")
    for i in range(len(tabela_decyzyjna[0]) - 1):
        gain_value = gain(i, tabela_decyzyjna)
        print(f"Atrybut {i + 1}: {gain_value}")

    print("\nWskaźnik Gain Ratio dla każdego atrybutu:")
    for i in range(len(tabela_decyzyjna[0]) - 1):
        gain_ratio_value = gain_ratio(i, tabela_decyzyjna)
        split_info_value = split_info_atrybutu(i, tabela_decyzyjna)
        print(f"Atrybut {i + 1}: Gain Ratio = {gain_ratio_value}, Split Info = {split_info_value}")


if __name__ == "__main__":
    main()



# Oto ogólne kroki i etapy wyliczania danych, które zostały wykonane w kodzie:
#
# 1. Wczytanie danych: Pierwszym krokiem jest wczytanie danych z pliku tekstowego. Każdy rekord w pliku reprezentuje zestaw danych, z których ostatni element jest etykietą klasy decyzyjnej.
#
# 2. Obliczenie liczby możliwych wartości atrybutów: Dla każdego atrybutu obliczana jest liczba możliwych wartości poprzez znalezienie maksymalnej wartości atrybutu i dodanie 1 (ponieważ wartości atrybutów są liczone od zera).
#
# 3. Obliczenie wystąpień poszczególnych wartości atrybutów: Dla każdego atrybutu obliczana jest liczba wystąpień każdej z możliwych wartości.
#
# 4. Obliczenie entropii: Funkcja entropia oblicza entropię dla danego atrybutu. Entropia mierzy stopień nieporządku lub niepewności w zestawie danych. Im wyższa entropia, tym większy nieporządek.
#
# 5. Obliczenie entropii klasy decyzyjnej: Funkcja entropia_klasy_decyzyjnej oblicza entropię dla klasy decyzyjnej.
#
# 6. Obliczenie informacji dla każdego atrybutu: Funkcja info_atrybutu oblicza ilość informacji dla każdego atrybutu. Jest to suma iloczynów prawdopodobieństw wystąpienia danej wartości atrybutu i entropii podziału na podzbiory dla każdej z tych wartości.
#
# 7. Obliczenie przyrostu informacji (Gain): Funkcja gain oblicza przyrost informacji dla każdego atrybutu. Jest to różnica między entropią klasy decyzyjnej a informacją atrybutu.
#
# 8. Obliczenie współczynnika przyrostu informacji (Gain Ratio): Funkcja gain_ratio oblicza współczynnik przyrostu informacji dla każdego atrybutu. Jest to iloraz przyrostu informacji atrybutu a podziałem informacji atrybutu (split info).
#
# 9. Przygotowanie tabeli decyzyjnej: Dane są przygotowywane do analizy przez usunięcie etykiet klasy decyzyjnej z rekordów i dodanie ich z powrotem po obliczeniach.
#
# 10. Wyświetlenie wyników: Wyniki obliczeń są wyświetlane w celu analizy.

