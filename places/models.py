from django.db import models


class Place(models.Model):
    title = models.CharField("Название", max_length=255, blank=True)
    place_id = models.CharField("Айди", max_length=255, blank=True)
    description_short = models.TextField("Короткое описание", blank=True)
    description_long = models.TextField("Длинное описание", blank=True)
    lat = models.FloatField("Широта", blank=True)
    lng = models.FloatField("Долгота", blank=True)

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField("Изображения", upload_to="media", blank=True, null=True)

    def __str__(self):
        return f"{self.place.id} {self.place.title}"
