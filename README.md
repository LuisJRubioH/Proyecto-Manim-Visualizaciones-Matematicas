# Proyecto Manim – Visualizaciones Matemáticas

Este repositorio contiene animaciones matemáticas desarrolladas con **Manim (Mathematical Animation Engine)**, orientadas a docencia universitaria y divulgación matemática.

Página oficial de Manim (Community Edition):  
https://www.manim.community/

---

## Objetivo

Proveer escenas matemáticas claras, reutilizables y bien estructuradas para ilustrar conceptos de:

- Álgebra lineal
- Cálculo diferencial e integral
- Geometría
- Otros temas de matemáticas superiores

## Requisitos

- Python ≥ 3.9
- Manim Community Edition

Instalación de dependencias:

```sh
pip install -r requirements.txt
```

## Uso básico
Renderizar una escena:

```sh
manim -pql scenes/intro.py IntroScene
```

## Estructura del repositorio
manim-proyecto/
├── README.md
├── LICENSE
├── pyproject.toml
├── requirements.txt
├── .gitignore
├── scenes/
│   ├── __init__.py
│   ├── algebra/
│   │   ├── __init__.py
│   │   └── vectores.py
│   ├── calculo/
│   │   ├── __init__.py
│   │   └── limites.py
│   ├── geometria/
│   │   ├── __init__.py
│   │   └── triangulos.py
│   └── intro.py
├── assets/
│   ├── images/
│   ├── svg/
│   └── fonts/
├── media/
│   └── .gitkeep
├── scripts/
│   └── render.sh
└── docs/
    └── ejemplos.md
