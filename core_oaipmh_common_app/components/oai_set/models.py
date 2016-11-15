"""
OaiSet model
"""

from django_mongoengine import fields, Document


class OaiSet(Document):
    """Represents a set for Oai-Pmh"""
    setSpec = fields.StringField(unique=True)
    setName = fields.StringField(unique=True)

    meta = {'allow_inheritance': True}

    @staticmethod
    def get_by_id(oai_set_id):
        """
        Get an OaiSet by its id
        :param oai_set_id:
        :return:
        """
        return OaiSet.objects().get(pk=str(oai_set_id))

    @staticmethod
    def get_by_set_spec(set_spec):
        """
        Get an OaiSet by its setSpec
        :param set_spec:
        :return:
        """
        return OaiSet.objects().get(setSpec=set_spec)

    @staticmethod
    def get_all():
        """
        Return all OaiSets
        :return:
        """
        return OaiSet.objects().all()

    @staticmethod
    def get_all_by_list_ids(list_oai_set_ids):
        """
        Get all OaiSet by a list of ids
        :param list_oai_set_ids:
        :return:
        """
        return OaiSet.objects(pk__in=list_oai_set_ids).all()
