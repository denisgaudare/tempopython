# first line: 23
@memory.cache
def process_file_cached(file_path):
    return _process_file(file_path)
