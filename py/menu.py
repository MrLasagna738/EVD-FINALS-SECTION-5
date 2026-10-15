"""Daily Brew - menu section (Member 1).

Events used here:
  click -> category chips
  input -> live menu search while typing
"""
from js import window
from pyodide.ffi import create_proxy
from pyscript import document, when

from data import LARGE_EXTRA, MENU, peso, slug

state = {"cat": "all", "q": "", "shown": None}

IMAGE_EXTS = ["jpg", "png", "jpeg", "webp"]


def next_image(img):
    """Called by the browser when an image fails to load: try the next file type."""
    i = int(img.getAttribute("data-try")) + 1
    if i < len(IMAGE_EXTS):
        img.setAttribute("data-try", str(i))
        img.src = f'assets/{img.getAttribute("data-slug")}.{IMAGE_EXTS[i]}'
    else:
        img.removeAttribute("onerror")
        img.parentElement.classList.add("no-photo")


window.nextImage = create_proxy(next_image)


def render_menu(animate=False, force=False):
    grid = document.querySelector("#menu-grid")
    q = state["q"]
    shown = [
        m for m in MENU
        if (state["cat"] == "all" or m["cat"] == state["cat"])
        and q in (m["name"] + " " + m["desc"]).lower()
    ]
    ids = tuple(m["id"] for m in shown)
    if ids == state["shown"] and not force:
        return  # same cards as before: skip, so typing never restarts the animation
    state["shown"] = ids
    grid.classList.toggle("swap", animate)  # fade the cards in when the results change

    if not shown:
        grid.innerHTML = '<p class="empty">Nothing matches your search. Try another word or choose All.</p>'
        return

    cards = []
    for i, m in enumerate(shown):
        name = m["name"]
        size_picker = ""
        if m["drink"]:
            size_picker = (
                f'<select class="size" aria-label="Size for {name}">'
                f'<option value="Regular">Regular</option>'
                f'<option value="Large">Large +₱{LARGE_EXTRA}</option></select>'
            )
        cards.append(
            f'<article class="card" style="--i:{min(i, 8)}">'
            f'<div class="photo">'
            f'<img src="assets/{slug(name)}.jpg" alt="{name}" loading="lazy" '
            f'data-slug="{slug(name)}" data-try="0" onerror="nextImage(this)">'
            f'<span class="tag">{peso(m["price"])}</span>'
            f'</div>'
            f'<div class="body">'
            f'<h3>{name}</h3><p>{m["desc"]}</p>'
            f'<div class="row">{size_picker}'
            f'<button class="add" data-id="{m["id"]}">Add to order</button></div>'
            f'</div>'
            f'</article>'
        )
    grid.innerHTML = "".join(cards)



def init():
    render_menu()
