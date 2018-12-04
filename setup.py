from setuptools import find_packages, setup

setup(
    name='secode',
    author='Črtomir Majer',
    version='0.1.0',
    long_description='Encode Kubernetes secrets',
    python_requires='>3',
    py_modules=['secode'],
    entry_points={
        'console_scripts': [
            'secode = secode.cli:run',
        ]
    },
    packages=find_packages(
        include=[
            'secode',
        ],
        exclude=[
            'tests',
        ],
    ),
    install_requires=[
        'ruamel.yaml==0.15.80'
    ],
    extras_require={
        'unit-tests': [
            'pytest',
        ]
    },
    include_package_data=True,
    dependency_links=[],
)
