from django.db import models
from django.contrib.auth.models import User

PRODUCT_CHOICES = (
    # What database sees, what we see
    ('TV', 'tv'),
    ('IPAD', 'ipad'),
    ('XBOX', 'xbox')
)

class Sale(models.Model):
    product = models.CharField(max_length=20, choices=PRODUCT_CHOICES)
    salesperson = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total = models.FloatField(blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product}-{self.quantity}"

    # overwrite save() method
    def save(self, *args, **kwargs):
        price = None
        if self.product == 'TV':
            price = 559.99
        elif self.product == 'IPAD':
            price = 399.99
        elif self.product == 'XBOX':
            price = 499.99
        else:
            pass

        self.total = price * self.quantity
        super.save(*args, **kwargs)


