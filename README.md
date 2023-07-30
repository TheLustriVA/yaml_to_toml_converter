# YAML to TOML converter

![YAML to TOML banner](assets/yaml_toml.png)

A simple tool to convert YAML files into TOML files.

Please note this README.md is an interim document.

## Installation

1. Clone the GitHub Repository `git clone https://github.com/TheLustriVA/yaml_to_toml_converter.git`
2. Run `pip install -r requirements.txt`

## Usage

To use the converter, make sure your yaml file is in the same directory to which you cloned the github repo.

### Convert a single file

For a simple default conversion, run:

```bash
python yaml_toml.py my_yaml_file.yml
```

The converter will send the `.toml` file to the `outputs/` folder.

```bash
outputs/my_yaml_file.toml
```

### Convert a batch of files

You can run the converter with a space-delimited list of yaml files and each one will be converted before being sent to the output directory.

```bash
python yaml_toml.py yaml_num_1.yaml yaml_num_2.yaml yaml_num_3.yaml yaml_num_4.yaml
```

### Set a non-default output folder for a single conversion

Use the `--output` flag to set a specific output directory.

```bash
python yaml_toml.py --output ~/dotfiles/ my_dotfile.yml
```
