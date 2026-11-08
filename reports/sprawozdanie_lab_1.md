### Wstępna analiza i przygotowanie danych

Dane zostały zaimportowane z arkusza Excel za pomocą biblioteki `pandas`. Po wczytaniu zbiór zawierał 21 wierszy oraz 5 zmiennych: rok, przychód, zysk, zatrudnienie i liczbę użytkowników.

W pierwszym etapie przeprowadzono kontrolę jakości danych. Zidentyfikowano dodatkowy wiersz zawierający informację o źródłach danych oraz pusty wiersz dotyczący roku 2026. Wiersze te nie stanowią właściwych obserwacji i zostały usunięte.

Stwierdzono również występowanie brakujących wartości w zmiennej `users`. Braki dotyczą lat 2007, 2008, 2024 i 2025. Nie usunięto tych obserwacji, ponieważ pozostałe zmienne zawierają dostępne dane, które mogą być wykorzystane w dalszej analizie.

Po wstępnym oczyszczeniu zbiór obejmuje 19 obserwacji z lat 2007–2025.
