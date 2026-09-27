import psutil


def get_memory_usage():
    memory = psutil.virtual_memory()
    return memory.percent


if __name__ == "__main__":
    memory = get_memory_usage()
    print(f"Memory Usage: {memory}%")
