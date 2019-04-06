from django.contrib import admin
from .models import (GuideBusiness, ServiceLocation, WaterTypes, BoatSpec, FishingType, FishingTechnique,
                     Amenities, TripeInclude, Policy, Trip)

admin.site.register(GuideBusiness)
admin.site.register(WaterTypes)
admin.site.register(ServiceLocation)
admin.site.register(BoatSpec)
admin.site.register(FishingType)
admin.site.register(FishingTechnique)
admin.site.register(Amenities)
admin.site.register(TripeInclude)
admin.site.register(Policy)
admin.site.register(Trip)
