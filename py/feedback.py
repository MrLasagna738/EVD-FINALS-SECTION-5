"""Daily Brew - customer feedback (Member 5's part).

Events used here:
  click  -> choosing a star rating
  input  -> live character counter while typing a comment
  submit -> sending the feedback, with validation
"""
from pyscript import document, when

MAX_CHARS = 200
WORDS = {1: "Poor", 2: "Fair", 3: "Good", 4: "Very good", 5: "Excellent"}
rating = {"value": 0}


def paint_stars(value):
    """Fill in the stars up to the chosen rating."""
    for star in document.querySelectorAll(".star"):
        filled = int(star.getAttribute("data-value")) <= value
        star.classList.toggle("on", filled)
        star.setAttribute("aria-pressed", "true" if filled else "false")
    label = document.querySelector("#rating-label")
    if value:
        label.textContent = f"Your rating: {value} of 5 ({WORDS[value]})"
    else:
        label.textContent = "Your rating"


@when("click", "#stars")
def on_star_click(event):
    star = event.target.closest(".star")
    if star is None:
        return
    rating["value"] = int(star.getAttribute("data-value"))
    paint_stars(rating["value"])


@when("input", "#fb-text")
def on_comment_input(event):
    count = len(event.target.value)
    counter = document.querySelector("#fb-count")
    counter.textContent = f"{count} / {MAX_CHARS}"
    counter.classList.toggle("near", count >= MAX_CHARS - 20)


@when("submit", "#feedback-form")
def on_feedback_submit(event):
    event.preventDefault()
    msg = document.querySelector("#fb-msg")
    box = document.querySelector("#fb-text")

    if rating["value"] == 0:
        msg.className = "msg error"
        msg.textContent = "Please choose a star rating first."
        return

    stars = rating["value"]
    msg.className = "msg ok"
    if stars <= 2:
        msg.textContent = "Thank you for telling us. We're sorry it fell short and will work on it."
    else:
        msg.textContent = f"Thank you! We're glad you gave us {stars} stars."

    # reset the form for the next person
    box.value = ""
    rating["value"] = 0
    paint_stars(0)
    document.querySelector("#fb-count").textContent = f"0 / {MAX_CHARS}"
