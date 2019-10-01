from django.contrib import admin
from .models import Tag, Parameter, ParameterValueWeight, RiskRule
# Register your models here.

admin.site.register(Tag)
admin.site.register(Parameter)
admin.site.register(ParameterValueWeight)
admin.site.register(RiskRule)