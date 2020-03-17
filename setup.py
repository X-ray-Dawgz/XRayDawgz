import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="xraydawgz",
    version="0.1",
    author="Rick, Alex, Robert, Kevin",
    description="XRayDawgz XRD image pattern classifier",
    url="https://github.com/X-ray-Dawgz/XRayDawgz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)
