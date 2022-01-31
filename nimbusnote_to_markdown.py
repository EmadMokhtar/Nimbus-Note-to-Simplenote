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


def convert_to_markdown(path, tag_list=None):
    """
    Travel over the directory and converts the Nimbus exported notes (*.zip) 
    to markdown files.
    """
    if tag_list is None:
        tag_list = []
    
    dir_list = listdir(path)
    for dir in dir_list:
        if '.zip' in dir:
            zip_path = f'{path}\{dir}'
            zf = ZipFile(zip_path)
            note = BeautifulSoup(zf.open('note.html'), 'html.parser')
            title = note.title.text
            body = str(note.body.find(id="note-root"))
            content = markdownify(body)
            # Export the markdown file to disk.
            note = MarkdownNote(title, content, tag_list)
            note.export(path)

        else:
            jong_path = f'{path}\{dir}'
            new_tag_list = tag_list.copy()
            new_tag_list.append(dir.lower().replace(' ', '_'))
            convert_to_markdown(jong_path, new_tag_list)


class MarkdownNote:
    def __init__(self, title:str, content:str, tage_list:list) -> Note:
        self.title = title
        self.content = content
        self.tage_list = tag_list

    def export(self, path: str):
        with open(f"{path}/{self.title}.md", "w") as md_file:
            md_file.Write(f"{self.title}\r\n{self.content})

def main():
    convert_to_markdown(path.abspath(argv[1]))

if __name__ == '__main__':
    main()
