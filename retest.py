import requests

def posturl1(ip):
    url = "http://hermes-debug.fun.tv/iplocate?&v=zgxv6.2023.01&g=6&ip={ip1}".format(ip1 = ip)

    respones = requests.get(url=url)
    return respones


def posturl2(ip):
    url = "http://192.168.8.100:8130/iplocation?g=6&ip={ip1}".format(ip1=ip)

    respones = requests.get(url = url)
    return respones


