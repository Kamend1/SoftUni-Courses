from MyMusicAppExamPrep1.profile.models import Profile


def get_object():
    return Profile.objects.all().first()