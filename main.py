############################################################################
## Django ORM Standalone Python Template
############################################################################
""" Here we'll import the parts of Django we need. It's recommended to leave
these settings as is, and skip to START OF APPLICATION section below """

# Turn off bytecode generation
import sys
sys.dont_write_bytecode = True

# Import settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

# setup django environment
import django
django.setup()

# Import your models for use in your script
from db.models import *

############################################################################
## START OF APPLICATION
############################################################################
def populate_products():
    print("\n=== Populating Product Database ===")
    
    # Products from Assignment 2
    products_data = [
        {"upc": "12345", "name": "Coffee", "price": 8.32},
        {"upc": "67890", "name": "Muffin", "price": 2.50},
        {"upc": "11111", "name": "Sandwich", "price": 5.99},
        {"upc": "22222", "name": "Cookie", "price": 1.25},
        {"upc": "33333", "name": "Tea", "price": 3.75},
        {"upc": "44444", "name": "Juice", "price": 4.50},
        {"upc": "55555", "name": "Bagel", "price": 3.25},
        {"upc": "66666", "name": "Donut", "price": 1.75},
        {"upc": "77777", "name": "Salad", "price": 7.99},
        {"upc": "88888", "name": "Water", "price": 1.50},
    ]
    
    # Add products to database
    for product_data in products_data:
        product, created = Product.objects.get_or_create(
            upc=product_data["upc"],
            defaults={
                "name": product_data["name"],
                "price": product_data["price"]
            }
        )
        if created:
            print(f"Added: {product}")
        else:
            print(f"Already exists: {product}")
    
    print(f"\nTotal products in database: {Product.objects.count()}")


def display_all_products():
    """Display all products in the database"""
    print("\n=== Current Product Inventory ===")
    products = Product.objects.all()
    if products:
        print(f"{'UPC':<10} {'Product':<15} {'Price':<10}")
        print("-" * 35)
        for product in products:
            print(f"{product.upc:<10} {product.name:<15} ${product.price:<9.2f}")
    else:
        print("No products in database.")


def scan_product(upc):
    try:
        product = Product.objects.get(upc=upc)
        print("\n" + "="*50)
        print("PRODUCT FOUND")
        print("="*50)
        print(f"Name:  {product.name}")
        print(f"Price: ${product.price}")
        print("="*50)
        return product
    except Product.DoesNotExist:
        print("\n" + "="*50)
        print("ERROR: Product not found!")
        print("="*50)
        print(f"UPC '{upc}' is not in the database.")
        return None


def cash_register_ui():
    print("\n" + "="*50)
    print("CASH REGISTER - Product Scanner")
    print("="*50)
    print("Commands:")
    print(" - Enter UPC code to scan product")
    print(" - Type 'list' to see all products")
    print(" - Type 'quit' or 'exit' to quit")
    print("="*50)
    
    while True:
        try:
            user_input = input("\nScan UPC (or command): ").strip()
            
            if user_input.lower() in ['quit', 'exit']:
                print("\nThank you for using the cash register!")
                break
            elif user_input.lower() == 'list':
                display_all_products()
            elif user_input:
                scan_product(user_input)
            else:
                print("Please enter a valid UPC code or command.")
        except KeyboardInterrupt:
            print("\n\nShutting down cash register...")
            break
        except Exception as e:
            print(f"Error: {e}")


def main():
    print("\n" + "="*50)
    print("DJANGO ORM CASH REGISTER APPLICATION")
    print("="*50)
    
    # Part a: Populate the database
    populate_products()
    
    # Display all products
    display_all_products()
    
    # Part b: Allow the user to scan products
    print("\n\nStarting interactive mode...")
    cash_register_ui()


if __name__ == "__main__":
    main()
