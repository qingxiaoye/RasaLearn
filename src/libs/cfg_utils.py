# -*- coding:utf-8 -*-
import json
from configparser import ConfigParser
import codecs
import os


from src.libs.path_utils import get_project_dir


class ConfigDictParser(ConfigParser):
    def as_dict(self):
        d = dict(self._sections)
        for k, v in d.items():
            d[k] = dict(v)

        return d


def get_config_dict(conf_file='config.ini', conf_path='./cfg'):
    if conf_path[0] != '/':
        conf_path = os.path.abspath(os.path.join(get_project_dir(), conf_path))
    conf_file = os.path.join(conf_path, conf_file)

    if not os.path.exists(conf_file):
        raise RuntimeError(u'配置文件不存在')

    cf = ConfigDictParser()
    cf.read(conf_file, encoding='utf-8')

    return cf.as_dict()



