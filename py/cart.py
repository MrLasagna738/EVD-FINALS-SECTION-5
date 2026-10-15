"""Daily Brew - cart and totals (Member 2).

Events used here:
  click -> "Add to order" buttons and the quantity + / - buttons
"""
from js import setTimeout
from pyodide.ffi import create_proxy
from pyscript import document, when

from data import BY_ID, FIRST_ORDER_RATE, peso, unit_price

cart = {}  # key "id|Size" -> quantity


@when("click", "#menu-grid")
def on_add_click(event):
    btn = event.target.closest(".add")
    if btn is None:
        return
    card = btn.closest(".card")
    picker = card.querySelector(".size")
    size = picker.value if picker is not None else "Regular"
    key = f'{btn.getAttribute("data-id")}|{size}'
    cart[key] = cart.get(key, 0) + 1
    render_cart()

    # small bump on the order counter so the change is noticed
    badge = document.querySelector("#cart-count")
    badge.classList.add("bump")
    setTimeout(create_proxy(lambda: badge.classList.remove("bump")), 350)

    # quick confirmation on the button itself
    btn.textContent = "Added"
    btn.classList.add("done")

    def reset_button():
        btn.textContent = "Add to order"
        btn.classList.remove("done")

    setTimeout(create_proxy(reset_button), 900)


# ---------- Cart ----------
def render_cart():
    box = document.querySelector("#cart-items")
    if not cart:
        box.innerHTML = '<p class="empty">Nothing here yet. Add something from the menu.</p>'
    else:
        lines = []
        for key, qty in cart.items():
            item_id, size = key.split("|")
            item = BY_ID[item_id]
            label = item["name"] + (f" ({size})" if item["drink"] else "")
            line_total = unit_price(key) * qty
            lines.append(
                f'<div class="cart-line">'
                f'<span class="name">{label}</span>'
                f'<span class="qty">'
                f'<button data-key="{key}" data-act="minus" aria-label="Remove one {label}">-</button>'
                f'<span>{qty}</span>'
                f'<button data-key="{key}" data-act="plus" aria-label="Add one {label}">+</button>'
                f'</span>'
                f'<span class="price">{peso(line_total)}</span>'
                f'</div>'
            )
        box.innerHTML = "".join(lines)
    update_totals()
def init():
    render_cart()
