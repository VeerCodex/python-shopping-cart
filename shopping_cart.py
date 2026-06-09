# ============================================
#   🛒 Shopping Cart & Inventory Manager
#   Python Lists & Arrays - Full Project
# ============================================

# ---------- INVENTORY (List of Dictionaries) ----------
inventory = [
    {"id": 1, "name": "Apple",    "price": 20,  "stock": 50},
    {"id": 2, "name": "Milk",     "price": 55,  "stock": 30},
    {"id": 3, "name": "Bread",    "price": 40,  "stock": 20},
    {"id": 4, "name": "Eggs",     "price": 80,  "stock": 100},
    {"id": 5, "name": "Butter",   "price": 120, "stock": 15},
]

# Cart -> list of {"item": {...}, "qty": int}
cart = []


# ---------- HELPER FUNCTIONS ----------

def show_inventory():
    print("\n📦 --- INVENTORY ---")
    print(f"{'ID':<5} {'Name':<12} {'Price':>8} {'Stock':>8}")
    print("-" * 36)
    for item in inventory:
        print(f"{item['id']:<5} {item['name']:<12} Rs{item['price']:>6} {item['stock']:>8}")
    print()


def find_item_by_id(item_id):
    # List comprehension - filter and find item by ID
    result = [item for item in inventory if item["id"] == item_id]
    return result[0] if result else None


def add_to_cart(item_id, qty):
    item = find_item_by_id(item_id)
    if not item:
        print("❌ Item not found!")
        return
    if qty > item["stock"]:
        print(f"❌ Only {item['stock']} units available in stock.")
        return

    # Check if item already exists in cart
    existing = [c for c in cart if c["item"]["id"] == item_id]
    if existing:
        existing[0]["qty"] += qty
    else:
        cart.append({"item": item, "qty": qty})

    item["stock"] -= qty
    print(f"✅ {qty}x {item['name']} added to cart!")


def remove_from_cart(item_id):
    global cart
    to_remove = [c for c in cart if c["item"]["id"] == item_id]
    if not to_remove:
        print("❌ This item is not in the cart.")
        return
    entry = to_remove[0]
    entry["item"]["stock"] += entry["qty"]   # Restore stock
    cart = [c for c in cart if c["item"]["id"] != item_id]
    print(f"🗑️  {entry['item']['name']} removed from cart.")


def show_cart():
    if not cart:
        print("\n🛒 Cart is empty!\n")
        return
    print("\n🛒 --- CART ---")
    print(f"{'Name':<12} {'Price':>8} {'Qty':>5} {'Subtotal':>10}")
    print("-" * 38)
    total = 0
    for c in cart:
        subtotal = c["item"]["price"] * c["qty"]
        total += subtotal
        print(f"{c['item']['name']:<12} Rs{c['item']['price']:>6} {c['qty']:>5} Rs{subtotal:>8}")
    print("-" * 38)
    print(f"{'TOTAL':>27} Rs{total:>8}\n")


def checkout():
    if not cart:
        print("❌ Cart is empty. Please add items first.")
        return
    show_cart()
    confirm = input("✅ Confirm checkout? (y/n): ").strip().lower()
    if confirm == 'y':
        cart.clear()
        print("🎉 Order placed! Cart has been cleared. Thank you!\n")
    else:
        print("⏪ Checkout cancelled.\n")


def search_item(name):
    # List comprehension - search item by name
    results = [item for item in inventory if name.lower() in item["name"].lower()]
    if results:
        print(f"\n🔍 Results for '{name}':")
        for item in results:
            print(f"  ID {item['id']}: {item['name']} — Rs{item['price']} (Stock: {item['stock']})")
    else:
        print(f"❌ '{name}' not found in inventory.")
    print()


def show_low_stock(threshold=20):
    low = [item for item in inventory if item["stock"] <= threshold]
    print(f"\n⚠️  Low Stock Items (≤{threshold}):")
    if low:
        for item in low:
            print(f"  {item['name']} — Stock: {item['stock']}")
    else:
        print("  All items have sufficient stock!")
    print()


# ---------- MAIN MENU ----------

def main():
    print("=" * 42)
    print("    🛒  PYTHON SHOPPING CART MANAGER")
    print("=" * 42)

    while True:
        print("1. View Inventory")
        print("2. Add item to Cart")
        print("3. View Cart")
        print("4. Remove item from Cart")
        print("5. Checkout")
        print("6. Search Item")
        print("7. Check Low Stock")
        print("0. Exit")
        print("-" * 30)

        choice = input("Enter option: ").strip()

        if choice == '1':
            show_inventory()

        elif choice == '2':
            show_inventory()
            try:
                item_id = int(input("Enter Item ID: "))
                qty = int(input("Enter Quantity: "))
                add_to_cart(item_id, qty)
            except ValueError:
                print("❌ Invalid input. Please enter a number.\n")

        elif choice == '3':
            show_cart()

        elif choice == '4':
            show_cart()
            try:
                item_id = int(input("Enter Item ID to remove: "))
                remove_from_cart(item_id)
            except ValueError:
                print("❌ Invalid input.\n")

        elif choice == '5':
            checkout()

        elif choice == '6':
            name = input("Enter item name to search: ").strip()
            search_item(name)

        elif choice == '7':
            show_low_stock()

        elif choice == '0':
            print("👋 Goodbye! See you again.\n")
            break

        else:
            print("❌ Invalid option. Please try again.\n")


if __name__ == "__main__":
    main()
