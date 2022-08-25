"""
OaiSet model
"""
from django.core.exceptions import ObjectDoesNotExist
from django.db import models

from core_main_app.commons import exceptions


class OaiSet(models.Model):
    """Represents a set for Oai-Pmh"""

    set_spec = models.CharField(blank=False, max_length=200)
    set_name = models.CharField(blank=False, max_length=200)

    class Meta:
        """Meta"""

        abstract = True
        unique_together = ("set_spec", "set_name")

    @staticmethod
    def get_by_id(oai_set_id):
        """Get an OaiSet by its id.

        Args:
            oai_set_id: OaiSet id.

        Returns: The OaiSet instance.

        Raises:
            DoesNotExist: The set doesn't exist
            ModelError: Internal error during the process

        """
        try:
            return OaiSet.objects.get(pk=str(oai_set_id))
        except ObjectDoesNotExist as exception:
            raise exceptions.DoesNotExist(str(exception))
        except Exception as exception:
            raise exceptions.ModelError(str(exception))

    @staticmethod
    def get_by_set_spec(set_spec):
        """Get an OaiSet by its set_spec.

        Args:
            set_spec: OaiSet set_spec.

        Returns: The OaiSet instance.

        Raises:
            DoesNotExist: The set doesn't exist
            ModelError: Internal error during the process

        """
        try:
            return OaiSet.objects.get(set_spec=set_spec)
        except ObjectDoesNotExist as exception:
            raise exceptions.DoesNotExist(str(exception))
        except Exception as exception:
            raise exceptions.ModelError(str(exception))

    @staticmethod
    def get_all():
        """Return all OaiSet

        Returns:
            List of OaiSet

        """
        return OaiSet.objects.all()

    @staticmethod
    def get_all_by_list_ids(list_oai_set_ids):
        """Return all OaiSet by a list of ids.

        Returns:
            List of OaiSet

        """
        return OaiSet.objects.filter(pk__in=list_oai_set_ids).all()
