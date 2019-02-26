import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "doctt-backend",
    version = "0.0.1",
    author = "Denys Vitali",
    author_email = "denys@denv.it",
    description = "DocTT Backend",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/doctt/doctt-backend",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Linguistic"
    ]
)