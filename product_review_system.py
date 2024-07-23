#  Product Review System
# Scenario: You are developing a  product review system for an e-commerce platform. 
# Each product has a unique ID and a list of reviews. 
# You need to add new reviews to the products and calculate the average rating for each product.

# Question: Write a function that takes a dictionary representing the products 
# (product IDs as keys and a list of reviews as values, where each review is a dictionary 
# with user and rating), a product ID, and a new review. Update the product's reviews and 
# return the updated average rating for the product.

def product_review(products, prod_id, review):
    avg_rating =0
    for key, value in products.items():        
        if prod_id==key:
            products[key].update(review)
            for _, rating in value.items():
                avg_rating+=rating
            avg_rating=avg_rating/len(value)
    return products, avg_rating

product_details = {1001: {"sharma": 4, "Tony": 3.5, "Pandey": 4.5, "Raju": 3},
                   1002: {"Sree": 3.5, "Edward": 4, "Ramya": 4.7},
                   1003: {"Raja": 4.3, "Sherif": 4.8, "Antony": 4.6}}

print(product_review(product_details, 1002, {"Rinku": 4.3}))