# Kamil Kamiński

print("\nZad 1")
shopping_list = {
    'piekarnia': ['chleb', 'pączek', 'bułki'],
    'warzywniak': ['marchew', 'seler', 'rukola']
}

items_number = 0

for shop, products in shopping_list.items():
    shop = shop.capitalize()
    products = [product.capitalize() for product in products]
    items_number += len(products)
    print(f"Idę do {shop} i kupuję tam {products}.")

print(f"W sumie kupuję {items_number} produktów.")
