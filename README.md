# openslawsgii
## connecting openlaws to the german federal law

There is a [demo ipython-notebook]
(http://nbviewer.ipython.org/github/fkuhn/openlawsgii/blob/master/notebooks/giigraph_demo.ipynb) available.


The giigraph module is based on a prototype written during a code camp of
the openslaws.eu project at the university of applied sciences Salzburg,
Austria (March 20st and 21st 2015).

The open data project 'openlaws.eu' is aiming at providing legal
knowledge freely and sophistically processed by using state of the art
technologies. Since the project is based on an european level, it also
tries to interlink as many european legal domains as possible.

The german legal domain has not yet been linked to openlaws and my task
for the hackaton was to prototype the converter that takes the data provided
on www.gesetze-im-internet.de and converts it to the geoff format of
neo4j by using the specific attribute model for a database node.

Since time was short, I sticked to just converting the copyright-law file
as a baseline.

GiiGraph is a class derived from MultiDiGraph of networkx so it can be
easily enhanced lateron to meet requirements like backreference, crossreference,
in-place reference, versioning etc.

First of all, I parsed the xml file with the well known lxml module
(a binding to the libxml2 c-library). The important data items were read using the
builtin xpath capabilities.

The graph was easily built after looking up the important german data
items that have to be put in its place in the openlaws attribute model.

The root of all elements is the catalogue metadata of the law itself.

By using conditionals for the metafile structure, only articles were
put into the graph. They all are chained via edges. Moreover, each article
node is linked to the root element.

The package neonx is a converter to the json string of neo4j's geoff format.
It was used to export the networkx graph to the geoff format.

As you can see, the class definition is quite small and readable by
using already existing open source packages. Besides, the attribute model
of openlaws is restricted to the very core of important information.


### However
The gii website does not have an API to optain the data without any problems.
A webcrawler must be written first to get all items in place. I will be
using scrapy. 




