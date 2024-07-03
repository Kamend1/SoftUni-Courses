from django.contrib import admin

from main_app.models import Car


# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'year', 'owner', 'car_details')

    @staticmethod
    def car_details(obj: object):
        owner_name = 'No owner'
        registration = 'No registration'

        try:
            owner_name = obj.owner.name
        except AttributeError:
            pass

        try:
            registration = obj.registration.registration_number
        except AttributeError:
            pass

        return f"Owner: {owner_name}, Registration: {registration}"

    car_details.short_description = 'Car Details'
