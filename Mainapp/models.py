from django.db import models
from django.contrib.auth.models import(AbstractBaseUser)
from django.utils.timezone import now
from django.contrib.auth.models import User,auth

# Create your models here.




class Tenent(AbstractBaseUser) :

    Select_Gender   =(
        ('M','Male') , ('F','Female') , ('O' , 'Other')
    )


    first_name              = models.CharField(max_length=30)
    last_name               = models.CharField(max_length=30)
    phone                   = models.CharField(max_length=12)
    email                   = models.CharField(max_length=120, unique = True)
    USERNAME_FIELD          = 'email' # default username
    gender                  = models.CharField(max_length=1, choices = Select_Gender)
    maried                  = models.BooleanField(default = False)
    home_address            = models.TextField(max_length=200 , blank = True)
    highest_education       = models.CharField(max_length=20 , blank = True)
    empolybility            = models.CharField(max_length=50 , blank = True)
    work_address            = models.TextField(max_length=200 , blank = True)
    profile_image           = models.ImageField(upload_to='profiles',default='profile.jpg')


    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Owner(AbstractBaseUser) :

    Select_Gender_avilability   =(
                    ('M','Male') , ('F','Female') , ('B' , 'Both')
                )

    states = (
                    ('Maharashtra','Maharashtra'),
            )
    districts = (
                    ('nanded','nanded'),('nagpur','nagpur'),
                )

    cities = (
                ('vishnupuri','vishnupuri'),
            )


    first_name              = models.CharField(max_length=30)
    last_name               = models.CharField(max_length=30)
    phone                   = models.CharField(max_length=12)
    email                   = models.CharField(max_length=120, unique = True)
    USERNAME_FIELD          = 'email' # default username
    availibility_for_gender = models.CharField(max_length=1, choices = Select_Gender_avilability)
    state                   = models.CharField(max_length=50, choices = states)
    district                = models.CharField(max_length=50, choices = districts)
    city                    = models.CharField(max_length=50, choices = cities)
    home_address            = models.TextField(max_length=200 , blank = True)
    profile_image           = models.ImageField(upload_to='profiles',default='profile.jpg')


    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Property(models.Model) :

    states      = (('Maharashtra','Maharashtra'),)
    districts   = (('nanded','nanded'),('nagpur','nagpur'),)
    cities       = (('vishnupuri','vishnupuri'),)

    proptype = (('room','Room Basis'),('cot','Cot Basis'))

    owner                   = models.ForeignKey(Owner , on_delete = models.CASCADE)
    number_of_props         = models.IntegerField()
    rent_amount             = models.IntegerField()
    type                    = models.CharField(max_length = 50, choices = proptype)
    state                   = models.CharField(max_length=50, null=True, choices = states)
    district                = models.CharField(max_length=50, null=True, choices = districts)
    city                    = models.CharField(max_length=50, null=True , choices = cities)
    landmark                = models.TextField(max_length=120,blank = True)
    image                   = models.ImageField(upload_to = 'property',default='propdef.jpg')
