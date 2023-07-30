# YAML to TOML converter

![YAML to TOML banner](assets/yaml_toml.png)

A simple tool to convert YAML files into TOML files.

## Installation

1. Clone the GitHub Repository `git clone https://github.com/TheLustriVA/yaml_to_toml_converter.git`
2. Navigate into the cloned directory `cd yaml_to_toml_converter`
3. Install the required Python packages `pip install -r requirements.txt`

## Usage

You can run the converter in several ways:

### Convert a single file

```bash
python yaml_toml.py my_yaml_file.yml
```

The converter will send the .toml file to the outputs/ folder.

```bash
outputs/my_yaml_file.toml
```

### Convert a batch of files

You can run the converter with a space-delimited list of yaml files and each one will be converted.

```bash
python yaml_toml.py yaml_num_1.yaml yaml_num_2.yaml yaml_num_3.yaml yaml_num_4.yaml
```

### Convert all YAML files in a directory

You can run the converter with an input directory and all YAML files in that directory will be converted.

```bash
python yaml_toml.py --input ~/old_dotfiles/
```

### Set a non-default output folder

Use the --output flag to set a specific output directory.

```bash
python yaml_toml.py --output ~/dotfiles/ my_dotfile.yml
```

### Skip the file extension check

By default, the converter checks if the input files have a .yml or .yaml extension. You can skip this check with the `--skip-extension-check`` flag.

```bash
python yaml_toml.py --skip-extension-check my_file
```

### Default behavior

If no arguments are provided, the script will convert all YAML files in the current directory and output them to ./outputs/.

```bash
python yaml_toml.py
```
