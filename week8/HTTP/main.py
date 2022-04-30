'''
http 
tcp
ip
ip -address:port(8000) ->socket -> client, server
'''
import socket


def run():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 8000))
    server_socket.listen()
    while True:
        client_socket, address = server_socket.accept()
        request = client_socket.recv(1024)
        print(request.decode('utf-8'))
        print()
        print(address)
        client_socket.sendall('Hello!'.encode('utf-8'))
        client_socket.close()


# b'GET / HTTP/1.1\r\nHost: localhost:8000\r\nConnection: keep-alive\r\nsec-ch-ua: "Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"\r\nsec-ch-ua-mobile: ?0\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nSec-Fetch-Site: none\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-User: ?1\r\nSec-Fetch-Dest: document\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.9,ru-KG;q=0.8,ru;q=0.7\r\n\r\n'

# ('127.0.0.1', 64693)
# b'GET / HTTP/1.1\r\nHost: localhost:8000\r\nConnection: keep-alive\r\nCache-Control: max-age=0\r\nsec-ch-ua: "Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"\r\nsec-ch-ua-mobile: ?0\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nSec-Fetch-Site: none\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-User: ?1\r\nSec-Fetch-Dest: document\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.9,ru-KG;q=0.8,ru;q=0.7\r\n\r\n'

# ('127.0.0.1', 64695)
# b'GET / HTTP/1.1\r\nHost: localhost:8000\r\nConnection: keep-alive\r\nCache-Control: max-age=0\r\nsec-ch-ua: "Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"\r\nsec-ch-ua-mobile: ?0\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nSec-Fetch-Site: none\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-User: ?1\r\nSec-Fetch-Dest: document\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.9,ru-KG;q=0.8,ru;q=0.7\r\n\r\n'

# ('127.0.0.1', 64697)


if __name__ == '__main__':
    run()

###############################################
# def parse_request(request):
#     parsed = request.split(' ')
#     method = parsed[0]
#     url = parsed[1]
#     return method, url

# def generate_headers(method, url):
#     if not method == 'GET':
#         return ('HTTP/1.1')
# def generate_response(request):
#     method, url = parse_request(request)
#     headers, code = generate_headers(method, url)


# def run():
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#     server_socket.bind(('localhost', 8000))
#     server_socket.listen()
#     while True:
#         client_socket, address = server_socket.accept()
#         request = client_socket.recv(1024)
#         print(request)
#         print()
#         print(address)
#         response = generate_response(request.decode('utf-8'))
#         # client_socket.sendall('Hello!'.encode('utf-8'))
#         client_socket.close()




# if __name__ == '__main__':
#     run()
#############################