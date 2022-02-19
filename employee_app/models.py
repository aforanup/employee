from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    cv = models.FileField(upload_to="cv/")
    photo = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.name


class SkillSet(models.Model):
    profile = models.ForeignKey(
        Profile, related_name='employeeProfile', on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=255)
    proficiency_level = models.IntegerField()

    def __str__(self):
        return self.profile.name
