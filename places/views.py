import json
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.templatetags.static import static
from django.http.response import JsonResponse
from django.urls import reverse
from .models import Place, PlaceImage


def home(request):
    places = Place.objects.all()

    features = [
        {
            "type": "Feature",
            "geometry": {"type": "Point", "coordinates": [place.lng, place.lat]},
            "properties": {
                "title": place.title,
                "placeId": place.place_id,
                "detailsUrl": reverse("generate_place", args=[place.pk]),
            },
        }
        for place in places
    ]

    geojson_data = {"type": "FeatureCollection", "features": features}

    context = {"geojson_data": geojson_data}

    return render(request, "places/index.html", context=context)


def generate_place(request, place_id) -> JsonResponse:
    place = get_object_or_404(Place, pk=place_id)
    images = get_list_or_404(PlaceImage, place=place)
    place_details = {
        "title": place.title,
        "imgs": [str(image.image) for image in images if image.image],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {"lat": place.lat, "lng": place.lng},
    }

    return JsonResponse(
        place_details, json_dumps_params={"ensure_ascii": False, "indent": 4}
    )
