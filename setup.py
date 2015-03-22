from setuptools import setup, find_packages
install_requires = [
    # List your project dependencies here.
    # For more details, see:
    # http://packages.python.org/distribute/
    # setuptools.html#declaring-dependencies
    'networkx', 'lxml']

setup(
    name='openlawsgii',
    version='0.1',
    packages=find_packages('src'),
    package_dir = {'': "src"},
    include_package_data=True,
    install_requires=install_requires,
    url='github.com/fkuhn/openlawsgii',
    license='Apache License 2.0',
    author='kuhn',
    author_email='kuhn@ids-mannheim.de',
    description='converter for gii to openlaws geoff'
)
