import setuptools

setuptools.setup(
    name='tokompiler',
    version='0.1',
    description='Scope is all you need: Transforming LLMs for HPC Code',
    url='https://github.com/Scientific-Computing-Lab-NRCN/Tokompiler/tree/main',
    packages=['tokompiler'],
    package_dir={'tokompiler': 'src/tokompiler'},
    package_data={'tokompiler': ['parsers/*.so']},
)
