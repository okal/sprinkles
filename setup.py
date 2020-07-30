import setuptools

with open("README.md", "r") as readme:
    long_description=readme.read()

setuptools.setup(
    name="sprinkles-config",
    version="0.0.1",
    author="Okal Otieno",
    author_email="okal@justokal.com",
    description="Generate config files from AWS Secrets",
    long_description="",
    url="https://github.com/okal/sprinkles",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    entry_points={
        'console_scripts': ['sprinkles=sprinkles.commands:generate_config']
    },
    install_requires=[
        'boto3>=1.14.31',
        'click>=7.1.2',
        'jinja>=2.11.2',
        'tomlkit>=0.6.0'
    ]
)