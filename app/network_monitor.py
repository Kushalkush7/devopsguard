import psutil


def get_network_usage():
    network = psutil.net_io_counters()

    return {
        "bytes_sent": network.bytes_sent,
        "bytes_received": network.bytes_recv
    }


if __name__ == "__main__":
    network = get_network_usage()

    print(f"Bytes Sent: {network['bytes_sent']}")
    print(f"Bytes Received: {network['bytes_received']}")
