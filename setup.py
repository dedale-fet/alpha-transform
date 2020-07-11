import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="alpha-transform",
    version="0.0.1",
    description="Adaptive transform for manifold-valued data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dedale-fet/alpha-transform",
    packages=setuptools.find_packages(),

    # list of dependencies
    install_requires=[
        "numpy",
        "matplotlib",
        "numexpr",
        "pyfftw",
        "tqdm",
        "healpy",
        "Pillow",
        "scipy"
    ],
)
