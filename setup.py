import setuptools

with open("README.md", "r") as fh:
long_description = fh.read()


setuptools.setup(
    name='package',
    version='0.1',
    scripts=[],
    author="ChewierSkink",
    author_email="chewierskink342@gmail.com",
    description="A training package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ChewierSkink/training_package",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
)
