from django.db import models

# Create your models here.
#model => python class
#model represents a table in the db
#attributes are the fields in the table

#job posting table
#title, description, company, salary


class JobPosting(models.Model):
    #id - starts at 1 and autoincrements
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=100)
    salary = models.IntegerField()
    isActive = models.BooleanField(default=False)
    aboutUs = models.TextField()

    def __str__(self):
        return f"{self.title} | {self.company} | Active: {self.isActive}"


    #makemigrations => creates instructions telling django how the db have changed
    #migrate => applies above changes 

    #model manage -> objects
    #JobPosting.objects.all() or .get(id = 1), .filter(company = "tech")

