#!/usr/bin/env python3
from subprocess import call

FONTS_PATH = "assets/fonts"
STYLES_PATH = "assets/styles"
BUILD_PATH = "build"
SOURCE = "src/book.adoc"

OUTPUT = "Book.pdf"
ARGS = "-a pdf-fonts-dir={} -a pdf-stylesdir={} -a pdf-style=default -D {} -o {} {}".format(FONTS_PATH, STYLES_PATH, BUILD_PATH, OUTPUT, SOURCE)
command = "asciidoctor-pdf {}".format(ARGS)
call(command.split(' '))
