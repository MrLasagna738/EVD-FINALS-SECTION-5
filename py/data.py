"""Daily Brew - shared data and helpers (Member 1).

Plain Python only (no browser code), so every other module can import it.
"""

LARGE_EXTRA = 20          # pesos added to a Large drink
FIRST_ORDER_RATE = 0.10   # 10% off first order (from the flyer)

MENU = [
    {"id": "brew",   "name": "Highland Brew",     "cat": "hot",     "price": 90,  "drink": True,  "desc": "Freshly brewed coffee, from the highlands to your cup."},
    {"id": "latte",  "name": "Cafe Latte",        "cat": "hot",     "price": 130, "drink": True,  "desc": "Espresso with steamed milk and leaf art."},
    {"id": "cappu",  "name": "Cappuccino",        "cat": "hot",     "price": 130, "drink": True,  "desc": "Equal parts espresso, milk and thick foam."},
    {"id": "mocha",  "name": "Cinnamon Mocha",    "cat": "hot",     "price": 150, "drink": True,  "desc": "Chocolate, espresso and a dusting of cinnamon."},
    {"id": "iamer",  "name": "Iced Americano",    "cat": "iced",    "price": 110, "drink": True,  "desc": "Espresso over ice. Clean and strong."},
    {"id": "ilatte", "name": "Iced Latte",        "cat": "iced",    "price": 140, "drink": True,  "desc": "Cold milk, espresso, lots of ice."},
    {"id": "ispan",  "name": "Iced Spanish Latte","cat": "iced",    "price": 150, "drink": True,  "desc": "Sweetened condensed milk and espresso."},
    {"id": "icaram", "name": "Iced Caramel Macchiato", "cat": "iced", "price": 160, "drink": True, "desc": "Vanilla, milk, espresso and caramel drizzle."},
    {"id": "crois",  "name": "Butter Croissant",  "cat": "pastry",  "price": 85,  "drink": False, "desc": "Flaky, golden and baked fresh."},
    {"id": "roll",   "name": "Cinnamon Roll",     "cat": "pastry",  "price": 95,  "drink": False, "desc": "Soft roll with cinnamon sugar glaze."},
    {"id": "quiche", "name": "Quiche Slice",      "cat": "pastry",  "price": 120, "drink": False, "desc": "Savory slice with a buttery crust."},
    {"id": "cheese", "name": "Basque Cheesecake", "cat": "dessert", "price": 160, "drink": False, "desc": "Creamy center, caramelized top."},
]
BY_ID = {m["id"]: m for m in MENU}


def slug(name):
    """'Iced Spanish Latte' -> 'iced-spanish-latte' (the image file name)."""
    return name.lower().replace(" ", "-")


def peso(amount):
    return f"₱{amount:,.2f}"


def unit_price(key):
    item_id, size = key.split("|")
    price = BY_ID[item_id]["price"]
    if size == "Large":
        price += LARGE_EXTRA
    return price
