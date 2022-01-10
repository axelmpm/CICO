import sys
sys.path.append(r'C:\Users\axelpm\Desktop\cico')
sys.path.append(r'C:\Users\axelpm\Desktop\cico\src\reader')
sys.path.append(r'C:\Users\axelpm\Desktop\cico\src\parser')
sys.path.append(r'C:\Users\axelpm\Desktop\cico\src\processor')

from src.reader.reader import read, new_regs_exist_at, directories_of
from src.parser.parser_main import parse
from src.processor.processor_lib import into_data, process_and_store, read_data_from, merge, processed_regs_from

def read_all(dirs):
    return sum([read(dir) for dir in dirs], [])

def read_and_parse(dirs):
    file_reg = read_all(dirs)
    failed, regs = parse(file_reg)
    return failed, regs

def read_parse_process(dirs):
    failed, regs = read_and_parse(dirs)
    data = into_data(regs)
    return failed, data

def store(data, path):
    process_and_store(data, path)

def load_data(path, alternative):
    try:
        data = read_data_from(path)
    except FileNotFoundError:
        _, data = read_parse_process([alternative])
        store(data, path)  # TODO maybe not always store
    return data
