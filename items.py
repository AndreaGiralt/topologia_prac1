from scrapy.item import Item, Field

class RealStateItem(Item):
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