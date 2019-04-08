import setuptools
import io

with open("README.md", "r") as fh:
    long_description = fh.read()

dependencies = []
with io.open('requirements.txt') as f:
    dependencies = [l.strip() for l in f if not l.startswith('#')]

setuptools.setup(
    name="vscext",
    version="0.2.2",
    author="Irakli Nadareishvili",
    #author_email="author@example.com",
    description="Gives installed VS Code extensions as a linked markdown list",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/inadarei/vscode-extensions-list",
    packages=setuptools.find_packages(),
    python_requires='>=3.6.*',
    install_requires=dependencies,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Development Status :: 6 - Mature',
        'Intended Audience :: Developers',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)