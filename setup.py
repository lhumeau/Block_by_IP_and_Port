setup(
    name='Block_by_IP_and_Port',
    version='1.0.0',
    description='Tool to block IP addresses on ports 3389 and 443 in a Windows environment',
    author='Luis Humeau - HYNIT',
    author_email='l.humeau@hynit.com',
    url='https://github.com/HYNIT/Block_by_IP_and_Port',
    packages=[''],
    install_requires=[
        'ipwhois',
        'scapy',
        'win32com',
        'netifaces'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: Microsoft :: Windows',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Networking :: Monitoring'
    ],
)
