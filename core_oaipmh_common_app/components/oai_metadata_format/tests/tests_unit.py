from unittest.case import TestCase
from bson.objectid import ObjectId
from mock.mock import Mock, patch
import core_oaipmh_common_app.components.oai_metadata_format.api as metadata_format_api
from core_main_app.commons import exceptions
from core_oaipmh_common_app.components.oai_metadata_format.models import OaiMetadataFormat


class TestOaiMetadataFormatGetById(TestCase):
    @patch('core_oaipmh_common_app.components.oai_metadata_format.models.OaiMetadataFormat.get_by_id')
    def test_oai_metadata_format_get_by_id_return_object(self, mock_get_by_id):
        # Arrange
        mock_oai_metadata_format = _create_mock_oai_metadata_format()

        mock_get_by_id.return_value = mock_oai_metadata_format

        # Act
        result = metadata_format_api.get_by_id(mock_get_by_id.id)

        # Assert
        self.assertIsInstance(result, OaiMetadataFormat)

    @patch('core_oaipmh_common_app.components.oai_metadata_format.models.OaiMetadataFormat.get_by_id')
    def test_oai_metadata_format_get_by_id_throws_exception_if_object_does_not_exist(self, mock_get_by_id):
        # Arrange
        mock_absent_id = ObjectId()

        mock_get_by_id.side_effect = Exception()

        # Act + Assert
        with self.assertRaises(exceptions.ApiError):
            metadata_format_api.get_by_id(mock_absent_id)


class TestOaiMetadataFormatGetByMetadataPrefix(TestCase):
    @patch('core_oaipmh_common_app.components.oai_metadata_format.models.OaiMetadataFormat.get_by_metadata_prefix')
    def test_oai_metadata_format_get_by_metadata_prefix_return_object(self, mock_get_by_metadata_prefix):
        # Arrange
        mock_oai_metadata_format = _create_mock_oai_metadata_format()

        mock_get_by_metadata_prefix.return_value = mock_oai_metadata_format

        # Act
        result = metadata_format_api.get_by_metadata_prefix(mock_get_by_metadata_prefix.MetadataPrefix)

        # Assert
        self.assertIsInstance(result, OaiMetadataFormat)

    @patch('core_oaipmh_common_app.components.oai_metadata_format.models.OaiMetadataFormat.get_by_metadata_prefix')
    def test_oai_metadata_format_get_by_metadata_prefix_throws_exception_if_object_does_not_exist(self, mock_get_by):
        # Arrange
        mock_absent_metadata_prefix = "oai_test"

        mock_get_by.side_effect = Exception()

        # Act + Assert
        with self.assertRaises(exceptions.ApiError):
            metadata_format_api.get_by_id(mock_absent_metadata_prefix)


class TestOaiMetadataFormatGetAll(TestCase):
    @patch('core_oaipmh_common_app.components.oai_metadata_format.models.OaiMetadataFormat.get_all')
    def test_oai_metadata_format_get_all_contains_only_oai_metadata_format(self, mock_get_all):
        # Arrange
        mock_oai_metadata_format1 = _create_mock_oai_metadata_format()
        mock_oai_metadata_format2 = _create_mock_oai_metadata_format()

        mock_get_all.return_value = [mock_oai_metadata_format1, mock_oai_metadata_format2]

        # Act
        result = metadata_format_api.get_all()

        # Assert
        self.assertTrue(all(isinstance(item, OaiMetadataFormat) for item in result))


class TestOaiMetadataFormatGetAllByListIds(TestCase):
    @patch('core_oaipmh_common_app.components.oai_metadata_format.models.OaiMetadataFormat.get_all_by_list_ids')
    def test_oai_metadata_format_get_all_by_list_ids_contains_only_oai_metadata_format(self, mock_get_all):
        # Arrange
        mock_oai_metadata_format1 = _create_mock_oai_metadata_format()
        mock_oai_metadata_format2 = _create_mock_oai_metadata_format()
        list_ids = [ObjectId(), ObjectId()]

        mock_get_all.return_value = [mock_oai_metadata_format1, mock_oai_metadata_format2]

        # Act
        result = metadata_format_api.get_all_by_list_ids(list_ids)

        # Assert
        self.assertTrue(all(isinstance(item, OaiMetadataFormat) for item in result))


def _create_mock_oai_metadata_format():
    """
    Mock an OaiMetadataFormat object
    :return:
    """
    mock_oai_metadata_format = Mock(spec=OaiMetadataFormat)
    mock_oai_metadata_format.id = ObjectId()
    mock_oai_metadata_format.metadataPrefix = "oai_test"
    mock_oai_metadata_format.schema = "http://addressToMySchema/schema.xsd"
    mock_oai_metadata_format.xmlSchema = "<root><test><test></root>"
    mock_oai_metadata_format.xmlSchema = "testNamespace"

    return mock_oai_metadata_format
