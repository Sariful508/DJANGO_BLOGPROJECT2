from django.utils.text import slugify
from .models import *
import string
import random

def generate_random_string(N):
    res = ''.join(random.choices(string.ascii_lowercase +
                             string.punctuation, k=N))
    return res

# print result

print("The generated random string:-> " + str(res))

def generate_slug(text):
    new_slug = slugify(text)
    if BlogModel.objects.filter(slug = new_slug).exists():
        generate_slug(text +generate_random_string(5))
        return new_slug()
