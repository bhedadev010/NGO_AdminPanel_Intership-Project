from django.db import models

# Create your models here.


class category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class country(models.Model):
    name = models.CharField(max_length=50)


class state(models.Model):
    name = models.CharField(max_length=50)
    country_name = models.ForeignKey(country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class city(models.Model):
    name = models.CharField(max_length=50)
    state_name = models.ForeignKey(state, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class volunteer(models.Model):

    gender_choices = {
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others')

    }

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.BigIntegerField()
    gender = models.CharField(max_length=50, choices=gender_choices)
    description = models.CharField(max_length=100)
    city = models.ForeignKey(city, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ngo(models.Model):
    ngo_name = models.CharField(max_length=100)
    ngo_category = models.CharField(max_length=100)
    ngo_address = models.TextField(max_length=200)
    ngo_city = models.CharField(max_length=50)
    ngo_website = models.URLField(max_length=100)

    def __str__(self):
        return self.ngo_name


class donor(models.Model):

    donor_gender_choices = {
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others')

    }

    donor_name = models.CharField(max_length=50)
    donor_email = models.EmailField()
    donor_phone = models.BigIntegerField()
    donor_gender = models.CharField(max_length=50, choices=donor_gender_choices)
    city = models.ForeignKey(city, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.donor_name


class donation(models.Model):
    donor_name = models.ForeignKey(donor, on_delete=models.CASCADE)
    ngo_name = models.ForeignKey(ngo, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return self.donor_name

