from setuptools import setup, find_packages

setup(
    name="Test_Build",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "requirements.txt",
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "myproject = myproject.cli:main",
        ],
    },
)
