"""
Simple script to help convert Nimbus notes to Simplenote.
    Author: Stanik
    Email: stanik@tuta.io
    GitHub: https://github.com/stanik120
    License: GPL 3
    Python Version: 3.9.1
"""
from os import listdir, path
from sys import argv
from zipfile import ZipFile
from bs4 import BeautifulSoup
from markdownify import markdownify
import json


notes_json = {
    "activeNotes": [],
    "trashedNotes": []
}


def convert_to_simplenote(path, tag_list=[]):
    dir_list = listdir(path)
    for dir in dir_list:
        if '.zip' in dir:
            zip_path = f'{path}\{dir}'
            zf = ZipFile(zip_path)
            note = BeautifulSoup(zf.open('note.html'), 'html.parser')
            title = note.title.text
            body = str(note.body.find(id="note-root"))
            content = markdownify(body)

            note = {
                "id": "",
                "content": f"{title}\r\n{content}",
                "creationDate": "",
                "lastModified": "",
                "tags": tag_list
            }
            notes_json["activeNotes"].append(note)

        else:
            jong_path = f'{path}\{dir}'
            new_tag_list = tag_list.copy()
            new_tag_list.append(dir)
            convert_to_simplenote(jong_path, new_tag_list)


def main():
    convert_to_simplenote(path.abspath(argv[1]))
    with open('notes.json', 'w') as f:
        json.dump(notes_json, f)


if __name__ == '__main__':
    main()
