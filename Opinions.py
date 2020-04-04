import requests
from bs4 import BeautifulSoup
from Opinion import Opinion

class Opinions:
    opinions = []
    URL_PREFIX = "https://www.ceneo.pl"
    URL_POSTFIX = "#tab-reviews"
    TAGS = {
        "recommendation": ["div", "product-review-summary", "em"],
        "stars": ["span", "review-score-count"],
        "content": ["p", "product-review-body"],
        "author": ["div", "reviewer-name-line"],
        "pros": ["div", "pros-cell", "ul"],
        "cons": ["div", "cons-cell", "ul"],
        "useful": ["button", "vote-yes", "span"],
        "useless": ["button", "vote-no", "span"],
        "purchased": ["div", "product-review-pz"],
    }

    def __init__(self, opinions_list):
        self.opinions = opinions_list

    def __str__(self):
        return str([x for x in self.opinions])
    
    def insert_to_database(self):
        for opinion in self.opinions:
            opinion.insert_to_database()

    @staticmethod
    def get_opinions(id):
        url = Opinions.URL_PREFIX+"/"+str(id)+Opinions.URL_POSTFIX
        opinions_list = []

        while True:
            res = requests.get(url)
            tree = BeautifulSoup(res.text, 'html.parser')
            opinions = tree.find_all("li", "js_product-review")

            for opinion in opinions:
                features = {key:Opinion.get_opinion_feature(opinion, *args)
                            for key, args in Opinions.TAGS.items()}
                if features['purchased'] == "Opinia potwierdzona zakupem":
                    features['purchased'] = True
                else:
                    features['purchased'] = False
                features['id'] = opinion["data-entry-id"]
                features['product_id'] = id
                dates = opinion.find("span", "review-time").find_all("time")
                features['review_date'] = dates.pop(0)["datetime"]
                try:
                    features['purchase_date'] = dates.pop(0)["datetime"]
                except IndexError:
                    features['purchase_date'] = None
                
                opinions_list.append(
                    Opinion(
                        features['id'],
                        features['product_id'],
                        features['author'],
                        features['recommendation'],
                        features['stars'],
                        features['content'],
                        features['pros'],
                        features['cons'],
                        features['useful'],
                        features['useless'],
                        features['purchased'],
                        features['review_date'],
                        features['purchase_date']
                    )
                )
            try:
                url = Opinions.URL_PREFIX+tree.find("a", "pagination__next")["href"]
            except TypeError:
                break
        return Opinions(opinions_list)

if __name__ == "__main__":
    ops = Opinions.get_opinions(91074697)
    ops.insert_to_database()

    ops = Opinions.get_opinions(91715705)
    ops.insert_to_database()