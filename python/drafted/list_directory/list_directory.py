#!/usr/intel/pkgs/python3/3.7.4/bin/python3

from os.path import abspath, isdir, join
import subprocess
import sys
import os
import re

ansi_escape = re.compile(r'(\x1B[@-_][0-?]*[ -/]*[@-~])')


if 'color codes':

    reset_color = '\033[0;0m'
    red         = '\033[0;31m'
    green       = '\033[0;32m'
    yellow      = '\033[0;33m'
    blue        = '\033[0;34m'
    megenta     = '\033[0;35m'
    cyan        = '\033[0;36m'
    white       = '\033[0;37m'

    # Bold
    Bred         = '\033[1;31m'
    Bgreen       = '\033[1;32m'
    Byellow      = '\033[1;33m'
    Bblue        = '\033[1;34m'
    Bmegenta     = '\033[1;35m'
    Bcyan        = '\033[1;36m'
    Bwhite       = '\033[1;37m'

    # Underline
    Ured         = '\033[4;31m'
    Ugreen       = '\033[4;32m'
    Uyellow      = '\033[4;33m'
    Ublue        = '\033[4;34m'
    Umegenta     = '\033[4;35m'
    Ucyan        = '\033[4;36m'
    Uwhite       = '\033[4;37m'

    grey        = '\033[90m'
    dark_blue   = '\033[94m'


def filesystem_processing(filesystems):

    infos, color_codes, filenames = [], [], []
    for filesystem in filesystems:

        if 'total ' in filesystem:
            continue

        if ' ' in filesystem:
            if ' -> ' in filesystem:  # Symlink
                info, link_name, symbol, link_source = filesystem.rsplit(' ', 3)
                filename = ' '.join([link_name, symbol, link_source])
            else:
                info, filename = filesystem.rsplit(' ', 1)

            match = ansi_escape.search(filename)
            if match is None: color_codes.append('')
            else            : color_codes.append(match.group(1))

            filename = ansi_escape.sub('', filename)
            filenames.append(filename)

            infos.append(info)

    return infos, color_codes, filenames


def generate_alias(filesystems, infos, filenames):

    msg = ''
    alias_asc, alias_desc = '', ''
    counter_asc, counter_desc = 0, len(infos)

    for line in filesystems:
        if line.startswith('total '):
            msg += f'{line}\n'
            break

    for index, (info, filename) in enumerate(zip(infos, filenames)):

        symlink_directory = False
        filename_no_color = ansi_escape.sub('', filename)
        if ' -> ' in filename:
            symlink_directory = True

        if ' -> ' in filename: filepath = abspath(filename_no_color.split(' ')[-1])
        else                 : filepath = abspath(filename_no_color)

        counter_asc += 1

        if isdir(filepath):  # Directory
            if symlink_directory: prefix = f'{grey}L{Bcyan}{counter_asc:>2}'
            else:                 prefix = f'{grey}L{Bblue}{counter_asc:>2}'
            msg += f'{info} [{prefix}][{counter_desc:2d}] {filename}{reset_color}\n'

            alias_asc  += f'alias  {counter_desc} "cd {filepath}; l"\n'
            alias_desc += f'alias l{counter_asc}  "cd {filepath}; l"\n'
        else:  # File
            if symlink_directory:
                prefix = f'{grey}L{Bcyan}{counter_asc:>2}'
                msg += f'{info} [{prefix}]{Bcyan}[{counter_desc:2d}] {filename}{reset_color}\n'
            else:
                prefix = f'{grey}L{Bgreen}{counter_asc:>2}'
                msg += f'{info} [{prefix}]{Bgreen}[{counter_desc:2d}] {filename}{reset_color}\n'

            alias_asc  += f'alias  {counter_desc} "gvim {filepath}"\n'
            alias_desc += f'alias l{counter_asc}  "gvim {filepath}"\n'

        counter_desc -= 1

    return msg, alias_asc, alias_desc


def main(argv):

    # Step 1: Get directory infos
    current_directory = os.getcwd()

    filesystems = subprocess.getoutput(f'ls {current_directory} -ltrh --color=always')
    filesystems = filesystems.split('\n')

    # Step 2: Process directory infos
    infos, color_codes, filenames = filesystem_processing(filesystems=filesystems)

    # Step 3: Filtering feature
    if len(argv) > 0:

        filtered_infos, filtered_filenames = [], []
        for keyword in argv:
            keyword = keyword.lower()

            for index, (line, info, color_code, filename) in enumerate(zip(filesystems, infos, color_codes, filenames)):
                if keyword in filename.lower():
                    filename = re.sub(f'({keyword})', red + r'\1' + color_code, filename, flags=re.IGNORECASE)
                    filtered_filenames.append(filename)
                    filtered_infos.append(info)

        infos = filtered_infos
        filenames = filtered_filenames

    # Step 4: Generate msg and aliases
    msg, alias_asc, alias_desc = generate_alias(filesystems, infos, filenames)

    print(msg)
    print(current_directory)

    # Step 4: Export aliases
    alias_filepath = join(os.getenv('HOME'), '.list_directory_alias')
    fh = open(alias_filepath, 'w')
    text = alias_asc + '\n' + alias_desc
    fh.write(text)
    fh.close()


if __name__ == '__main__':
    argv = sys.argv[1:]
    main(argv=argv)
