from setuptools import setup,find_packages
setup(
    name='OcrGather',
    versioin='0.1.1',
    description='描述',
    include_package_data=True,
    install_requires=[item.strip('\n') for item in list(open('requirement.txt','r').readlines())],
    packages=find_packages(),
    license='Apache License 2.0',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent'
    ],

)