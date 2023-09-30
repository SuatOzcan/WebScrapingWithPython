import re
from locators.book_locators import BookLocators

class BookParser:
    '''A class to take in an HTML page (or a part of it) and find properties of an item in it.'''
    
    RATINGS = {
        'One' : 1,
        'Two' : 2,
        'Three' : 3,
        'Four' : 4,
        'Five' : 5
    }

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<Book {self.name}, £{self.price}, {self.rating} stars.>'

    @property
    def name(self):
        locator = BookLocators.NAME_LOCATOR #locator = 'article.product_pod h3 a'
        item_link = self.parent.select_one(locator)
        item_name = item_link.attrs['title']   #item_link.attrs.get('title')
        return(item_name)
    @property
    def link(self):
        locator = BookLocators.LINK_LOCATOR #locator = 'article.product_pod h3 a'
        item_link = self.parent.select_one(locator)
        item_link_string = item_link.attrs['href']   #item_link.attrs.get('title')
        return(item_link_string)
    @property
    def image_source(self):
        locator = BookLocators.IMAGE_LOCATOR #locator = 'article.product_pod div a img'
        item_link = self.parent.select_one(locator)
        item_image_source = item_link.attrs['src']   #item_link.attrs.get('title')
        return(item_image_source)
    @property
    def price(self):
        locator = BookLocators.PRICE_LOCATOR
        item_price_full = self.parent.select_one(locator).string #£51.77
        pattern = '£([0-9]+.[0-9]+)'
        matches = re.search(pattern,item_price_full)
        item_price_float = float(matches[1])
        return item_price_float
    @property
    def rating(self):
        locator = BookLocators.RATING_LOCATOR  #'article.product_pod p.star_rating.Three'
        star_rating_tag = self.parent.select_one(locator)
        classes = star_rating_tag.attrs['class'] # class order may not be the way it is written in the html file, class order might change.
        rating_classes = [r for r in classes if r != 'star-rating']
        rating_number = BookParser.RATINGS.get(rating_classes[0])  #This will return None if not found.
        return rating_number
