# -*- coding:utf-8 -*-
import sys

import os


def get_project_dir():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))


def get_src_dir():
    return os.path.join(get_project_dir(), 'src')


def get_core_model_dir():
    return os.path.join(get_project_dir(), 'models/core')


def get_nlu_model_dir():
    return os.path.join(get_project_dir(), 'models/nlu')


def get_data_path():
    return os.path.join(get_project_dir(), 'data')


def get_resource_dir():
    return os.path.join(get_src_dir(), 'resource')


def get_package_path():
    dirname_list = [dirname for dirname in sys.path if 'site-packages' in dirname]
    return os.path.abspath(dirname_list[0]) if len(dirname_list) > 0 else None


def get_file_path(file_path):
    (filepath, tempfilename) = os.path.split(file_path)
    return filepath


def get_file_name(file_path):
    (filepath, tempfilename) = os.path.split(file_path)
    (filename, extension) = os.path.splitext(tempfilename)
    return filename


def get_file_format(file_path):
    (filepath, tempfilename) = os.path.split(file_path)
    (filename, extension) = os.path.splitext(tempfilename)
    return extension
