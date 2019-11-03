import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="plagcheck",
    version="0.1",
    author="Bhupesh Varshney",
    author_email="varshneybhupesh@gmail.com",
    description="A Powerful Moss results scrapper",
    keywords='mosspy moss plagiarism cheat',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/codeclassroom/PlagCheck",
    project_urls={
        "Documentation": "https://github.com/codeclassroom/PlagCheck/blob/master/docs/docs.md",
        "Source Code": "https://github.com/codeclassroom/PlagCheck",
        "Funding": "https://www.patreon.com/bePatron?u=18082750",
        "Say Thanks!": "https://github.com/codeclassroom/PlagCheck/issues/new?assignees=&labels=&template=---say-thank-you.md&title=",
    },
    packages=setuptools.find_packages(),
    install_requires=[
        'requests',
        'mosspy',
        'beautifulsoup4',
        'lxml',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        'Topic :: Software Development :: Build Tools',
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)