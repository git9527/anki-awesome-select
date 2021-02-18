#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path

base_folder = str(Path.home()) + '/Documents/学习强国/'


def get_answer(answer_index):
    answer_line = striped_lines[answer_index]
    return answer_line.split("正确答案：", 1)[1]


def get_end_with_target(start_index, target):
    end_index = start_index
    next_line = full_line[start_index: end_index]
    while not next_line.endswith(target):
        end_index = end_index + 1
        next_line = full_line[start_index:end_index]
    return end_index


def get_option_end(start_index):
    return get_end_with_target(start_index, '正确答案：') - 5


def get_question_end(start_index):
    return get_end_with_target(start_index, '选项：') - 3


def get_answer_end(start_index):
    return get_end_with_target(start_index, '  ') - 2


def get_combined_array(source, step):
    arr = []
    for i in range(0, len(source), step):
        arr.append(" ".join(source[i:i + step]))
    return arr


def get_formatted_answers(question, answer):
    count = question.count("【 ")
    answer_array = answer.split(" ")
    if count != len(answer_array):
        raise Exception
    for i in range(0, count):
        question = question.replace("【    】", '<font color="#e25b76">{{c1::【' + answer_array[i] + '】}}</font>', 1)
    return question


def get_question_and_answers(question_start_index):
    question_end_index = get_question_end(question_start_index)
    question_line = full_line[question_start_index: question_end_index]
    question = question_line.split(".", 1)[1].strip()
    options_start_index = question_end_index + 3
    options_end_index = get_option_end(options_start_index)
    options = full_line[options_start_index: options_end_index].strip().split(" ")
    answer_start_index = options_end_index + 5
    answer_end_index = get_answer_end(answer_start_index)
    answer = full_line[answer_start_index: answer_end_index]
    if question.count("【") > 1 and " " in answer:
        options = get_combined_array(options, question.count("【"))
    answer_index = options.index(answer) + 1
    formatted_question = get_formatted_answers(question, answer)
    return {
        "question": question,
        "options": options,
        "answer": answer,
        "answer_index": str(answer_index),
        "next_index": answer_end_index + 1,
        "formatted_question": formatted_question,
        "formatted_options": "||".join(options)
    }


def find_tag_by_seq(seq):
    for key in tags:
        if seq in tags[key]:
            print('found tag:', key, 'for seq', seq)
            return key
    return ''


striped_lines = []

with open(base_folder + '争上游题库2021年2月10日1946题库答案-2.txt', 'r') as file:
    for line in file:
        striped_line = line.removesuffix("\n")
        if striped_line:
            striped_lines.append(striped_line)

with open(base_folder + '争上游题库2021年2月10日1946题库答案-3.txt', 'w') as file:
    full_content = "".join(striped_lines)
    file.write(full_content)
with open(base_folder + '争上游题库2021年2月10日1946题库答案-3.txt', 'r') as file:
    for line in file:
        full_line = line

tags = {}
with open(base_folder + 'tags.txt', 'r') as file:
    for line in file:
        tokens = line.strip().split(":")
        tags[tokens[0]] = tokens[1]

with open(base_folder + '强国题库-0218.txt', 'w') as file:
    next_index = 0
    for i in range(1, 1947):
        question_index = '{:04d}'.format(i)
        block = get_question_and_answers(next_index)
        next_index = block['next_index']
        tag = find_tag_by_seq(question_index)
        line = question_index + "\t" + block['formatted_question'] + "\t" + block['formatted_options'] + "\t" + block[
            'answer_index'] + "\t" + tag + "\n"
        file.write(line)
