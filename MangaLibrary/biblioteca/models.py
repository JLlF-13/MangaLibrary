from django.db import models
#python manage.py migrate
#python manage.py loaddata biblioteca/fixtures/initial_data.json

class Status(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id}: {self.name}"

class Origin(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id}: {self.name}"
    
class Language(models.Model):
    name = models.CharField(max_length=50)
    name_short = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.id}: {self.name}"
    
class Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id}: {self.name}"


class Manga(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='uploads/')
    observations = models.TextField(null=True, blank=True)
    owned = models.IntegerField()
    total_books = models.IntegerField()
    avg_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_spend = models.DecimalField(max_digits=10, decimal_places=2)
    status_id = models.ForeignKey(Status, on_delete=models.CASCADE)    
    origin_id = models.ForeignKey(Origin, on_delete=models.CASCADE)  
    language_id = models.ForeignKey(Language, on_delete=models.CASCADE)
    type_id = models.ForeignKey(Type, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    


