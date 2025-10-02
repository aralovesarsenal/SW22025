from pyscript import display
#Restaurant Order System (Python Data Types)

#String
restaurant_name = "Divino Aura Farming"
owner_name = "Princess Radhika D. Evangelio" 

#Integer
year_since = 2010 

#Float
tax_rate = 0.08

#Boolean
has_delivery = True
is_dine_in = True
is_takeaway = False

#List
product_name = "5 Inches Taller" , "Become 6ft" , "Nonchalance"
beverages = "Matcha" , "Milk Tea" 

#Tuple
business_hours = ("11:00 AM" , "10:00 PM")

#Dictionary
menu = {
    "5 Inches Taller" : 5000,
    "Become 6ft" : 6000,
    "Nonchalance" : 67,
    "Matcha" : 6,
    "Milk Tea" : 7
}

#Set
common_allergens = {"emotion", "short people", "being broke"}

#Display restaurant information
display(restaurant_name, target="name1")
display(f"Owner: {owner_name}", target="owner")
display(f"Since {year_since}", target="since")
display("Menu Pricelist", target="heading1")

#Display menu items
display(product_name[0], target="prod1")
display(f"₱{menu['5 Inches Taller']:.2f}", target="price1")
display(product_name[1], target="prod2")
display(f"₱{menu['Become 6ft']:.2f}", target="price2")
display(product_name[2], target="prod3")
display(f"₱{menu['Nonchalance']:.2f}", target="price3")

display(beverages[0], target="prod4")
display(f"₱{menu['Matcha']:.2f}", target="price4")
display(beverages[1], target="prod5")
display(f"₱{menu['Milk Tea']:.2f}", target="price5")


#display additional info
display(f"Open: {business_hours[0]} - {business_hours[1]}", target="openingHours")

#display order type
display(f"Dine-in Available", target="orderType")