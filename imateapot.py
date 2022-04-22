import socket

host = "127.0.0.1"
port = 85

loadfile = False

if loadfile == True:
        file = open("index.html", "r")
        html = file.read()
        file.close()

if loadfile == False:
        html = f"""<DOCTYPE html>
<html>
  <body>
    <center><p>im a teapot<p></center>
  </body>
</html>
"""

html = bytes(html, "utf-8")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
print(f"Listening for incoming connections on {host}:{port}")

while True:
        s.listen()
        conn, addr = s.accept()

        with conn:
                print(f"Connected by {addr}")
                conn.sendall(str.encode("HTTP/1.0 418 I'm a teapot\n",'utf-8'))
                conn.sendall(str.encode('Content-Type: text/html\n', 'utf-8'))
                conn.send(str.encode('\r\n'))
                conn.sendall(html)

