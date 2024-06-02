# Analiza opinii

## Opis
Prosta aplikacja napisana w języku Python, służąca do analizy tekstowych recenzji lub opinii przechowywanych w pliku tekstowym. Aplikacja przeprowadza tokenizację tekstu i oblicza liczbę wystąpień każdego tokenu oraz wybranych słów kluczowych.

## Zastosowanie
- **Analiza Opinii**: Pozwala na analizę opinii klientów na temat produktów lub usług poprzez identyfikację często używanych słów i wyrażeń.
- **Monitorowanie Wizerunku Marki**: Pomaga w monitorowaniu wizerunku marki poprzez analizę opinii klientów i identyfikację najczęściej występujących terminów.

## Metoda
- **Tokenizacja**: Tekst jest dzielony na pojedyncze słowa (tokeny), usuwane są znaki interpunkcyjne oraz sprowadzane do małych liter.
- **Obliczanie Liczby Wystąpień**: Za pomocą biblioteki Counter obliczana jest liczba wystąpień każdego tokenu oraz słów kluczowych w całym tekście.

## Implementacja
- **Tokenizacja**: Wykorzystuje wyrażenia regularne oraz wbudowane metody Pythona do podziału tekstu na tokeny.
- **Obliczanie Liczby Wystąpień**: Stosuje bibliotekę `collections.Counter` do zliczania wystąpień każdego tokenu i słów kluczowych.

## Problemy z Implementacją
- **Dokładność Analizy**: Metoda może nie uwzględniać kontekstu, co może prowadzić do nieprecyzyjnych wyników, szczególnie w przypadku wieloznacznych słów.
- **Wybór Słów Kluczowych**: Ręczne określenie słów kluczowych może prowadzić do niedoszacowania lub przeszacowania ich znaczenia w analizowanym tekście.
- **Efektywność**: Dla dużych zbiorów danych metoda może być mało efektywna, a przetwarzanie może zająć znaczną ilość czasu.
