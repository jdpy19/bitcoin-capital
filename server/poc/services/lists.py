from ..database import DB
from ..models import List
from .address_listings import delete_address_listing_service


def create_list_service(name=None, db_session=None):
    db_session = db_session or DB.session
    list = List(name=name)
    db_session.add(list)
    return list


def delete_list_service(list, db_session=None):
    db_session = db_session or DB.session
    for listing in list.listings:
        delete_address_listing_service(listing, db_session=db_session)
    db_session.delete(list)
