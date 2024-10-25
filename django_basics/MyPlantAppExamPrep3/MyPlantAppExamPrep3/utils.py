from MyPlantAppExamPrep3.profiles.models import Profile


def get_profile_object():
    return Profile.objects.all().first()
