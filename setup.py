from pathlib import Path
from setuptools import setup, find_packages

ROOT = Path(__file__).parent
README = (ROOT / "README.md").read_text(encoding="utf-8")

# Read version from __init__.py if available
version = {}
init_py = ROOT / "abcweather" / "__init__.py"
if init_py.exists():
    for line in init_py.read_text(encoding="utf-8").splitlines():
        if line.startswith("__version__"):
            version["__version__"] = line.split("=")[1].strip().strip("'\"")
            break

setup(
    name="abcweather",
    version=version.get("__version__", "0.1.0"),
    description="Tools for working with weather data (abcweather).",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="quantumpython@ucl.ac.uk",
    url="https://github.com/QC2-python-SE/AB_weather/",
    license="MIT",
    keywords=["weather", "climate", "data", "analysis"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(exclude=("tests*", "docs*")),
    include_package_data=True,
    python_requires=">=3.9",
    install_requires=[
        # "numpy>=1.24",
        # "pandas>=2.0",
    ],
    extras_require={
        "dev": ["pytest>=7", "ruff>=0.4", "build>=1.2", "twine>=5.0"],
    },
    entry_points={
        "console_scripts": [
            # Example: allows `abcweather` in terminal if you have cli.py
            "abcweather=abcweather.cli:main",
        ]
    },
    project_urls={
        "Documentation": "https://your-docs-url.example.com",
        "Source": "https://github.com/QC2-python-SE/AB_weather/",
        "Issues": "https://github.com/QC2-python-SE/AB_weather/issues",
    },
)