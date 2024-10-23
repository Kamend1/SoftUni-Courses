from TastyRecipesAppExamPrep17042024.profiles.models import Profile


def get_profile_object():
    return Profile.objects.all().first()
