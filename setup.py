from setuptools import setup, find_packages

setup(
    name="quickmark",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["click"],
    entry_points={"console_scripts": ["qm=quickmark.cli:cli"]},
    author="klaussh",
    description="A fast CLI bookmark manager with fuzzy search",
    license="MIT",
)
