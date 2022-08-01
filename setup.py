import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py-pipeline",
    version="develop",
    license='GPL v3',
    author="Riccardo Curcio",
    author_email="curcioriccardo@gmail.com",
    description="Function pipeline",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RiccardoCurcio/py-pipeline.git",
    download_url = 'https://github.com/RiccardoCurcio/py-pipeline.git/archive/develop.tar.gz',
    packages=setuptools.find_packages(),
    keywords = [
        'functional',
        'pipeline'
    ],
    install_requires=['typing'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
