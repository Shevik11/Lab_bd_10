from db import DBConnection
from DAO import DAO
import os
from dotenv import load_dotenv

load_dotenv()

# Set your database connection details
db_connection = DBConnection(
    host=os.environ.get("DB_HOST"),
    user=os.environ.get("DB_USER"),
    password=os.environ.get("DB_PASSWORD"),
    database=os.environ.get("DB_DATABASE")
)
dao = DAO(db_connection)

def yes_or_no():
    while True:
        choice = input("Enter yes or no: ")
        if choice.lower() == "yes":
            selected_table = table_choice_text()
            table_choice(selected_table)
        elif choice.lower() == "no":
            break
        else:
            print("Invalid input. Please enter yes or no.")

def table_choice_text():
    print("Choose table")
    print("1. auctions")
    print("2. persons")
    print("3. items")
    table = input("Enter the number corresponding to the table: ")
    return table

def auction_command():
    print("What do you want to do?")
    print("1. Show auctions")
    print("2. Create auction")
    print("3. Delete auction")
    print("4. Edit auction")
    print("6. Get 1 auction")
    print("5. Go back")
    choice = input("Enter the number corresponding to your choice: ")
    
    match choice:
        case "1":
            dao.get("auctions")
            yes_or_no()
        case "2":
            auction_date = input("Enter auction date: ")
            auction_time = input("Enter auction time: ")
            location = input("Enter location: ")
            features = input("Enter features: ")
            dao.create_record("auctions", {
                "auction_date": auction_date,
                "auction_time": auction_time,
                "location": location,
                "features": features
            })
            print("Auction created successfully!")
            yes_or_no()
        case "3":
            auction_id = input("Enter auction id: ")
            dao.delete_record("auctions","auction_id", auction_id)
            print("Auction deleted successfully!")
            yes_or_no()
        case "4":
            auction_id = input("Enter auction id: ")
            auction_date = input("Enter auction date: ")
            auction_time = input("Enter auction time: ")
            location = input("Enter location: ")
            features = input("Enter features: ")
            dao.edit_record("auctions", "auction_id", auction_id, {
                "auction_date": auction_date,
                "auction_time": auction_time,
                "location": location,
                "features": features
            })
            print("Auction edited successfully!")
            yes_or_no()

        case "5":
            yes_or_no()    

        case "6":
            auction_id = input("Enter auction id: ")
            dao.get_one("auctions", "auction_id", auction_id)
            yes_or_no()

def person_command():
    print("What do you want to do?")
    print("1. Show persons")
    print("2. Create person")
    print("3. Delete person")
    print("4. Edit person")
    print("5. get 1 person")
    choice = input("Enter the number corresponding to your choice: ")
    
    match choice:
        case "1":
            dao.get("persons")
            yes_or_no()
        case "2":
            full_name = input("Enter full name: ")
            date_of_birth = input("Enter date of birth: ")
            address = input("Enter address: ")
            phone_number = input("Enter phone number: ")
            buyer_id = input("Enter buyer id: ")
            seller_id = input("Enter seller id: ")
            dao.create_record("persons", {
                "full_name": full_name,
                "date_of_birth": date_of_birth,
                "phone_number": phone_number,
                "address": address,
                "buyer_id": buyer_id,
                "seller_id": seller_id
            })
            print("Person created successfully!")
            yes_or_no()
        case "3":
            person_id = input("Enter person id: ")
            dao.delete_record("persons", "person_id", person_id)
            print("Person deleted successfully!")
            yes_or_no()
        case "4":
            person_id = input("Enter person id: ")
            full_name = input("Enter full name: ")
            date_of_birth = input("Enter date of birth: ")
            address = input("Enter address: ")
            phone_number = input("Enter phone number: ")
            buyer_id = input("Enter buyer id: ")
            seller_id = input("Enter seller id: ")
            dao.edit_record("persons", "person_id", person_id, {
                "full_name": full_name,
                "date_of_birth": date_of_birth,
                "phone_number": phone_number,
                "address": address,
                "buyer_id": buyer_id,
                "seller_id": seller_id
            })
            print("Person edited successfully!")
            yes_or_no()
        case "5":
            person_id = input("Enter person id: ")
            dao.get_one("persons", "person_id", person_id)


def items_command():
    print("What do you want to do?")
    print("1. Show items")
    print("2. Create item")
    print("3. Delete item")
    print("4. Edit item")
    print("5. get 1 item")
    choice = input("Enter the number corresponding to your choice: ")
    
    match choice:
        case "1":
            dao.get("items")
            yes_or_no()
        case "2":
            auction_id = input("Enter auction id: ")
            lot_number = input("Enter lot number: ")
            start_price = input("Enter start price: ")
            short_description = input("Enter short description: ")
            sale_price = input("Enter sale price: ")
            seller_id = input("Enter seller id: ")
            buyer_id = input("Enter buyer id: ")
            dao.create_record("items", {
                "auction_id": auction_id,
                "lot_number": lot_number,
                "start_price": start_price,
                "short_description": short_description,
                "sale_price": sale_price,
                "seller_id": seller_id,
                "buyer_id": buyer_id
            })
            print("Item created successfully!")
            yes_or_no()
        case "3":
            item_id = input("Enter item id: ")
            dao.delete_record("items", "item_id", item_id)
            print("Item deleted successfully!")
            yes_or_no()
        case "4":
            item_id = input("Enter item id: ")
            auction_id = input("Enter auction id: ")
            lot_number = input("Enter lot number: ")
            start_price = input("Enter start price: ")
            short_description = input("Enter short description: ")
            sale_price = input("Enter sale price: ")
            seller_id = input("Enter seller id: ")
            buyer_id = input("Enter buyer id: ")
            dao.edit_record("items", "item_id", item_id, {
                "auction_id": auction_id,
                "lot_number": lot_number,
                "start_price": start_price,
                "short_description": short_description,
                "sale_price": sale_price,
                "seller_id": seller_id,
                "buyer_id": buyer_id,
                "item_id": item_id
            })
            print("Item edited successfully!")
            yes_or_no()
        case "5":
            item_id = input("Enter item id: ")
            dao.get_one("items", "item_id", item_id)


def table_choice(table):
    match table:
        case "1":
            auction_command()
        case "2":
            person_command()
        case "3":
            items_command()

def main():
    selected_table = table_choice_text()
    table_choice(selected_table)

if __name__ == "__main__":
    main()
