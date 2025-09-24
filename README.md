# 📌 FichaGenerator Bot

Un bot de Discord hecho con [Pycord](https://docs.pycord.dev) que genera una **ficha personalizada** con tu información en formato de imagen con estética de Stardew Valley. 🎨

<img width="800" height="500" alt="image" src="https://github.com/user-attachments/assets/b5fafd74-de01-4168-9f29-7498f98f9a44" />


## 🚀 Funcionalidades

* Slash command `/ficha` para crear una ficha con tus datos.
* Calcula automáticamente tu edad a partir de tu cumpleaños.
* Inserta tu avatar de Discord en la ficha.
* Personalizable con campos opcionales como *anime favorito* y hasta *diámetro de muslos (?)*.

## 🛠️ Requisitos

* Python **3.10+** (probado en 3.11 / 3.12 / 3.13).
* Una cuenta de Discord con un **bot token** válido.
* Dependencias (ver abajo).

## 📦 Instalación

Clona el repo y entra a la carpeta:

```bash
git clone https://github.com/TU_USUARIO/FichaGenerator.git
cd FichaGenerator
```

Instala dependencias:

```bash
pip install -r requirements.txt
```

Crea un archivo `.env` en la raíz del proyecto con tu token:

```
DISCORD_TOKEN=tu_token_aquí
```

## ▶️ Uso

Ejecuta el bot con:

```bash
python bot.py
```

En Discord, escribe:

```
/ficha
```

y completa la información para generar tu tarjeta personalizada.

## 📁 Archivos importantes

* `bot.py` → código principal del bot.
* `requirements.txt` → librerías necesarias.
* `.env` → tu token de Discord (necesitas crearlo y ponerlo en la carpeta para que pueda funcionar).
* `img/` → imágenes usadas como fondo y marcos.
* `fonts/` → fuentes usadas para el diseño. Hay algunas adicionales por si quieres experimentar.

## 🌍 Deploy

Puedes correr el bot en Docker usando el Dockerfile adjunto.

## 📜 Licencia

Este proyecto se distribuye bajo la licencia **MIT**.
Eres libre de usarlo, modificarlo y compartirlo.
