from setuptools import setup, find_packages

setup(
    name="abstract-claimer-br",
    version="2.4.0",
    packages=find_packages(),
    install_requires=[
        'web3>=6.0.0',
        'requests>=2.28.0',
        'colorama>=0.4.5',
        'eth-account>=0.8.0',
    ],
    author="wooookfeef",
    description="Automação oficial para alocação Abstract Chain Genesis no Brasil",
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)
