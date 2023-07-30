import yaml
import toml
import argparse
from typing import List
from pathlib import Path
from rich.console import Console
from rich.traceback import install
from rich.prompt import Prompt

install()

console = Console()

def convert_yaml_to_toml(yaml_file_path: Path, toml_file_path: Path) -> None:
    """
    Converts a YAML file to a TOML file.

    Args:
        yaml_file_path (Path): The path to the input YAML file.
        toml_file_path (Path): The path to the output TOML file.
    """
    # Load the YAML file
    with open(yaml_file_path, 'r') as yaml_file:
        yaml_data = yaml.safe_load(yaml_file)

    if yaml_data is None:
        console.log(f"No data in {yaml_file_path}. Skipping conversion.")
        return

    # Write the data to a TOML file
    with open(toml_file_path, 'w') as toml_file:
        toml.dump(yaml_data, toml_file)

def convert_file(yaml_file: Path, output_dir: Path, skip_extension_check: bool) -> None:
    """
    Convert a YAML file to a TOML file in the specified output directory.

    Args:
        yaml_file (Path): The path to the YAML file.
        output_dir (Path): The output directory.
        skip_extension_check (bool): Whether to skip the file extension check.
    """
    # Check the file extension if necessary
    if not skip_extension_check and yaml_file.suffix not in ['.yml', '.yaml']:
        console.log(f"Skipping {yaml_file}: not a .yml or .yaml file")
        return

    # Prepare the output file path
    toml_file = output_dir / (yaml_file.stem + '.toml')
    
    # Check if the file already exists
    if toml_file.exists():
        action = Prompt.ask(f"File {toml_file} already exists. What would you like to do?", choices=["Skip", "Rename", "Overwrite", "Cancel"], default="Skip")
        
        if action == "Skip":
            console.log(f"Skipping {yaml_file}")
            return
        elif action == "Rename":
            new_name = Prompt.ask("Enter the new filename", default=toml_file.stem + "_1.toml")
            toml_file = output_dir / new_name
        elif action == "Overwrite":
            console.log(f"Overwriting {toml_file}")
        elif action == "Cancel":
            exit()

    # Convert the file
    try:
        convert_yaml_to_toml(yaml_file, toml_file)
        console.log(f"Converted {yaml_file} to {toml_file}")
    except Exception as e:
        console.log(f"Failed to convert {yaml_file} to {toml_file}: {e}")

def parse_arguments() -> argparse.Namespace:
    """
    Parse command-line arguments.

    Returns:
        argparse.Namespace: The parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(description="Convert YAML files to TOML files.")
    parser.add_argument('yaml_files', type=Path, nargs='*', default=[], help="The YAML files to convert.")
    parser.add_argument('--input', type=Path, help="The input directory containing YAML files to convert.")
    parser.add_argument('--output', type=Path, help="The output directory for the TOML files.")
    parser.add_argument('--skip-extension-check', action='store_true', help="Skip the file extension check for the YAML files.")
    
    return parser.parse_args()

def main() -> None:
    """
    The main function of the script. Parses command-line arguments, converts files, and handles errors.
    """
    args = parse_arguments()

    # If no output directory was provided, use the default
    if args.output is None:
        args.output = Path('./outputs')

    # Ensure the output directory exists
    args.output.mkdir(parents=True, exist_ok=True)

    # Convert the specified YAML files
    for yaml_file in args.yaml_files:
        convert_file(yaml_file, args.output, args.skip_extension_check)

    # Convert the YAML files in the input directory
    if args.input is not None:
        for yaml_file in args.input.glob('*.y{a,}ml'):
            convert_file(yaml_file, args.output, args.skip_extension_check)

    # If no files or input directory were specified, convert all YAML files in the current directory
    if len(args.yaml_files) == 0 and args.input is None:
        for yaml_file in Path.cwd().glob('*.y{a,}ml'):
            convert_file(yaml_file, args.output, args.skip_extension_check)

if __name__ == "__main__":
    main() 
