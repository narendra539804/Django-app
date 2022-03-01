from django.db import models

# Create your models here.
Food_CHOICES = (
    ("1", "Veg"),
    ("2", "Fruit"),
    ("3", "Grain"),
    ("4", "Protein"),
    ("5", "Dairy"),
    ("6", "Confectionery"),
    ("7", "Unknown"),
)

class KidData(models.Model):
    KidName = models.CharField(max_length=128)
    KigAge=models.CharField(max_length=128)
    ParentPhoneNumber=models.CharField(max_length=128)
    ParentEmailAddress=models.EmailField()
    
    def __str__(self):
        return self.KidName
    
class ImageTable(models.Model):
    KidName=models.ForeignKey(KidData,on_delete=models.CASCADE)
    ImageURL = models.ImageField(blank=True, null=True, upload_to='media')
    FoodGroup = models.CharField(
        max_length = 20,
        choices = Food_CHOICES,
        default = '1'
        )
    CreatedOn=models.DateField()
    UpdatedOn=models.DateField()
    IsApproved=models.CharField(max_length=128)
    ApprovedBy=models.CharField(max_length=128)
    
    def __str__(self):
        return self.ApprovedBy
    