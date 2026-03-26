#Grocery store with 10 products and their prices
products = {
    "apple": 100,
    "banana": 50,
    "orange": 150,
    "milk": 300,
    "bread": 250,
    "eggs": 200,
    "chicken": 50,
    "rice": 10,
    "pasta": 10,
    "tomatoes": 200
}
#Function to calculate total price of items in the cart
def calculate_total(cart): 
    total = 0
    for item in cart:
        if item in products:
            total += products[item]
        else:
            print(f"{item} is not available in the store.")
    return total
#Ask Customer for items to add to the cart
cart = []
while True:
    item = input("Enter the name of the product to add to the cart (or 'done' to finish): ")
    if item.lower() == 'done':
        break
    cart.append(item)   

#Calculate the total price of items in the cart
total_price = calculate_total(cart)
print(f"Total price of items in the cart: ${total_price}")  
