from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from helper.bas_models import AbstractModel
from helper.model_validator import validate_phone


class ProjectUserManager(BaseUserManager):

    def create_user(self, username, password=None):
        """Creates and saves a User with the given username and password."""

        if not username:
            raise ValueError('Users must have username')

        user = self.model(
            username=username
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """Creates and saves a superuser with the given username and password."""

        user = self.create_user(username=username, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class ProjectUser(AbstractModel, AbstractUser):
    phone = models.CharField(verbose_name=_('phone'),
                             validators=[validate_phone],
                             max_length=15, unique=True, blank=True, null=True)

    REQUIRED_FIELDS = []

    objects = ProjectUserManager()

    def __str__(self):
        """returns a Unicode “representation” of ProjectUser object."""
        full_name = self.get_full_name()
        if full_name:
            return "{} - {}".format(self.username, full_name)
        return "{}".format(self.username)


class Address(AbstractModel):
    user = models.ForeignKey(ProjectUser, on_delete=models.CASCADE, related_name='addresses')
    title = models.CharField(max_length=200, blank=True, null=True)
    create_by = models.ForeignKey(ProjectUser, on_delete=models.CASCADE)
    latitude = models.FloatField(min_value=-90, max_value=90)
    longitude = models.FloatField(min_value=-180, max_value=180)

    @property
    def type_of_creator(self):
        return "staff" if self.create_by.is_staff else "user"
