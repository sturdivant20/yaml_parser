# yaml_parser
Wrapper for parsing yaml files into dictionaries. Contains recursive tool to overwrite small 
sections of large yaml files with much smaller ones.

## Installation
Clone the project into desired folder and `cd` into it:
```shell
git clone git@github.com:sturdivant20/yaml_parser.git yaml_parser
cd yaml_parser
```

Create a virtual environment or use your base Python environment. For creating a virtual 
environment, refer to 
[this article](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/). 
Ensure the virtual environment is active in your editor if you decide to use one.

From here, `pip install` the yaml_parser package in editable mode.
```shell
pip install -e .
```
Or in installed mode.
```shell
pip install .
```

<!-- >**Note:** `pip` may throw an error claiming you cannot install from a `pyproject.toml` file. If 
this is the case, upgrade your version of pip with `pip install --upgrade pip`. -->