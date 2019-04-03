from django.db import models
from django.conf import settings


class WaterTypes(models.Model):
    water_type = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Water Type'
        verbose_name_plural = 'Water Types'

    def __str__(self):
        return self.water_type


class ServiceLocation(models.Model):
    water_type = models.ManyToManyField(WaterTypes)
    location = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Service Location'
        verbose_name_plural = 'Service Locations'

    def __str__(self):
        return self.location


class BoatSpec(models.Model):
    length = models.IntegerField()
    capacity = models.IntegerField()
    boat_description = models.TextField(max_length=250)

    class Meta:
        verbose_name = 'Boat Specification'
        verbose_name_plural = 'Boat Specifications'

    def __str__(self):
        return self.boat_description


class FishingType(models.Model):
    type = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Fishing Type'
        verbose_name_plural = 'Fishing Types'

    def __str__(self):
        return self.type


class FishingTechnique(models.Model):
    technique = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Fishing Technique'
        verbose_name_plural = 'Fishing Techniques'

    def __str__(self):
        return self.technique


class Amenities(models.Model):
    amenities = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Amenities'
        verbose_name_plural = 'Amenities'

    def __str__(self):
        return self.amenities


class TripeInclude(models.Model):
    includes = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Trip Includes'
        verbose_name_plural = 'Trip Includes'

    def __str__(self):
        return self.includes


class Policy(models.Model):
    policy_title = models.CharField(max_length=50)
    policy_description = models.TextField(max_length=250)

    class Meta:
        verbose_name = 'Policy'
        verbose_name_plural = 'Policies'

    def __str__(self):
        return self.policy_title


class GuideBusiness(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    location_city = models.CharField(max_length=150)
    location_state = models.CharField(max_length=50)
    service_location = models.ManyToManyField(ServiceLocation)
    business_description = models.TextField(max_length=1500)
    boat_spec = models.ManyToManyField(BoatSpec)
    fishing_type = models.ManyToManyField(FishingType)
    fishing_technique = models.ManyToManyField(FishingTechnique)
    amenities = models.ManyToManyField(Amenities)
    trip_includes = models.ManyToManyField(TripeInclude)
    policy = models.ManyToManyField(Policy)

    class Meta:
        verbose_name_plural = 'Guide Businesses'

    def __str__(self):
        return self.user

