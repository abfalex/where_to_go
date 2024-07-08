from django.shortcuts import render
from django.templatetags.static import static

from .models import Place, PlaceImage


def home(request):
    places = Place.objects.all()

    features = []
    for place in places:
        features.append(
            {
                "type": "Feature",
                "geometry": {"type": "Point", "coordinates": [place.lng, place.lat]},
                "properties": {
                    "title": place.title,
                    "placeId": place.place_id,
                    "detailsUrl": static(f"/places/{place.place_id}.json"),
                },
            }
        )

    geojson_data = {"type": "FeatureCollection", "features": features}

    context = {"geojson_data": geojson_data}

    return render(request, "places/index.html", context=context)
