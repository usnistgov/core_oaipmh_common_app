"""
OaiMetadataFormat model
"""

from django_mongoengine import fields, Document


class OaiMetadataFormat(Document):
    """Represents a metadata format for Oai-Pmh"""
    metadataPrefix = fields.StringField(unique=True)
    schema = fields.StringField()
    xmlSchema = fields.StringField()
    metadataNamespace = fields.StringField()

    meta = {'allow_inheritance': True}

    @staticmethod
    def get_by_id(oai_metadata_format_id):
        """
        Get an OaiMetadataFormat by its id
        :param oai_metadata_format_id:
        :return:
        """
        return OaiMetadataFormat.objects().get(pk=str(oai_metadata_format_id))

    @staticmethod
    def get_by_metadata_prefix(metadata_prefix):
        """
        Get an OaiMetadataFormat by its metadata prefix
        :param metadata_prefix:
        :return:
        """
        return OaiMetadataFormat.objects().get(metadataPrefix=metadata_prefix)

    @staticmethod
    def get_all():
        """
        Return all OaiMetadataFormat
        :return:
        """
        return OaiMetadataFormat.objects().all()

    @staticmethod
    def get_all_by_list_ids(list_oai_metadata_format_ids):
        """
        Get all OaiMetadataFormat by a list of ids
        :param list_oai_metadata_format_ids:
        :return:
        """
        return OaiMetadataFormat.objects(pk__in=list_oai_metadata_format_ids).all()
