from django.db import models
import uuid
class Tag(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
        

class Parameter(models.Model):
    name = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag)
    def __str__(self):
        return self.name

        
class ParameterValueWeight(models.Model):
    name= models.CharField(max_length=50)
    parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE)
    value = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag)
    def __str__(self):
        return "{} --> ({}|{}|{})".format(self.name, self.parameter, self.value, self.weight)

class RiskRule(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, help_text="ID único")
    name = models.CharField(max_length=50)
    description = models.TextField()
    rules = models.ManyToManyField(ParameterValueWeight)
    tags = models.ManyToManyField(Tag)
    def __str__(self):
        return self.name