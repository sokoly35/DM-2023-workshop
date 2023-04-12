# Warsztaty Dni Matematyki 2023

--- 

Prezentacje z warsztatów możemy znaleźć klikając [tutaj](https://www.canva.com/design/DAFfmY4RnLM/d145zJXNKdvTPe8eAVasLA/view?utm_content=DAFfmY4RnLM&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink)

## Cookiecutter

Cookiecutter to narzędzie do automatycznego strukturyzowania projektu, wykorzystując zdefiniowane szablony. Na początku musimy zainstalować pakiet w wybranym środowisku:

```
pip install --upgrade cookiecutter
```

Skopiowanie struktury jest bardzo proste, wystarczy przejść do lokalizacji, gdzie chcemy wypakować pliki, a następnie wywołać

```
cookiecutter <link_do_schematu>
```

gdzie link kieruje nas do repozytorium z interesującym nas schematem. Na potrzeby warsztatów wystarczy, że wywołamy:

```
cookiecutter https://github.com/sokoly35/applied-math-cookiecutter
```

## Wirtualne środowisko

Wirtualne środowisko założymy z wykorzystanie dystrybucji Anaconda lub Miniconda. Składnia jest następująca:

```
conda create --name <nazwa_środowiska> python=3.9
```
Dobrą praktyką jest uwzględnianie wersji python'a, której chcemy użyć w naszym projekcie. Przykładowo możemy utworzyć środowisko na potrzeby warsztatów

```
conda create --name dm2023 python=3.9
```

Jeśli chcemy aktywować środowisko wywołujemy:

```
conda activate
```

Jeśli chcemy opuścić środowisko wywołujemy:

```
conda deactivate
```

## VS Code

### Rozszerzenia

Do pythona:
- Python,
- Jupyter,
- autoDocstring - Python Docstring Generator,
- isort,
- Pylance - language support,
- Python indent.

Do programowania:
- Markdown Preview Enhanced,
- Better Comments,
- Bracket Pair Color DLW,
- vscode-pets.

### Ustawienia

```json
{
    "python.analysis.typeCheckingMode": "basic",
    "python.formatting.provider": "black",
    "python.languageServer": "Pylance",
    "editor.formatOnSave": true,
    "[python]": {
        "editor.formatOnType": true
    },
    "editor.codeActionsOnSave": {
        "source.organizeImports": true
    },
    "autoDocstring.docstringFormat": "numpy",
}
```

## Profilowanie kodu

### Py-heat

Profilowanie kodu z wykorzystanie py-heat

```
pyheat <ścieżka_do_pliku>
```

### Line-profiler

Profilowanie kodu jest uruchomione z wykorzystaniem

```
kernprof -l <ścieżka_do_pliku>
```

W celu wyświetlenia wyniku analizy wywołaj

```
python -m line_profiler <ścieżka_do_wygenerowanego_pliku_lprof>
```

