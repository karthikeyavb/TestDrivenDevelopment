def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f"File not found: {file_path}"
    except IOError:
        return "Error reading the file."

# Example usage:
file_path = 'example.txt'
content = read_file(file_path)
print(content)


def update_file(file_path, new_content):
    try:
        with open(file_path, 'w') as file:
            file.write(new_content)
        return f"File updated successfully: {file_path}"
    except FileNotFoundError:
        return f"File not found: {file_path}"
    except IOError:
        return "Error updating the file."

# Example usage:
file_path = 'example.txt'
new_content = "This is the updated content."
result = update_file(file_path, new_content)
print(result)


import os

def delete_file(file_path):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            return f"File deleted successfully: {file_path}"
        else:
            return f"File not found: {file_path}"
    except OSError as e:
        return f"Error deleting file: {e}"

# Example usage:
file_path = 'example.txt'
result = delete_file(file_path)
print(result)



products = [
    {"name": "Laptop", "category": "Electronics", "available": True},
    {"name": "Smartphone", "category": "Electronics", "available": False},
    {"name": "Desk Chair", "category": "Furniture", "available": True},
    {"name": "Table", "category": "Furniture", "available": False},
    {"name": "Headphones", "category": "Electronics", "available": True}
]

def list_all(products):
    return products

# Example usage:
all_products = list_all(products)
for product in all_products:
    print(product)


def list_by_name(products, search_name):
    return [product for product in products if product['name'].lower() == search_name.lower()]

# Example usage:
name_search = "Laptop"
products_by_name = list_by_name(products, name_search)
for product in products_by_name:
    print(product)


def list_by_category(products, category_name):
    return [product for product in products if product['category'].lower() == category_name.lower()]

# Example usage:
category_search = "Furniture"
products_by_category = list_by_category(products, category_search)
for product in products_by_category:
    print(product)



def list_by_availability(products, is_available):
    return [product for product in products if product['available'] == is_available]

# Example usage:
available_products = list_by_availability(products, True)
for product in available_products:
    print(product)

unavailable_products = list_by_availability(products, False)
for product in unavailable_products:
    print(product)

