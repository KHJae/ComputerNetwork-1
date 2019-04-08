import socket
import threading
import argparse


def socket_handler(conn):
    # 여기에 클라이언트 소켓에서 데이터를 받고, 보내는 코드 작성
    # ex) conn.recv(1024)
    msg = conn.recv(1024)
    reverse_msg = msg.decode()[::-1]
    conn.sendall(reverse_msg.encode())
    conn.close()
    print(addr[0], ' : Closed')
  



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Thread server -p port")
    parser.add_argument('-p', help = "port_number", required = True)

    args = parser.parse_args()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', int(args.p)))
    server.listen(5)

    while True:
        conn, addr = server.accept()
        print('Connected : ',addr[0], ' : ', addr[1])
        # 여기에 socket.accept 후 리턴받은 클라이언트 소켓으로 스레드를 생성하는 코드 작성
        my_thread = threading.Thread(target = socket_handler, args = (conn,))
        my_thread.start() 
        my_thread.join()
    server.close()
    
