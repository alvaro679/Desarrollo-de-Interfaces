# 🖥 Mi primer Hola Mundo con PySide6

## 📚 Índice

## Índice

- [Contexto](#contexto)
- [Objetivos de aprendizaje](#objetivos-de-aprendizaje)
- [Requisitos previos](#requisitos-previos)
- [Creación y activación del entorno virtual](#creación-y-activación-del-entorno-virtual)
- [Instalación de dependencias](#instalación-de-dependencias)
- [Estructura mínima del proyecto](#estructura-mínima-del-proyecto)
- [Código fuente explicado](#código-fuente-explicado)
- [Ejecución y prueba](#ejecución-y-prueba)
- [Problemas frecuentes](#problemas-frecuentes)
- [Cierre y siguientes pasos](#cierre-y-siguientes-pasos)
- [Checklist del alumno](#checklist-del-alumno)


---

## 📌 Contexto

Este proyecto muestra cómo crear una aplicación de escritorio básica en Python utilizando la librería *PySide6*. Se ha desarrollado en un entorno virtual (venv3) dentro del directorio UAX_26/DI, y se ha estructurado siguiendo buenas prácticas de separación de responsabilidades.

🔗 Enlace al repositorio del proyecto: (añade aquí tu enlace de GitHub)

---

## 🎯 Objetivos de aprendizaje

- Crear y activar un entorno virtual
- Instalar dependencias con pip
- Separar el punto de entrada (main.py) de la clase Ventana
- Comprender QApplication, widgets y el ciclo de eventos (app.exec())

---

## 🧰 Requisitos previos

- *Python*: 3.11
- *Sistema operativo*: Windows 10/11
- *Herramientas*: Git, Visual Studio Code

---

## ⚙ Creación y activación del entorno virtual

bash
# Desde la raíz del proyecto
python -m venv venv3



# Activación en Windows
venv3\Scripts\activate


# Abrir VS Code
code .


## 🧠 Código fuente explicado
Bloques de código de hola_qt.py y importador.py con explicaciones línea por línea. Se aclara el uso de QApplication, QWidget, QLabel, .show() y app.exec().
