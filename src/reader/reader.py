import sys
sys.path.append(r'C:\Users\axelpm\Desktop\cico')
sys.path.append(r'C:\Users\axelpm\Desktop\cico\src\parser')

from os import listdir
from os.path import isfile

from src.parser.parser_utils import is_valid
from reader_constants import CICO_FILE_KEYWORD, TXT_EXTENTION, DIR_SEPARATOR

def compose_file_path(dir, filename):
    return dir + DIR_SEPARATOR + filename

def compose_dir(dir, subdir):
    return dir + DIR_SEPARATOR + subdir + DIR_SEPARATOR

def listFilesIn(dir):

    files = []
    for filename in listdir(dir):
        if isfile(compose_file_path(dir, filename)):
            files.append(compose_file_path(dir, filename))
        else:
            files += listFilesIn(compose_dir(dir, filename))
    return files

def regs_from(file_reg):
    return [reg for _, reg in file_reg]

def read(dir):

    entries = listFilesIn(dir)
    file_reg = []
    for file_path in entries:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                file_reg.append((file_path, line))
    return file_reg

def new_regs_exist_at(dir, old_regs):
    return list(set([file for file, reg in read(dir) if reg not in old_regs and is_valid(reg)]))

def is_txt(file_name):
    return TXT_EXTENTION in file_name

def is_cico_file(file_name):
    return CICO_FILE_KEYWORD in file_name and is_txt(file_name)

def keep_only_cico_files(files):
    return [file for file in files if is_cico_file(file)]

def directorie_of(path):
    return DIR_SEPARATOR.join(path.split(DIR_SEPARATOR)[:-1]) if isfile(path) else path

def directories_of(paths):
    return [directorie_of(path) for path in paths]
