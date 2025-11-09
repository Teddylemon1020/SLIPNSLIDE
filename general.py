import os 

def create_directory(directory):
    """Create a directory if it doesn't exist."""
    try:
        os.makedirs(directory, exist_ok=True)
        print(f"Directory '{directory}' created or already exists.")
    except Exception as e:
        print(f"Error creating directory '{directory}': {e}")


def create_data_file(path, base_url):
    queue = path + "/queue.txt"
    crawled = path + "/crawled.txt"
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')

def write_file(path, data):
    with open(path, 'w') as file:
        file.write(data)


def appeand_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

def delete_file_contents(path):
    with open(path, 'w') as file:
        pass


def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results

def set_to_file(links, file):
    delete_file_contents(file)
    for link in sorted(links):
        appeand_to_file(file, link)