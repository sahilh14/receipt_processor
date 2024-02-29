import re
import uuid
import json

from rest_framework import status
from rest_framework.response import Response
from jsonschema.exceptions import SchemaError
from rest_framework.decorators import api_view
from jsonschema import validate, ValidationError

from .services import calculate_points, receipt_schema

id_points = dict()


@api_view(["POST"])
def process_receipt(request):
    try:
        data = json.loads(request.body)
        validate(instance=data, schema=receipt_schema)
        random_uuid = uuid.uuid4()
        random_uuid_str = str(random_uuid)
        points = calculate_points(request.data)
        id_points[random_uuid_str] = points
        return Response({"id": random_uuid_str}, status=status.HTTP_200_OK)
    except ValidationError as e:
        return Response(
            {"message": "The receipt is invalid"}, status=status.HTTP_400_BAD_REQUEST
        )
    except SchemaError as e:
        return Response(
            {"message": "The receipt is invalid"}, status=status.HTTP_400_BAD_REQUEST
        )
    except Exception as e:
        return Response(
            {"message": "Error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(["GET"])
def get_points(request, id):

    if not re.match(r"^\S+$", id):
        return Response(
            {
                "message": "Invalid ID format. ID must consist of non-whitespace characters only."
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    data = {"points": id_points.get(str(id))}
    if data["points"] is None:
        return Response(
            {"message": "No receipt found for ID ({})".format(id)},
            status=status.HTTP_404_NOT_FOUND,
        )
    else:
        return Response(data, status=status.HTTP_200_OK)
