import rospy
import socket

def receive_object_dimensions():
    host = '192.168.50.91'  # Replace with your Unity server's IP
    port = 10001        # Replace with your Unity server's port

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)

    print("Waiting for Unity connection...")
    conn, addr = server.accept()
    print("Connected to Unity:", addr)

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break

        object_data = data.split(',')
        object_name = object_data[0]
        dimensions = tuple(map(float, object_data[1:]))
        
        print(f"Object: {object_name}, Dimensions: {dimensions}")
        
    conn.close()

if __name__ == "__main__":
    rospy.init_node('object_dimensions_listener')
    receive_object_dimensions()

