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
