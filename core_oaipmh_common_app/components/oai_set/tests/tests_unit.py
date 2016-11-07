from unittest.case import TestCase
from bson.objectid import ObjectId
from mock.mock import Mock, patch
from core_oaipmh_common_app.components.oai_set.api import get_by_id, get_all, get_by_set_spec
from core_main_app.commons.exceptions import MDCSError
from core_oaipmh_common_app.components.oai_set.models import OaiSet


class TestOaiSetGet(TestCase):

    @patch('core_oaipmh_common_app.components.oai_set.models.OaiSet.get_by_id')
    def test_oai_set_get_by_id_return_object(self, mock_get_by_id):
        # Arrange
        mock_oai_set = _get_oai_set_mock()

        mock_get_by_id.return_value = mock_oai_set

        # Act
        result = get_by_id(mock_get_by_id.id)

        # Assert
        self.assertIsInstance(result, OaiSet)

    @patch('core_oaipmh_common_app.components.oai_set.models.OaiSet.get_by_id')
    def test_oai_set_get_by_id_throws_exception_if_object_does_not_exist(self, mock_get_by_id):
        # Arrange
        mock_absent_id = ObjectId()

        mock_get_by_id.side_effect = Exception()

        # Act + Assert
        with self.assertRaises(MDCSError):
            get_by_id(mock_absent_id)

    @patch('core_oaipmh_common_app.components.oai_set.models.OaiSet.get_by_set_spec')
    def test_oai_set_get_by_set_spec_return_object(self, mock_get_by_set_spec):
        # Arrange
        mock_oai_set = _get_oai_set_mock()

        mock_get_by_set_spec.return_value = mock_oai_set

        # Act
        result = get_by_set_spec(mock_get_by_set_spec.setSpec)

        # Assert
        self.assertIsInstance(result, OaiSet)

    @patch('core_oaipmh_common_app.components.oai_set.models.OaiSet.get_by_set_spec')
    def test_oai_set_get_by_set_spec_throws_exception_if_object_does_not_exist(self, mock_get_by_set_spec):
        # Arrange
        mock_absent_set_spec = "oai_test"

        mock_get_by_set_spec.side_effect = Exception()

        # Act + Assert
        with self.assertRaises(MDCSError):
            get_by_id(mock_absent_set_spec)


class TestOaiSetList(TestCase):
    @patch('core_oaipmh_common_app.components.oai_set.models.OaiSet.get_all')
    def test_oai_set_list_contains_only_oai_set(self, mock_get_all):
        # Arrange
        mock_oai_set1 = _get_oai_set_mock()
        mock_oai_set2 = _get_oai_set_mock()

        mock_get_all.return_value = [mock_oai_set1, mock_oai_set2]

        # Act
        result = get_all()

        # Assert
        self.assertTrue(all(isinstance(item, OaiSet) for item in result))


def _get_oai_set_mock():
    """
    Mock an OaiSet object
    :return:
    """
    mock_oai_set = Mock(spec=OaiSet)
    mock_oai_set.setSpec = "oai_test"
    mock_oai_set.setName = "test"
    mock_oai_set.id = ObjectId()

    return mock_oai_set
