import psutil


def get_cpu_usage():
    return psutil.cpu_percent(interval=5)


if __name__ == "__main__":
    cpu = get_cpu_usage()
    print(f"CPU Usage: {cpu}%")
