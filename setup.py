from setuptools import setup, find_packages

setup(
    name="prpip",
    version="0.1.0",
    author="Your Name",
    author_email="your_email@example.com",
    description="A package for reconstructing pupil size and handling eye-tracker blinks.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/AhsanKhodami/prpip",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=[
        "numpy",
        "pandas"
    ],
)
