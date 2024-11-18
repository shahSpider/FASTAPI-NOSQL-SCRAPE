from pydantic import BaseModel, root_validator
from typing import Optional, Any
from uuid import UUID
from . import utils


class ProductSchema(BaseModel):
    asin: str
    title: Optional[str]
    price: Optional[str]


class ProductListSchema(BaseModel):
    asin: str
    title: Optional[str]
    price: Optional[str]


class ProductScrapeEventSchema(BaseModel):
    uuid: UUID
    asin: str
    title: Optional[str]
    price: Optional[str]

class ProductScrapeEventDetailSchema(BaseModel):
    uuid: UUID
    asin: str
    title: Optional[str]
    price: Optional[str]
    created: Optional[Any] = None

    @root_validator(pre=True)
    def extra_create_time_from_uuid(cls, values):
        values['created'] = utils.uuid1_time_to_datetime(values['uuid'].time)
        return values