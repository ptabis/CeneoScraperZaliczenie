import requests
from bs4 import BeautifulSoup
import mysql.connector
from Database import DB

class Opinion:

    def __init__(self, id, product_id, author, recommendation, stars, 
                content, pros, cons, useful, useless, purchased,
                review_date, purchase_date):
        self.id = id
        self.product_id = product_id
        self.author = author
        self.recommendation = recommendation
        self.stars = stars
        self.content = content
        self.pros = pros
        self.cons = cons
        self.useful = useful
        self.useless = useless
        self.purchased = purchased
        self.review_date = review_date
        self.purchase_date = purchase_date
    
    def __repr__(self):
        return f"{{id={self.id},\
    product_id={self.product_id},\
    author={self.author},\
    recommendation={self.recommendation},\
    stars={self.stars},\
    content={self.content},\
    pros={self.pros},\
    cons={self.cons},\
    useful={self.useful},\
    useless={self.useless},\
    purchased={self.purchased},\
    review_date={self.review_date},\
    purchase_date={self.purchase_date}}}"

    def insert_to_database(self):
        
        cursor = DB.cursor()
        query = "INSERT INTO opinions (\
                id, product_id, author, recommendation, stars, content,\
                useful, useless, purchased, review_date, purchase_date\
            )\
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (self.id, self.product_id, self.author, self.recommendation, self.stars, self.content,
        self.useful, self.useless, self.purchased, self.review_date, self.purchase_date)
        try:
            cursor.execute(query, values)
        except mysql.connector.errors.DataError:
            pass
        except mysql.connector.errors.IntegrityError:
            pass

        if self.pros is not None:
            for pro in self.pros.strip().split("\n"):
                query = "INSERT INTO pros (opinion_id, text) VALUES( %s, %s)"
                values = (self.id, pro)
                try:
                    cursor.execute(query, values)
                    print("s")
                except mysql.connector.errors.DataError:
                    pass
                except mysql.connector.errors.IntegrityError:
                    pass

        if self.cons is not None:
            for con in self.cons.strip().split("\n"):
                query = "INSERT INTO cons (opinion_id, text) VALUES( %s, %s)"
                values = (self.id, con)
                try:
                    cursor.execute(query, values)
                except mysql.connector.errors.DataError:
                    pass
                except mysql.connector.errors.IntegrityError:
                    pass
        DB.commit()

    @staticmethod
    def get_opinion_feature(opinion, tag, tag_class, child=None):
        try:
            if child:
                return opinion.find(tag, tag_class).find(child).get_text().strip()
            else:
                return opinion.find(tag, tag_class).get_text().strip()
        except AttributeError:
            return None
