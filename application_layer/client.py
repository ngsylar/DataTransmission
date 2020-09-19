import http.client

host = "localhost"
port = 8888

conn = http.client.HTTPConnection(host, port)
conn.request("GET", "index.html")
r1 = conn.getresponse()
print(r1.status, r1.reason)
data1 = r1.read().decode()
print(data1)
headers = r1.getheaders()
print(headers[0][0], " : ", headers[0][1])
conn.close()
