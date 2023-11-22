import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="yaml_parser",
    version="0.0.1",
    author="Daniel Sturdivant",
    author_email="sturdivant20@gmail.com",
    description="Wrapper for parsing yaml files into dictionaries",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gavlab-radiance/yaml_parser",
    install_requires=['numpy>1.24.3', 
                      'PyYAML>6.0.0'],
    packages=setuptools.find_packages(),
)