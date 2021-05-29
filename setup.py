from typing import List

import setuptools


def read_multiline_as_list(file_path: str) -> List[str]:
    with open(file_path) as fh:
        contents = fh.read().split("\n")
        if contents[-1] == "":
            contents.pop()
        return contents


with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = read_multiline_as_list("requirements.txt")

# classifiers = read_multiline_as_list("classifiers.txt")

setuptools.setup(
    name="network-chan",
    version="0.0.1",
    author="Nei Cardoso de Oliveira Neto, Nicolas Isquierdo Curço",
    author_email="nei.neto@hotmail.com, nicolas.curco@gmail.com",
    description="P2P network to share chan threads.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cardoso-neto/network-chan",
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},  # not sure if this line should be here
    # classifiers=classifiers,
    keywords="",
    entry_points={
        "console_scripts": [
            "network-chan=network_chan.strategy:main",
        ],
    },
    python_requires=">=3.7",
    install_requires=requirements,
)
