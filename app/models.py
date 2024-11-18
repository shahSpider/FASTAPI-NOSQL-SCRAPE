from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
from uuid import UUID

data = {
    "asin": "AMZNNUMBERIDX",
    "title": "Product X",
    "price": "$99"
}

class Product(Model): # --> table
    __keyspace__ = "scraper_app"
    asin: str = columns.Text(primary_key=True, required=True)
    title: str = columns.Text()
    price: str = columns.Text(default="0$")

class ProductScrapeEvent(Model): # --> table
    __keyspace__ = "scraper_app" #A namespace container that defines how data is replicated on nodes in each datacenter.
    uuid: UUID = columns.UUID(primary_key=True)
    asin: str = columns.Text(index=True)
    title: str = columns.Text()
    price: str = columns.Text(default='0$')
    created: str = columns.DateTime()