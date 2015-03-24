__author__ = 'kuhn'
__doc__ = 'a hack to convert gii xml data to openlaws-neo4j'
import codecs
import networkx
import neonx
from zipfile import ZipFile
from lxml import etree

# TODO: find a non hardcoded solution
LAWMETAXPATH = "/dokumente/norm/metadaten"

class GiiGraph(networkx.MultiDiGraph):
    """
    GiiGraph represents the attribute Node structure
    """

    def __init__(self):
        super(GiiGraph, self).__init__()
        """

        :return:
        """

    def add_gii_xmlfile(self, xmlfile):
        """
        reads an gii xml file to an networkx MultiDiGraph
        :param xmlfile:
        :return:
        """
        giixmlfileobject = codecs.open(xmlfile, encoding="utf-8")
        giietree = etree.parse(giixmlfileobject)

        # define the root node of the graph
        self.add_german_law_object(giietree)
        self.add_german_article(giietree)

    def add_german_law_object(self, giietree):
        """
        adds the etree of an law object to the graph structure
        :param giietree:
        :return:
        """
        metainfo = giietree.xpath(LAWMETAXPATH)[0]

        self.add_node("GermanLegalObject", {"name_of_legal_object": metainfo.xpath("./kurzue")[0].text,
                                            "author": metainfo.xpath("./fundstelle/periodikum")[0].text,
                                            "description": metainfo.xpath("./langue")[0].text,
                                            "type": "Bundesgesetz",
                                            "date_of_document": giietree.xpath("/dokumente/norm[1]/@builddate")[0],
                                            "date_of_effect": metainfo.xpath("./ausfertigung-datum")[0].text,
                                            "external_ID": giietree.xpath("/dokumente/norm[1]/@doknr")[0],
                                            "link_to_document": "URI"})

    def add_german_article(self, giietree):
        """
        adds the eptree to the graph structure
        :param giietree:
        :return:
        """
        # /dokumente/norm[37] /dokumente/norm[10]
        # find the articles level in the etree object
        count = 0
        for normelement in giietree.xpath("/dokumente/norm"):

            if len(normelement.xpath("./metadaten/enbez")) > 0 and len(normelement.xpath("./metadaten/titel")) > 0:
                # <!ELEMENT metadaten (jurabk+, amtabk?, ausfertigung-datum?, fundstelle*, kurzue?, langue?, gliederungseinheit?, enbez?, titel?, standangabe*)>

                self.add_node("GermanLegalArticle_" + str(count),
                                                                 {
                                                                    "external_ID": normelement.xpath("./metadaten/enbez")[0].text,
                                                                    "name_of_legal_object": normelement.xpath("./metadaten/titel")[0].text,
                                                                    "author": giietree.xpath("/dokumente/norm/metadaten/fundstelle/periodikum")[0].text,
                                                                    "date_of_effect": giietree.xpath("/dokumente/norm[1]/metadaten/ausfertigung-datum")[0].text,
                                                                    "date_of_document": normelement.xpath("./@builddate")[0],
                                                                    "link_to_document": "URI",
                                                                    "entire_text_of_legal_article": [p.text for p in normelement.xpath("./textdaten/text/Content/P")]}
                                                                 )

                self.add_edge("GermanLegalObject", "GermanLegalArticle_" + str(count))
                count += 1
            if count > 0:
                self.add_edge("GermanLegalArticle_" + str(count-1), "GermanLegalArticle_" + str(count))


    def export2geoff(self):
        """
        export the networkx representation to neo4j geoff format
        """
        gdata = neonx.get_geoff(self, "LINKS_TO")
        return gdata

    def readzippedxml(self, xmlzip):
        """
        accesses the generic xml.zip of each gii document.
        :param xmlzip:
        :return: xml-file
        """
        zipped = ZipFile(xmlzip)
        zname = zipped.filelist[0].filename
        fileobject = zipped.open(zname)
