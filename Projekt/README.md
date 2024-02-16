#### Moduł `tictactoe`

##### Kluczowe zmienne:
- `X`: Stała reprezentująca gracza X.
- `O`: Stała reprezentująca gracza O.
- `EMPTY`: Stała reprezentująca puste pole na planszy.
- `BOARD_SIZE`: Stała reprezentująca rozmiar planszy (3x3).
- `X_WIN`: Stała reprezentująca wynik wygranej dla gracza X.
- `O_WIN`: Stała reprezentująca wynik wygranej dla gracza O.
- `DRAW`: Stała reprezentująca remis.

##### Funkcje:

`initial_state()`
    - Zwraca początkowy stan planszy (pustą planszę).

`player(board)`
    - Zwraca gracza, który ma kolejny ruch na planszy.

`actions(board)`
    - Zwraca zbiór wszystkich możliwych ruchów dostępnych na planszy.

`result(board, action)`
    - Zwraca planszę, która wynika z wykonania ruchu (i, j) na planszy.

`winner(board)`
    - Zwraca zwycięzcę gry, jeśli taki istnieje.

`terminal(board)`
    - Zwraca True, jeśli gra się skończyła, False w przeciwnym razie.

`utility(board)`
    - Zwraca 1, jeśli gracz X wygrał grę, -1 jeśli gracz O wygrał, 0 w przeciwnym razie.

`minimax(board)`
    - Zwraca optymalny ruch dla bieżącego gracza na planszy.

`max_value(board)`
    - Pomocnicza funkcja dla algorytmu minimax, oblicza wartość maksymalną.

`min_value(board)`
    - Pomocnicza funkcja dla algorytmu minimax, oblicza wartość minimalną.

#### Funkcja `minimax(board)`

- **Opis:** Funkcja implementuje algorytm minimax, który służy do znalezienia optymalnego ruchu dla bieżącego gracza na planszy w grze w kółko i krzyżyk. Algorytm przeszukuje drzewo gry, aby znaleźć najlepszy ruch dla danego gracza.

- **Parametry:**
  - `board`: Aktualny stan planszy gry.

- **Zwracane wartości:**
  - Zwraca najlepszy ruch dla bieżącego gracza na podstawie analizy drzewa gry.

- **Algorytm:**
  - Funkcja `minimax()` przeszukuje drzewo gry rekurencyjnie, aby znaleźć optymalny ruch.
  - Jeśli gracz to X, funkcja próbuje maksymalizować wynik, szukając ruchu, który zapewni najwyższy możliwy wynik.
  - Jeśli gracz to O, funkcja próbuje zminimalizować wynik, szukając ruchu, który zapewni najniższy możliwy wynik.
  - Algorytm korzysta z dwóch pomocniczych funkcji: `max_value()` i `min_value()`, które obliczają odpowiednio wartość maksymalną i minimalną dla danego stanu gry.

#### Moduł `runner`

- Odpowiada za interakcję z graczem, logikę gry oraz jej wyświetlanie w interfejsie graficznym przy użyciu biblioteki Pygame.
