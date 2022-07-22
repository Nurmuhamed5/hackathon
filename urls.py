from venv import create


from views import create, listing, retrieve, delete, update

url_pattern = {
    "create": create,
    "listing": listing,
    "retrieve": retrieve,
    "delete": delete,
    "update": update,
}
