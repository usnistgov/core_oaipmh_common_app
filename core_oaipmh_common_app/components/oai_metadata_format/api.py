"""
OaiMetadataFormat API
"""

from core_oaipmh_common_app.components.oai_metadata_format.models import OaiMetadataFormat
from core_main_app.commons import exceptions


def get_by_id(oai_metadata_format_id):
    """
    Get an OaiMetadataFormat by its id
    :param oai_metadata_format_id:
    :return:
    """
    try:
        return OaiMetadataFormat.get_by_id(oai_metadata_format_id)
    except:
        raise exceptions.ApiError('No OaiMetadataFormat could be found with the given id')


def get_by_metadata_prefix(metadata_prefix):
    """
    Get an OaiMetadataFormat by its metadata prefix
    :param metadata_prefix:
    :return:
    """
    try:
        return OaiMetadataFormat.get_by_metadata_prefix(metadata_prefix=metadata_prefix)
    except:
        raise exceptions.ApiError('No OaiMetadataFormat could be found with the given metadata prefix')


def get_all():
    """
    Get all OaiMetadataFormat
    :return:
    """
    return OaiMetadataFormat.get_all()


def get_all_by_list_ids(list_oai_metadata_format_ids):
    """
    Get all OaiMetadataFormat by a list of ids
    :param list_oai_metadata_format_ids:
    :return:
    """
    try:
        return OaiMetadataFormat.get_all_by_list_ids(list_oai_metadata_format_ids)
    except:
        raise exceptions.ApiError('No OaiMetadataFormat could be found with the given list of ids')
