from loaders.load_brand import load_brands
from loaders.load_category import load_categories
from loaders.load_seller import load_sellers
from loaders.load_product import load_products
from loaders.load_promotion import load_promotions
from loaders.load_promotion_product import load_promotion_products
from loaders.load_order import load_orders
from loaders.load_order_item import load_order_items

if __name__ == "__main__":
    print("Loading brands...")
    load_brands()

    print("Loading categories...")
    load_categories()
    
    print("Loading sellers...")
    load_sellers()
    
    print("Loading products...")
    load_products()
    
    print("Loading orders...")
    load_orders()
    
    print("Loading order items...")
    load_order_items()
    
    print("Loading promotions...")
    load_promotions()
    
    print("Loading promotion products...")
    load_promotion_products()

    print("DONE ✅")
