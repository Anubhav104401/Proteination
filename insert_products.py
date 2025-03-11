from pymongo import MongoClient

# MongoDB Connection
MONGO_URI = "mongodb+srv://anubhavk104:anubhavk104@cluster0.3uyck.mongodb.net/"
client = MongoClient(MONGO_URI)
db = client["ecommerce"]
products_collection = db["products"]

# Sample Products
products = [
    {
        "_id": "1",
        "name": "Muscleblaze Biozyme Whey",
        "description": "High-quality product for daily use.",
        "price": 4400,
        "stock": 10
    },
    {
        "_id": "2",
        "name": "ON Gold Standard Whey",
        "description": "Extraordinary results for extraordinary gainers.",
        "price": 2899,
        "stock": 8
    },
    {
        "_id": "3",
        "name": "Muscletech Nitrotech Gold Whey",
        "description": "Premium quality and excellent recovery.",
        "price": 5999,
        "stock": 5
    }
]

# Insert Products into MongoDB
products_collection.insert_many(products)

print("Products added successfully!")
