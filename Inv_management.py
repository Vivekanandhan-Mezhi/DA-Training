# Inventory Management System
# Scenario: You are developing an inventory management system for a warehouse. 
# Each product has a unique ID, a quantity in stock, and a list of suppliers. You need to process 
# new shipments to update the stock quantities and handle backorders.

# Question: Write a function that takes a dictionary representing the inventory (product IDs as 
# keys and a dictionary with quantity and suppliers as values), a list of new shipments (each shipment 
# is a dictionary with product ID, quantity, and supplier), and a dictionary of backorders (product IDs 
# as keys and quantities as values). Update the inventory and backorders based on the new shipments and 
# return the updated inventory and backorders.

def inventory(inventory_detail, shipment_list, backorder={}):
    for item in shipment_list:
        if list(item.keys())[0] in inventory_detail:
            if item[list(item.keys())[0]]["supplier"] == inventory_detail[list(item.keys())[0]]["supplier"]:
                inventory_detail[list(item.keys())[0]]["quantity"] += item[list(item.keys())[0]]["quantity"]
            else:
                inventory_detail[list(item.keys())[0]]["quantity"] += item[list(item.keys())[0]]["quantity"]
                # supplier = item[list(item.keys())[0]]["supplier"]
                # print(inventory_detail[list(item.keys())[0]]["supplier"])
                [inventory_detail[list(item.keys())[0]]["supplier"].append(x) for x in item[list(item.keys())[0]]["supplier"] if x not in inventory_detail[list(item.keys())[0]]["supplier"]]
        else:
            inventory_detail.update(item)
    return inventory_detail

inventory_details = {"P001": {"quantity": 10, "supplier": ["S001"]},
                     "P002": {"quantity": 8, "supplier": ["S002"]}}
list_of_shipment = [{"P001": {"quantity": 2, "supplier": ["S002"]}}, {"P003": {"quantity": 4, "supplier": ["S004"]}}]

inventory_details = inventory(inventory_details, list_of_shipment)
list_of_shipment = [{"P002": {"quantity": 6, "supplier": ["S002", "S006"]}}, {"P003": {"quantity": 10, "supplier": ["S004", "S005"]}}, {"P002": {"quantity": 6, "supplier": ["S006", "S005"]}}]
print(inventory(inventory_details, list_of_shipment))
