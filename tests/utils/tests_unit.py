from os.path import join, dirname
from unittest import TestCase
from mock.mock import patch
from xml_utils.xsd_flattener.xsd_flattener_url import XSDFlattenerURL
from core_oaipmh_common_app.utils.xsd_flattener_database_url import XSDFlattenerDatabaseOrURL
from core_main_app.components.template import api as template_api
from core_main_app.components.template.models import Template
from core_main_app.commons import exceptions

RESOURCES_PATH = join(dirname(__file__), 'data')


class TestXSDFlattenerDatabaseOrUrl(TestCase):
    @patch.object(template_api, 'get')
    def test_get_dependency_uses_database(self, mock_get_):
        # Arrange
        xml_string = '<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">' \
                     '<xs:include schemaLocation="http://server/rest/api?template=test.xsd"/></xs:schema>'

        dependency = '<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">' \
                     '<xs:element name="test"/></xs:schema>'

        # Act
        template = Template(content=dependency)
        mock_get_.return_value = template
        flattener = XSDFlattenerDatabaseOrURL(xml_string)
        flat_string = flattener.get_flat()

        # Assert
        self.assertTrue('<xs:element name="test"/>' in flat_string)

    @patch.object(template_api, 'get')
    @patch.object(XSDFlattenerURL, 'get_dependency_content')
    def test_get_dependency_uses_url(self, mock_get_dependency_content, mock_get_):
        # Arrange
        xml_string = '<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">' \
                     '<xs:include schemaLocation="http://server/rest/api?template=test.xsd"/></xs:schema>'

        dependency = '<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">' \
                     '<xs:element name="test"/></xs:schema>'

        # Act
        mock_get_.side_effect = exceptions.DoesNotExist("Error")
        mock_get_dependency_content.return_value = dependency
        flattener = XSDFlattenerDatabaseOrURL(xml_string)
        flat_string = flattener.get_flat()

        # Assert
        self.assertTrue('<xs:element name="test"/>' in flat_string)
