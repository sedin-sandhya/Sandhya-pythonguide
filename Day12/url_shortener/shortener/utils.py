import random
import string

from .models import ShortURL


def generate_short_code():
    characters = string.ascii_letters + string.digits

    while True:
        code = "".join(random.choices(characters, k=6))

        if not ShortURL.objects.filter(short_code=code).exists():
            return code
