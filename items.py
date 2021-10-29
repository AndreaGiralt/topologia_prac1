from scrapy.item import Item, Field

class RealStateItem(Item):

    _id = Field() #To upload it from mongo.
    id = Field()
    type = Field()
    title = Field()
    description = Field()
    town = Field()
    zone = Field()
    price = Field()
    surface = Field()
    rooms = Field()
    bathrooms = Field()
    floor = Field()

    longitude = Field()
    latitude = Field()
    url = Field()
    exact_position = Field()
    recently_date = Field()
    is_promo = Field()
    image_url = Field()
    owner_name = Field()
    old_price = Field()