# CHANGELOG - Hakerklojs Visionary Marketing

## [Wersja 0.1.0] - Pierwsze wydanie (Initial Setup)

### Dodano
- **Konfiguracja środowiskowa**:
  - Stworzono plik `.env` do przechowywania zmiennych środowiskowych, takich jak:
    - `DATABASE_URL` - konfiguracja połączenia z bazą danych PostgreSQL.
    - `DEBUG` - ustawienie trybu debugowania na `True` w środowisku deweloperskim.
    - `SECRET_KEY` - unikalny klucz bezpieczeństwa do zabezpieczenia aplikacji.
  
- **Baza danych**:
  - Utworzono bazę danych `hakerklojs_database` na lokalnym serwerze PostgreSQL.
  - Skonfigurowano połączenie do bazy danych PostgreSQL przez zmienną `DATABASE_URL`.

- **Struktura plików projektu**:
  - Przygotowano podstawową strukturę katalogów dla projektu:
    - **app.py** - Główny plik aplikacji.
    - **config/** - Pliki konfiguracyjne dla różnych środowisk (`development`, `production`, `testing`).
    - **database/** - Pliki bazy danych oraz skrypty migracyjne.
    - **cms/** - Moduły CMS do zarządzania treścią przez użytkowników.
    - **scss/** - Pliki SCSS dla stylów front-endowych:
      - **scss/base/** - Podstawowe style i zmienne.
      - **scss/components/** - Style komponentów.
      - **scss/layouts/** - Układy strony, np. nagłówek, stopka.
    - **static/** - Zasoby statyczne:
      - **static/css/** - Wygenerowane pliki CSS.
      - **static/js/** - Skrypty JavaScript.
      - **static/images/** - Obrazy, np. logotypy i tła.
    - **templates/** - Szablony HTML w Jinja2:
      - **templates/layouts/** - Główne szablony struktury strony (np. `base.html`).
      - **templates/prp_exhaust/** - Sekcja dedykowana partnerowi PRP-Exhaust.
      - **templates/pages/** - Szablony stron ogólnych, np. “O nas”, “Kontakt”.
    - **tests/** - Testy jednostkowe i integracyjne dla projektu:
      - **test_app.py** - Testy aplikacji.
      - **test_config.py** - Testy konfiguracji.
      - **test_routes.py** - Testy tras i routingu.
    - **ux_ui/** - Dokumentacja UX/UI, makiety, prototypy oraz specyfikacje designu.
    - **.env** - Plik z wrażliwymi zmiennymi środowiskowymi.
    - **requirements.txt** - Lista pakietów i zależności projektu.

- **Podstawowe zasady ochrony**:
  - Plik `.env` dodany do `.gitignore` w celu ochrony poufnych danych przed przesłaniem do repozytorium.

### Uwagi
- Obecna wersja skupia się na konfiguracji podstawowych plików, struktury projektu oraz połączenia z bazą danych. Kolejne wersje będą rozszerzać funkcjonalność i zawierać dodatkowe komponenty oraz testy.
- W przyszłości planowane jest dodanie modułów funkcjonalnych, takich jak szablony, style SCSS oraz testy jednostkowe dla kluczowych komponentów aplikacji.

---