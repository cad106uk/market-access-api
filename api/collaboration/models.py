from django.conf import settings
from django.db import models
from django.db.models import Q

from simple_history.models import HistoricalRecords

from api.core.models import ArchivableModel, BaseModel
from api.barriers.models import BarrierInstance

MAX_LENGTH = settings.CHAR_FIELD_MAX_LENGTH


class TeamMemberManager(models.Manager):
    """ Manage barrier team member within the model, with archived not False """

    def get_queryset(self):
        return super(TeamMemberManager, self).get_queryset().filter(Q(archived=False))


class TeamMember(BaseModel, ArchivableModel):
    """ TeamMember records for each Barrier """

    barrier = models.ForeignKey(
        BarrierInstance, related_name="barrier_team", on_delete=models.PROTECT
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    role = models.CharField(max_length=MAX_LENGTH, null=True)
    default = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    history = HistoricalRecords()

    objects = TeamMemberManager()

    @property
    def created_user(self):
        return self._cleansed_username(self.created_by)

    @property
    def modified_user(self):
        return self._cleansed_username(self.modified_by)