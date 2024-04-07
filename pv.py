import socket

def find_apache_port(ip_address):
    for port in range(1, 65536):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # تعيين وقت الانتظار للاتصال
        result = sock.connect_ex((ip_address, port))
        if result == 0:
            print(f"تم العثور على خادم Apache على البورت {port}")
            break

if __name__ == "__main__":
    ip_address = input("الرجاء إدخال عنوان IP الخاص بالخادم: ")
    find_apache_port(ip_address)
