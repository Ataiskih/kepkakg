# from django.db.models.signals import post_save
# from django.contrib.auth.models import User
# from order.models import Customer

# def create_customer(sender, instance, create, **kwargs):
#     if created:
#         Customer.objects.create(user=instance)
#         print('customer created')

# post_save.connect(create_customer, sender=User)

# def update_customer(sender, instance, created, **kwargs):
#     if created == False:
#         instance.customer.save()
#         print('customer updated')

# post_save.connect(update_customer, sender=User)