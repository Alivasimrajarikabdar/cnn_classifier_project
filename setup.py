import setuptools
__version__='0.0.1'
with open("README.md","r",encoding="utf-8") as f:
    long_description=f.read()

REPO_NAME="cnn_classifier_project"
AUTHOR_NAME="ASMA"
SRC_REPO="deepClassifier"
AUTHOR_Email="asmarikabdar@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_Email,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)