"""
OaiMetadataFormat model
"""
from django.core.exceptions import ObjectDoesNotExist
from django.db import models, IntegrityError

from core_main_app.commons import exceptions


class OaiMetadataFormat(models.Model):
    """Represents a metadata format for Oai-Pmh"""

    metadata_prefix = models.CharField(blank=False, max_length=200)
    schema = models.CharField(blank=False, max_length=200)
    xml_schema = models.TextField(blank=True)
    metadata_namespace = models.CharField(blank=False, max_length=200)

    class Meta:
        """Meta"""

        abstract = True

    @staticmethod
    def get_by_id(oai_metadata_format_id):
        """Get an OaiMetadataFormat by its id.

        Args:
            oai_metadata_format_id: OaiMetadataFormat id.

        Returns: The OaiMetadataFormat instance.

        Raises:
            DoesNotExist: The metadata format doesn't exist.
            ModelError: Internal error during the process.

        """
        try:
            return OaiMetadataFormat.objects.get(
                pk=str(oai_metadata_format_id)
            )
        except ObjectDoesNotExist as exception:
            raise exceptions.DoesNotExist(str(exception))
        except Exception as exception:
            raise exceptions.ModelError(str(exception))

    @staticmethod
    def get_by_metadata_prefix(metadata_prefix):
        """Get an OaiMetadataFormat by its metadata prefix.

        Args:
            metadata_prefix: OaiMetadataFormat metadata prefix.

        Returns: The OaiMetadataFormat instance.

        Raises:
            DoesNotExist: The metadata format doesn't exist.
            ModelError: Internal error during the process.

        """
        try:
            return OaiMetadataFormat.objects.get(
                metadata_prefix=metadata_prefix
            )
        except ObjectDoesNotExist as exception:
            raise exceptions.DoesNotExist(str(exception))
        except Exception as exception:
            raise exceptions.ModelError(str(exception))

    @staticmethod
    def get_all():
        """Return all OaiMetadataFormat

        Returns:
            List of OaiMetadataFormat.

        """
        return OaiMetadataFormat.objects.all()

    @staticmethod
    def get_all_by_list_ids(list_oai_metadata_format_ids):
        """Get all OaiMetadataFormat by a list of ids.

        Args:
            list_oai_metadata_format_ids:  List of ids.

        Returns:
            List of OaiMetadataFormat.

        """
        return OaiMetadataFormat.objects.filter(
            pk__in=list_oai_metadata_format_ids
        ).all()

    def save_object(self):
        """Custom save

        Returns:

        """
        try:
            return self.save()
        except IntegrityError as exception:
            raise exceptions.NotUniqueError(str(exception))
        except Exception as ex:
            raise exceptions.ModelError(str(ex))
