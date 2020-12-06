from django.db import models
from multiselectfield import MultiSelectField
from phone_field import PhoneField
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
def validate_phone(value):
    if len(value)<10 or not value.isdigit():
        raise ValidationError(
            _('enter correct phone number please!'),
            params={'value': value},
        
        )
def validate_fname(value):
    contains_digit = False

    for character in value:
        if character.isdigit():
            contains_digit = True

    if len(value)<3 or contains_digit:
        raise ValidationError(
            _('incorrect first name input'),
            params={'value': value},
        ) 
def validate_lname(value):
    contains_digit = False

    for character in value:
        if character.isdigit():
            contains_digit = True
    if len(value)<3 or contains_digit:
        raise ValidationError(
            _('incorrect last name input'),
            params={'value': value},
        )           
# Create your models here.
SKILLS =(('Python', 'Python'),
              ('React', 'React'),
              ('Angular', 'Angular'),
              ('Redux', 'Redux'),
              ('Expert in css', 'Expert in css'),
              ('Graphic Design', 'Graphic Design'),
              ('Photo Editing', 'Photo Editing'),
              ('Firebase', 'Firebase'))

class Developers(models.Model):
    first_name = models.CharField(max_length=100, validators=[validate_fname])
    last_name = models.CharField(max_length=100, validators=[validate_lname])
    email = models.EmailField()
    skills = MultiSelectField(choices=SKILLS, max_choices=2)
    phone_number = models.CharField(max_length=20 ,validators=[validate_phone])

    def __str__(self):
        return self.first_name