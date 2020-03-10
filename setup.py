import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="plagcheck",
    version="0.4",
    license="MIT",
    author="Bhupesh Varshney",
    author_email="varshneybhupesh@gmail.com",
    description="Moss Results scraper with powerful insights & analysis",
    keywords="moss plagiarism analysis cheat mosspy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://codeclassroom.github.io/PlagCheck/",
    project_urls={
        "Documentation": "https://plagcheck.readthedocs.io/en/latest/?badge=latest",
        "Source Code": "https://github.com/codeclassroom/PlagCheck",
        "Funding": "https://www.patreon.com/bePatron?u=18082750",
        "Say Thanks!": "https://github.com/codeclassroom/PlagCheck/issues/new?assignees=&labels=&template=---say-thank-you.md&title=",
        "Tracker": "https://github.com/codeclassroom/PlagCheck/issues",
    },
    packages=setuptools.find_packages(),
    install_requires=[
        'mosspy',
        'beautifulsoup4',
        'lxml',
    ],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        'Topic :: Software Development :: Build Tools',
        "Topic :: Education",
        "Topic :: Education",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Operating System :: OS Independent",

    ],
    python_requires='>=3.6',
)