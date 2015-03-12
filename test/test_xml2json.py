import unittest
import xml2json
import optparse
import json
import os

xmlstring = ""
options = None

class SimplisticTest(unittest.TestCase):

    def setUp(self):
        global xmlstring, options
        filename = os.path.join(os.path.dirname(__file__), 'xml_ns2.xml')
        xmlstring = open(filename).read()
        options = optparse.Values({"pretty": False})


        global xmlstring2, options2
        filename = os.path.join(os.path.dirname(__file__), 'simple.xml')
        xmlstring2 = open(filename).read()
        options2 = optparse.Values({"pretty": True,"strip_newlines":True,"strip_text":"<e> <a>text</a> <a>text</a> </e>"})

    def test_default_namespace_attribute(self):
        strip_ns = 0
        json_string = xml2json.xml2json(xmlstring,options,strip_ns)
        # check string
        self.assertTrue(json_string.find("{http://www.w3.org/TR/html4/}table") != -1)
        self.assertTrue(json_string.find("{http://www.w3.org/TR/html4/}tr") != -1)
        self.assertTrue(json_string.find("@class") != -1)

        # check the simple name is not exist
        json_data = json.loads(json_string)
        self.assertFalse("table" in json_data["root"])

    def test_strip_namespace(self):
        strip_ns = 1
        json_string = xml2json.xml2json(xmlstring,options,strip_ns)
        json_data = json.loads(json_string)

        # namespace is stripped
        self.assertFalse(json_string.find("{http://www.w3.org/TR/html4/}table") != -1)

        # TODO , attribute shall be kept
        #self.assertTrue(json_string.find("@class") != -1)

        #print json_data["root"]["table"]
        #print json_data["root"]["table"][0]["tr"]
        self.assertTrue("table" in json_data["root"])
        self.assertEqual(json_data["root"]["table"][0]["tr"]["td"] , ["Apples", "Bananas"])

    def test_bekzat(self):
        test1 = {
            # "text":"bekzat",
            "#list":["1","2","@3"],
            # "@text":"bekzat2"
        }

        res = xml2json.internal_to_elem(test1);

    def test_bekzat0(self):
        d = {'r': {'@p': 'p1', '#text': 't1', 'c': 't2'}};
        xml_string = xml2json.json2xml(d);
        # xml_data = json.loads(json_string)


        # res2 = xml2json.xml2json(res);   
       # self.assertTrue(xml_data.find("") !=)

    def test_bekzat1(self):
        # print res;

        e = {'r': {'@p': 'p1', '#tail': '#tail', 'c': 't2'}}

        res = xml2json.json2xml(xe);

        print res;

        g = "<e/> ";
        res2 = xml2json.xml2json(g,options2);

        print res2;

        # f = {'r': {'@p': 'p1', '#tail': '#tail', 'c': 't2'}}

        # res = xml2json.internal_to_elem(f);

        # strip_ns = 0
        # json_string = xml2json.xml2json("<r p='p1'>t1<c>t2</c></r>",options,strip_ns)
        # json_data = json.loads(json_string)
        # res = xml2json.json2xml(null,1);

    def test_bekzat2(self):
        strip_ns = 1
        json_string = xml2json.xml2json(xmlstring2,options2,strip_ns)
        # check string
        # self.assertTrue(json_string.find("{http://www.w3.org/TR/html4/}table") != -1)
        # self.assertTrue(json_string.find("{http://www.w3.org/TR/html4/}tr") != -1)
        # self.assertTrue(json_string.find("@class") != -1)

        # check the simple name is not exist
        json_data = json.loads(json_string)
        # self.assertFalse("table" in json_data["root"])

    def test_bekzat3(self):
        strip_ns = 1
        # json_string = xml2json.xml2json(null,null,strip_ns)
        # check string
        # self.assertTrue(json_string.find("{http://www.w3.org/TR/html4/}table") != -1)
        # self.assertTrue(json_string.find("{http://www.w3.org/TR/html4/}tr") != -1)
        # self.assertTrue(json_string.find("@class") != -1)

        # check the simple name is not exist
        # json_data = json.loads(json_string)
        # self.assertFalse("table" in json_data["root"])

if __name__ == '__main__':
    unittest.main()
