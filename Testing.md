# Testing checklist

Tested by: Member 5
Browser / device: (e.g. Chrome on Windows)

| # | What was tested | How | Expected | Result |
|---|-----------------|-----|----------|--------|
| 1 | Menu category filter | Click each chip (e.g. Hot, Iced, Pastries) | Only that category shows | Pass |
| 2 | Menu search | Type "latte" in the search box | Cards filter live as you type | Pass |
| 3 | Add to order | Click "Add to order" on an item | Item appears in the cart | Pass |
| 4 | Quantity buttons | Press + and - in the cart | Quantity and total change; item removed at 0 | Pass |
| 5 | First-order discount | Tick "This is my first order" | 10% discount shown, total drops | Pass |
| 6 | Place order (empty cart) | Click Place order with no items | Red "order is empty" message | Pass / Fail |
| 7 | Place order (no name) | Add item, leave name blank, submit | Red "enter your name" message | Pass / Fail |
| 8 | Place order (valid) | Add item, enter name, submit | Green message with DB-001, cart clears | Pass / Fail |
| 9 | Star rating | Click 1 to 5 stars | Stars fill, label shows rating | Pass / Fail |
| 10 | Comment counter | Type in the comment box | Counter updates, turns red near 200 | Pass / Fail |
| 11 | Feedback (no rating) | Submit without stars | Red "choose a star rating" message | Pass / Fail |
| 12 | Feedback (valid) | Pick stars, submit | Thank-you message, form resets | Pass / Fail |
| 13 | Open/closed status | Look at the hero | Shows open or closed for Philippine time | Pass / Fail |
| 14 | Phone width | Resize the window narrow (or use F12 device mode) | Layout stacks, nothing cut off | Pass / Fail |

## Problems found
- None
