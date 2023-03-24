import json

def redata():
    with open("ipv6_testcase.json") as f:
        datalist = json.load(f)
        testdata = []
        for i in datalist:
            biaot = i.get("biaot")
            bm = i.get("bm")
            country = i.get("country")
            province = i.get("province")
            city = i.get("city")
            district = i.get("district")
            areacode = i.get("areacode")
            testdata.append((biaot,bm,country,province,city,district,areacode))

        return testdata




