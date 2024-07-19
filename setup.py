from setuptools import setup, find_packages


setup(
    name="docscanner",
    version="0.2",
    packages=find_packages(),
    include_package_data=True,
    description="A script to scan html documents for forbidden phrases stored in a csv.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Marcin Walczak",
    url="https://github.com/marcinwalczak2",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'beautifulsoup4',
        'requests',
        'pandas',
    ],
    entry_points={
        'console_scripts': [
            'docscanner=docscanner.docscanner:main',
        ],
    },
)