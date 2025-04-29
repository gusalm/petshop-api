class Petshop:

    def __init__(self, id, product_name, product_description, product_price,
                 product_photo, stock_quantity):
        self.id = id
        self.product_name = product_name
        self.product_description = product_description
        self.product_price = product_price
        self.product_photo = product_photo
        self.stock_quantity = stock_quantity


    def to_json(self):
        return {
            "id": self.id,
            "product_name": self.product_name,
            "product_description": self.product_description,
            "product_price": self.product_price,
            "product_photo": self.product_photo,
            "stock_quantity": self.stock_quantity
        }