import unittest
import argparse
from unittest.mock import patch, call
from pathlib import Path
import src.yaml_toml.yaml_toml as yaml_toml

class TestYamlToToml(unittest.TestCase):
    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data='key: value')
    @patch('toml.dump')
    def test_convert_yaml_to_toml(self, mock_toml_dump, mock_open):
        # Convert a test YAML file
        yaml_toml.convert_yaml_to_toml(Path('test.yml'), Path('test.toml'))

        # Check that the YAML file was read correctly
        mock_open.assert_called_once_with(Path('test.yml'), 'r')

        # Check that the correct data was written to the TOML file
        mock_toml_dump.assert_called_once_with({'key': 'value'}, unittest.mock.ANY)

    @patch('src.yaml_toml.yaml_toml.convert_yaml_to_toml')
    def test_convert_file(self, mock_convert_yaml_to_toml):
        # Convert a test file
        yaml_toml.convert_file(Path('test.yml'), Path('outputs'), False)

        # Check that convert_yaml_to_toml was called with the correct arguments
        mock_convert_yaml_to_toml.assert_called_once_with(Path('test.yml'), Path('outputs/test.toml'))

    @patch('argparse.ArgumentParser.parse_args')
    def test_parse_arguments(self, mock_parse_args):
        # Create a mock Namespace object to return from parse_args
        args = argparse.Namespace()
        args.yaml_files = [Path('test1.yml'), Path('test2.yml')]
        args.output = Path('outputs')
        args.skip_extension_check = False
        mock_parse_args.return_value = args

        # Parse the arguments
        parsed_args = yaml_toml.parse_arguments()

        # Check that the arguments were parsed correctly
        self.assertEqual(parsed_args, args)

    @patch('src.yaml_toml.yaml_toml.convert_file')
    @patch('src.yaml_toml.yaml_toml.parse_arguments')
    def test_main(self, mock_parse_arguments, mock_convert_file):
        # Create a mock Namespace object to return from parse_arguments
        args = argparse.Namespace()
        args.yaml_files = [Path('test1.yml'), Path('test2.yml')]
        args.output = Path('outputs')
        args.skip_extension_check = False
        mock_parse_arguments.return_value = args

        # Run the main function
        yaml_toml.main()

        # Check that convert_file was called for each YAML file
        mock_convert_file.assert_has_calls([call(Path('test1.yml'), Path('outputs'), False), call(Path('test2.yml'), Path('outputs'), False)])

    @patch('src.yaml_toml.yaml_toml.convert_file')
    @patch('src.yaml_toml.yaml_toml.parse_arguments')
    @patch('pathlib.Path.glob')
    @patch('pathlib.Path.cwd')
    def test_main_no_arguments(self, mock_cwd, mock_glob, mock_parse_arguments, mock_convert_file):
        # Create a mock Namespace object to return from parse_arguments
        args = argparse.Namespace()
        args.yaml_files = []
        args.output = Path('outputs')
        args.skip_extension_check = False
        mock_parse_arguments.return_value = args

        # Mock the current directory and the glob function
        mock_cwd.return_value = Path('.')
        mock_glob.return_value = [Path('test1.yml'), Path('test2.yml')]

        # Run the main function
        yaml_toml.main()

        # Check that convert_file was called for each YAML file in the current directory
        mock_convert_file.assert_has_calls([call(Path('test1.yml'), Path('outputs'), False), call(Path('test2.yml'), Path('outputs'), False)])

if __name__ == '__main__':
    unittest.main()
