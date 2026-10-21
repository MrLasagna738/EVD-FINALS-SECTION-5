<h1 align="center">☕ Daily Brew</h1>

<p align="center"><em>A taste of the highlands</em></p>

<p align="center">
  <img src="assets/4Drinksnew.jpg" alt="Four illustrated Daily Brew drinks: iced americano, iced caramel latte, mocha with whipped cream, and cappuccino" width="100%">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/PyScript-2024.11.1-orange?style=for-the-badge" alt="PyScript">
  <img src="https://img.shields.io/badge/Python-3-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/HTML-5-red?style=for-the-badge&logo=html5&logoColor=white" alt="HTML">
  <img src="https://img.shields.io/badge/CSS-3-purple?style=for-the-badge&logo=css3&logoColor=white" alt="CSS">
</p>

<p align="center">
  <a href="https://mrlasagna738.github.io/EVD-FINALS-SECTION-5/"><b>🌐 Live Demo</b></a>
  &nbsp;•&nbsp;
  <a href="https://github.com/MrLasagna738/EVD-FINALS-SECTION-5/releases/download/v1.0/EVD.PRESENTATION.mp4"><b>🎬 Presentation Video</b></a>
  &nbsp;•&nbsp;
  <a href="#-meet-the-team"><b>👥 Team</b></a>
</p>

---

## About

**Daily Brew** is a coffee shop perched above the clouds of Cebu City (Tops Lookout, Busay).
Browse the menu, build your order, and rate your visit, all powered by **Python running right in your browser** with **PyScript**.

This is our final project for **Event-Driven Programming**. Every feature on the page reacts to something the user does.

## Watch the Presentation

Our full video presentation (introduction, business process, website demo, code explanation, and individual contributions) is available as a release download:

**[⬇️ Download EVD.PRESENTATION.mp4 (1.17 GB)](https://github.com/MrLasagna738/EVD-FINALS-SECTION-5/releases/download/v1.0/EVD.PRESENTATION.mp4)**

> 💡 GitHub can't play files this large in the browser, so the video downloads when you click the link. You can also see it on the [release page](https://github.com/MrLasagna738/EVD-FINALS-SECTION-5/releases/tag/v1.0).

## Features (all driven by events)

| Event | What happens |
|-------|--------------|
| `click` | Menu category chips, "Add to order", quantity + / -, star rating |
| `input` | Live menu search, live comment character counter |
| `change` | First-order checkbox recalculates the total |
| `submit` | Place order and send feedback, both with validation |
| `timer` | Open / closed status refreshes every minute |

## Try It Online

No setup needed. Just click the link:

### 👉 **https://mrlasagna738.github.io/EVD-FINALS-SECTION-5/**

## Run It Locally

PyScript needs a web server (opening the file directly will not work).

```bash
python -m http.server 8000
```

Then open http://localhost:8000

## Project Structure

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

## Meet the Team

| # | Member | Part |
|---|--------|------|
| 1 (lead) | **Simone Kristopher Baguio** | Project setup, `data.py`, `menu.py`, `main.py`, menu section, top bar, base + menu CSS |
| 2 | **John Michael Nuñal** | `cart.py`, cart section, Ad video Editor, `cart.css` |
| 3 | **Precious Shiloh Antig** | `order.py`, order form, promo banner, `order.css` |
| 4 | **Alexa Mae Paras** | `status.py`, hero, story, visit, Ad video, footer, `home.css` |
| 5 | **Aizel Clark Cañete** | `feedback.py`, feedback section, `feedback.css`, testing |

---

<p align="center">Made with ☕ and Python in Cebu City</p>
