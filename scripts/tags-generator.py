#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path

base_folder = str(Path.home()) + '/Documents/学习强国/'

tags = {}


def add_tag_with_seq(tag, seq):
    existing = tags.get(tag)
    if existing is None:
        tags[tag] = seq
    else:
        existing = existing + ',' + seq
        tags[tag] = existing


with open(base_folder + '学习强国-0218.txt', 'r') as file:
    for line in file:
        tokens = line.strip().split('\t')
        if len(tokens) == 5:
            tag_tokens = tokens[4].split(' ')
            for tag_token in tag_tokens:
                print('add tag', tag_token, 'with seq', tokens[0])
                add_tag_with_seq(tag_token, tokens[0])

with open(base_folder + 'tags_generated.txt', 'w') as file:
    for tag in tags:
        file.write(tag + ':' + tags[tag] + '\n')
