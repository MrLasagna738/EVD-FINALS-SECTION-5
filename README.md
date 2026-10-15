<h1 align="center">☕ Daily Brew</h1>

<p align="center"><em>A taste of the highlands</em></p>

<p align="center">
  <img src="assets/4Drinksnew.jpg" alt="Four illustrated Daily Brew drinks: iced americano, iced caramel latte, mocha with whipped cream, and cappuccino" width="100%">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/PyScript-2024.11.1-orange" alt="PyScript">
  <img src="https://img.shields.io/badge/Python-3-blue" alt="Python">
  <img src="https://img.shields.io/badge/HTML-5-red" alt="HTML">
  <img src="https://img.shields.io/badge/CSS-3-purple" alt="CSS">
</p>

# Daily Brew

Business website for **Daily Brew**, a coffee shop above Cebu City (Tops Lookout, Busay).
Final project for Event-Driven Programming, built with **PyScript** (Python running in the browser).

## Features (all driven by events)

| Event | What happens |
|-------|--------------|
| `click` | Menu category chips, "Add to order", quantity + / -, star rating |
| `input` | Live menu search, live comment character counter |
| `change` | First-order checkbox recalculates the total |
| `submit` | Place order and send feedback, both with validation |
| timer | Open / closed status refreshes every minute |

## Project structure

```
index.html        page layout (each section is marked with its owner)
pyscript.toml     tells PyScript which Python files to load
py/
  main.py         entry point: imports every module and starts them
  data.py         menu items, prices, helper functions
  menu.py         menu cards, category filter, search
  cart.py         cart, quantity buttons, totals, discount
  order.py        first-order checkbox, order form and validation
  status.py       open / closed status timer
  feedback.py     star rating, comment box, feedback form
css/              one stylesheet per part (base, menu, cart, order, home, feedback)
assets/           photos, hero illustration, Ad video
```

## Team

| Member | Name | Part |
|--------|------|------|
| 1 (lead) | Simone Kristopher Baguio | Project setup, `data.py`, `menu.py`, `main.py`, menu section, top bar, base + menu CSS |
| 2 | John Michael Nuñal | `cart.py`, cart section, Ad video Editor, `cart.css` |
| 3 | Precious Shiloh Antig | `order.py`, order form, promo banner, `order.css` |
| 4 | Alexa Mae Paras | `status.py`, hero, story, visit, Ad video, footer, `home.css` |
| 5 | Aizel Clark Cañete | `feedback.py`, feedback section, `feedback.css`, testing |

## Try it online

No setup needed. Just click the link:

**https://mrlasagna738.github.io/EVD-FINALS-SECTION-5/**

## Run it locally

PyScript needs a web server (opening the file directly will not work).

```
python -m http.server 8000
```

Then open http://localhost:8000
