import requests
from bs4 import BeautifulSoup
from Opinions import Opinions
import mysql.connector
from Database import DB

class Product:
    URL_PREFIX = "https://www.ceneo.pl/"
    TAGS = {
        "name": "h1.product-name",
        "subname": "div.ProductSublineTags",
        "price_value": "span.price span.value", 
        "price_penny": "span.price span.penny",
        "score": "span.product-score"
    }

    opinions = []

    def __init__(self, id, name, subname, price, score, opinions):
        self.id = id
        self.name = name
        self.subname = subname
        self.price = price
        self.score = score
        self.opinions = opinions

    def insert_to_database(self):
        
        cursor = DB.cursor()
        query = "INSERT INTO products (id, name, subname, price, score)\
            VALUES(%s, %s, %s, %s, %s)"
        values = (self.id, self.name, self.subname, self.price, self.score)
        try:
            cursor.execute(query, values)
        except mysql.connector.errors.DataError:
            pass
        except mysql.connector.errors.IntegrityError:
            pass
        self.opinions.insert_to_database()
        DB.commit()

    @staticmethod
    def get_opinion_feature(product, tag):
        try:
            return product.select_one(tag).get_text().strip().replace('\n', '').replace('\t', '')
        except AttributeError:
            return None

    @staticmethod
    def get_product(id):
        url = Product.URL_PREFIX+str(id)
        res = requests.get(url)
        tree = BeautifulSoup(res.text, features="html.parser")
        product = tree.select('table.product-content')
        features = {key:Product.get_opinion_feature(tree, args)
                            for key, args in Product.TAGS.items()}
        features['id'] = id
        features['score'] = features['score'][:3]
        opinions = Opinions.get_opinions(id)

        product = Product(
            features['id'],
            features['name'],
            features['subname'],
            features['price_value']+features['price_penny'],
            features['score'],
            opinions
        )
        return product



if __name__ == "__main__":
    p = Product.get_product(91715705)
    p.insert_to_database()