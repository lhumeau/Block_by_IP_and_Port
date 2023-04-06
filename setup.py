from setuptools import setup, find_packages

setup(
    name="ipblockandport.py",
    version="1.0.0",
    description="Project for blocking ip and port 3389 and 443 that is not from DR,
    long_description="Block entries ip from ports 3389 and 443 excepting local interfaces is base on a Windows base Enviroment. in this code i'm filtering ip by whois libraries using scappy for monitoring packets from source and ports.",
    author="Luis Humeau",
    author_email="l.humeau@hynit.com",
    url="https://github.com/lhumeau/Block_by_IP_and_Port",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="python, whois, scappy",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        ipwhois==0.12.0
        scapy==2.4.5
    ],
    entry_points={
        "console_scripts": [
            "python ipblockandport.py",
        ],
    },
)
