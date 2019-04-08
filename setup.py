import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vscode-extensions-list-inadarei",
    version="0.1.0",
    author="Irakli Nadareishvili",
    #author_email="author@example.com",
    description="Gives installed VS Code extensions as a linked markdown list",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/inadarei/vscode-extensions-list",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)