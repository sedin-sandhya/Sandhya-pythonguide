# You are given a list of product dictionaries from an e-commerce platform. 
# Use lambda functions with 
#     map() 
#     filter()
#     sorted() 
# to build a data processing pipeline. 
# No for loops allowed for the transformations. 
# Apply discounts, filter by rating, sort by price, and format output. 

products = [ 
  {"name": "iPhone 15", "price": 79999, "category": "Electronics", "rating": 4.5}, 
  {"name": "Nike Shoes", "price": 8999, "category": "Fashion", "rating": 4.2}, 
  {"name": "MacBook Pro", "price": 149999, "category": "Electronics", "rating": 4.8}, 
  {"name": "Levi Jeans", "price": 3499, "category": "Fashion", "rating": 3.9}, 
  {"name": "Sony Headphones","price": 12999, "category": "Electronics", "rating": 4.6}, 
  {"name": "Kurta Set", "price": 1299, "category": "Fashion", "rating": 4.1}, 
] 

# Task 1: Apply 10% discount to all Electronics 

discounted = list(
    map(
        lambda p: {
            **p,
            "price" : float(f"{(p["price"] * 0.10):.2f}"),
        } if p["category"] == "Electronics" else p,
        products
    )
)

# Task 2: Filter products with rating >= 4.2 

rating_filter = list(
    filter(
        lambda p: p["rating"] >= 4.2, 
        discounted
    )
)

# Task 3: Sort by price (low to high) 

sorted_list = list(
    sorted(
        rating_filter, key=lambda p: p["price"]
    )
)

# Task 4: Format as "Name — Rs.Price (Rating stars)" 

formatted = list(
    map(
        lambda p: f"{p["name"]} -- Rs{p["price"]} ({p["rating"]})", 
        sorted_list
    )
)
print(formatted)