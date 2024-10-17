from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

data = {
    "asin": "AMZNNUMBERID2",
    "title": "Product B"
}

class Product(Model): # --> table
    __keyspace__ = "scraper_app"
    asin: str = columns.Text(primary_key=True, required=True)
    title: str = columns.Text()