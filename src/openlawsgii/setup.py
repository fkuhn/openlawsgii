from distutils.core import setup

install_requires = [
    # List your project dependencies here.
    # For more details, see:
    # http://packages.python.org/distribute/
    # setuptools.html#declaring-dependencies
    'networkx', 'lxml']

setup(
    name='openlawsgii',
    version='0.1',
    packages=['', 'openlawsgii'],
    package_dir={'': 'src/openlawsgii'},
    url='github.com/fkuhn/openlawsgii',
    license='Apache License 2.0',
    author='kuhn',
    author_email='kuhn@ids-mannheim.de',
    description='converter for gii to openlaws geoff'
)
