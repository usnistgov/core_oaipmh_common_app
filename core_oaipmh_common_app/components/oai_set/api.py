"""
OaiSet API
"""

from core_oaipmh_common_app.components.oai_set.models import OaiSet
from core_main_app.commons import exceptions


def get_by_id(oai_set_id):
    """
    Get an OaiSet by its id
    :param oai_set_id:
    :return:
    """
    try:
        return OaiSet.get_by_id(oai_set_id)
    except:
        raise exceptions.ApiError('No OaiSet could be found with the given id')


def get_by_set_spec(set_spec):
    """
    Get an OaiSet by its setSpec
    :param set_spec:
    :return:
    """
    try:
        return OaiSet.get_by_set_spec(set_spec=set_spec)
    except:
        raise exceptions.ApiError('No OaiSet could be found with the given setSpec')


def get_all():
    """
    Get all OaiSets
    :return:
    """
    return OaiSet.get_all()
