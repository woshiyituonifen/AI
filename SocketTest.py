import socket
import threading


def handle_request(ip_port, new_Clinet):
    print("端口号：", ip_port);
    recv_data = new_Clinet.recv(1024);
    if recv_data:
        recv_conent = recv_data.decode("utf-8");
        print("接受的数据", recv_conent);
        sende_data = "<h>www</h>".encode("utf-8");
        new_Clinet.send(sende_data);
    else:
        print("下线")
        breakpoint();
    new_Clinet.close();


if __name__ == '__main__':
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True);
    tcp_socket.bind(('', 5000));
    tcp_socket.listen(128);
    while True:
        new_Clinet, ip_port = tcp_socket.accept();
        ub_thread = threading.Thread(target=handle_request, args=(ip_port, new_Clinet));
        ub_thread.setDaemon(True)
        ub_thread.start();
    tcp_socket.close();
