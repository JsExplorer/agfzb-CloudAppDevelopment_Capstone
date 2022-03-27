from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    name=models.CharField(null=False,max_length=30)
    description=models.CharField(null=False,max_length=100)

    def __str__(self):
        return "Make: " + self.name + "," + "\n Description: " + self.description

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    SEDAN='Sedan'
    SUV='Suv'
    WAGON='Wagon'
    STYLE_CHOICES=[
        (SEDAN,'Sedan'),
        (WAGON,'Wagon'),
        (SUV,'Suv')
    ]
    
    make=models.ForeignKey(CarMake,null=False,on_delete=models.CASCADE)
    dealer_id=models.IntegerField()
    model_name=models.CharField(null=False,max_length=30)
    style=models.CharField(
        null=False,
        max_length=20,
        choices=STYLE_CHOICES,
        default=SUV
    )
    year=models.DateField(default=now)

    def __str__(self):
        return "Make: " + str(self.make) + "," + "\n DealerId: " + str(self.dealer_id) + "," + "\n Model: " + self.model_name + "," + "\n Style: " + self.style + "," + "\n Year: " + str(self.year)


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
