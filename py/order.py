"""Daily Brew - order form (Member 3).

Events used here:
  change -> first-order checkbox recalculates the total
  submit -> placing an order (with validation)
"""
from pyscript import document, when

from cart import cart, compute_totals, render_cart, update_totals
from data import peso

orders = {"count": 0}


@when("change", "#first-order")
def on_first_order_toggle(event):
    update_totals()


# ---------- Order form ----------
@when("submit", "#order-form")
def on_order_submit(event):
    event.preventDefault()
    msg = document.querySelector("#order-msg")
    name = document.querySelector("#cust-name").value.strip()
    mode = document.querySelector("#pickup").value

    if not cart:
        msg.className = "msg error"
        msg.textContent = "Your order is empty. Add something from the menu first."
        return
    if not name:
        msg.className = "msg error"
        msg.textContent = "Please enter your name so we can call it out."
        return

    _, _, total = compute_totals()
    orders["count"] += 1
    order_no = f'DB-{orders["count"]:03d}'
    count = sum(cart.values())

    msg.className = "msg ok"
    msg.textContent = (
        f"Thank you, {name}! Order {order_no} ({mode}, {count} item"
        f'{"s" if count != 1 else ""}) comes to {peso(total)}. '
        f"We'll have it ready at Tops Lookout."
    )
    cart.clear()
    document.querySelector("#first-order").checked = False
    document.querySelector("#cust-name").value = ""
    render_cart()
