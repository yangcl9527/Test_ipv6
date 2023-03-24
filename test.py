import unittest
from retest import posturl1
from retest import posturl2
from parameterized import parameterized
from resdate import redata

class Test001(unittest.TestCase):
    def setUp(self):
        self.posturl1 = posturl1
        self.posturl2 = posturl2

    @parameterized.expand(redata())
    def test01(self,biaot,bm,country,province,city,district,areacode):
        print biaot
        response = self.posturl1(bm)
        self.assertEqual(province,response.json().get("province"))
        self.assertEqual(city,response.json().get("city"))
        self.assertEqual(district,response.json().get("district"))
        self.assertEqual(areacode,response.json().get("areacode"))
        self.assertEqual(country,response.json().get("country"))

    @parameterized.expand(redata())
    def test02(self,biaot,bm,country,province,city,district,areacode):
        print biaot
        response = self.posturl2(bm)
        self.assertEqual(province,response.json().get("province"))
        self.assertEqual(city,response.json().get("city"))
        self.assertEqual(district,response.json().get("district"))
        self.assertEqual(areacode,response.json().get("areacode"))
        self.assertEqual(country,response.json().get("country"))


