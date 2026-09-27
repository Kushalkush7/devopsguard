import psutil


def get_disk_usage():
    disk = psutil.disk_usage("/")
    return disk.percent


if __name__ == "__main__":
    disk = get_disk_usage()
    print(f"Disk Usage: {disk}%")
