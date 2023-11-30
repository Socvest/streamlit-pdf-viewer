from pathlib import Path

import setuptools

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
bump_version = (this_directory / ".bumpversion.toml").read_text()
version = bump_version.split("\n")[0].split(" = ")[1].replace("\"", "")

setuptools.setup(
    name="streamlit-pdf-viewer",
    version=version,
    author="Luca Foppiano",
    author_email="lucanoro@duck.com",
    description="Streamlit component for PDF visualisation and manipulation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lfoppiano/streamlit-pdf-viewer",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=["rag", "streamlit-component", "pdf-viewer", "documents"],
    python_requires=">=3.7",
    install_requires=[
        "streamlit >= 0.63"
    ],
    extras_require={
        "devel": [
            "wheel"
        ]
    }
)