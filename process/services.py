import math


receipt_schema = {
    "type": "object",
    "properties": {
        "retailer": {"type": "string"},
        "purchaseDate": {
            "type": "string",
            "pattern": "^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2]\d|3[0-1])$",
        },
        "purchaseTime": {"type": "string", "pattern": "^(0\d|1\d|2[0-3]):[0-5]\d$"},
        "items": {
            "type": "array",
            "minItems": 1,
            "items": {
                "type": "object",
                "properties": {
                    "shortDescription": {"type": "string"},
                    "price": {"type": "string", "pattern": "^\\d+\\.\\d{2}$"},
                },
                "required": ["shortDescription", "price"],
            },
        },
        "total": {"type": "string", "pattern": "^\\d+\\.\\d{2}$"},
    },
    "required": ["retailer", "purchaseDate", "purchaseTime", "items", "total"],
}


def calculate_points(receipt):
    points = 0

    points += sum(ch.isalnum() for ch in receipt["retailer"])

    if float(receipt["total"]) == round(float(receipt["total"])):
        points += 50

    if float(receipt["total"]) % 0.25 == 0:
        points += 25

    points += len(receipt["items"]) // 2 * 5

    for item in receipt["items"]:
        if len(item["shortDescription"].strip()) % 3 == 0:
            points += math.ceil(float(item["price"]) * 0.2)

    purchase_date = receipt["purchaseDate"]
    if int(purchase_date.split("-")[2]) % 2 != 0:
        points += 6

    purchase_time = receipt["purchaseTime"]
    if purchase_time > "14:00" and purchase_time < "16:00":
        points += 10

    return points
