from unittest.case import TestCase

from unittest.mock import Mock, patch

from core_main_app.commons import exceptions
import core_oaipmh_common_app.components.oai_metadata_format.api as metadata_format_api
from core_oaipmh_common_app.components.oai_metadata_format.models import (
    OaiMetadataFormat,
)


class TestOaiMetadataFormatGetById(TestCase):
    """Test Oai Meta data Format Get By Id"""

    @patch.object(OaiMetadataFormat, "get_by_id")
    def test_oai_metadata_format_get_by_id_return_object(self, mock_get_by_id):
        """test_oai_metadata_format_get_by_id_return_object"""

        # Arrange
        mock_oai_metadata_format = _create_mock_oai_metadata_format()

        mock_get_by_id.return_value = mock_oai_metadata_format

        # Act
        result = metadata_format_api.get_by_id(mock_get_by_id.id)

        # Assert
        self.assertIsInstance(result, OaiMetadataFormat)

    @patch.object(OaiMetadataFormat, "get_by_id")
    def test_oai_metadata_format_get_by_id_raises_exception_if_object_does_not_exist(
        self, mock_get_by_id
    ):
        """test_oai_metadata_format_get_by_id_raises_exception_if_object_does_not_exist"""

        # Arrange
        mock_absent_id = 1

        mock_get_by_id.side_effect = exceptions.DoesNotExist("Error")

        # Act + Assert
        with self.assertRaises(exceptions.DoesNotExist):
            metadata_format_api.get_by_id(mock_absent_id)

    @patch.object(OaiMetadataFormat, "get_by_id")
    def test_oai_metadata_format_get_by_id_raises_exception_if_internal_error(
        self, mock_get_by_id
    ):
        """test_oai_metadata_format_get_by_id_raises_exception_if_internal_error"""

        # Arrange
        mock_absent_id = 1

        mock_get_by_id.side_effect = exceptions.ModelError("Error")

        # Act + Assert
        with self.assertRaises(exceptions.ModelError):
            metadata_format_api.get_by_id(mock_absent_id)


class TestOaiMetadataFormatGetByMetadataPrefix(TestCase):
    """Test Oai Metadata Format Get By Metadata Prefix"""

    @patch.object(OaiMetadataFormat, "get_by_metadata_prefix")
    def test_oai_metadata_format_get_by_metadata_prefix_return_object(
        self, mock_get_by_metadata_prefix
    ):
        """test_oai_metadata_format_get_by_metadata_prefix_return_object"""

        # Arrange
        mock_oai_metadata_format = _create_mock_oai_metadata_format()

        mock_get_by_metadata_prefix.return_value = mock_oai_metadata_format

        # Act
        result = metadata_format_api.get_by_metadata_prefix(
            mock_get_by_metadata_prefix.metadata_prefix
        )

        # Assert
        self.assertIsInstance(result, OaiMetadataFormat)

    @patch.object(OaiMetadataFormat, "get_by_metadata_prefix")
    def test_oai_metadata_format_get_by_metadata_prefix_raises_exception_if_object_does_not_exist(
        self, mock_get_by
    ):
        """test_oai_metadata_format_get_by_metadata_prefix_raises_exception_if_object_does_not_exist"""

        # Arrange
        mock_absent_metadata_prefix = "oai_test"

        mock_get_by.side_effect = exceptions.DoesNotExist("Error")

        # Act + Assert
        with self.assertRaises(exceptions.DoesNotExist):
            metadata_format_api.get_by_metadata_prefix(
                mock_absent_metadata_prefix
            )

    @patch.object(OaiMetadataFormat, "get_by_metadata_prefix")
    def test_oai_metadata_format_get_by_metadata_prefix_raises_exception_if_internal_error(
        self, mock_get_by
    ):
        """test_oai_metadata_format_get_by_metadata_prefix_raises_exception_if_internal_error"""

        # Arrange
        mock_absent_metadata_prefix = "oai_test"

        mock_get_by.side_effect = exceptions.ModelError("Error")

        # Act + Assert
        with self.assertRaises(exceptions.ModelError):
            metadata_format_api.get_by_metadata_prefix(
                mock_absent_metadata_prefix
            )


class TestOaiMetadataFormatGetAll(TestCase):
    """Test Oai Metadata Format Get All"""

    @patch.object(OaiMetadataFormat, "get_all")
    def test_oai_metadata_format_get_all_contains_only_oai_metadata_format(
        self, mock_get_all
    ):
        """test_oai_metadata_format_get_all_contains_only_oai_metadata_format"""

        # Arrange
        mock_oai_metadata_format1 = _create_mock_oai_metadata_format()
        mock_oai_metadata_format2 = _create_mock_oai_metadata_format()

        mock_get_all.return_value = [
            mock_oai_metadata_format1,
            mock_oai_metadata_format2,
        ]

        # Act
        result = metadata_format_api.get_all()

        # Assert
        self.assertTrue(
            all(isinstance(item, OaiMetadataFormat) for item in result)
        )


class TestOaiMetadataFormatGetAllByListIds(TestCase):
    """Test Oai Metadata Format Get All By List Ids"""

    @patch.object(OaiMetadataFormat, "get_all_by_list_ids")
    def test_oai_metadata_format_get_all_by_list_ids_contains_only_oai_metadata_format(
        self, mock_get_all
    ):
        """test_oai_metadata_format_get_all_by_list_ids_contains_only_oai_metadata_format"""

        # Arrange
        mock_oai_metadata_format1 = _create_mock_oai_metadata_format()
        mock_oai_metadata_format2 = _create_mock_oai_metadata_format()
        list_ids = [1, 2]

        mock_get_all.return_value = [
            mock_oai_metadata_format1,
            mock_oai_metadata_format2,
        ]

        # Act
        result = metadata_format_api.get_all_by_list_ids(list_ids)

        # Assert
        self.assertTrue(
            all(isinstance(item, OaiMetadataFormat) for item in result)
        )


def _create_mock_oai_metadata_format():
    """Mock an OaiMetadataFormat.

    Returns:
        OaiMetadataFormat mock.

    """
    mock_oai_metadata_format = Mock(spec=OaiMetadataFormat)
    mock_oai_metadata_format.id = 1
    mock_oai_metadata_format.metadata_prefix = "oai_test"
    mock_oai_metadata_format.schema = "http://addressToMySchema/schema.xsd"
    mock_oai_metadata_format.xml_schema = "<root><test><test></root>"
    mock_oai_metadata_format.metadata_namespace = "testNamespace"

    return mock_oai_metadata_format
