# -*- coding:utf-8 -*-
import os
import yaml
import codecs
import logging.config
from src.libs.path_utils import get_project_dir


def get_logger(name='root'):
    logging_cfg = os.path.abspath(os.path.join(get_project_dir(), './cfg/logging.yaml'))
    if os.path.exists(logging_cfg):
        with codecs.open(logging_cfg, 'r', encoding='utf8') as f:
            logging_cfg_dict = yaml.safe_load(f.read())
            handlers = logging_cfg_dict.get('handlers')
            if handlers:
                for handle_k, handler in handlers.items():
                    if not handler.get('filename'):
                        continue
                    log_filename = os.path.basename(handler['filename'])
                    log_dir = os.path.dirname(handler['filename'])
                    if log_dir[0] != '/':
                        log_dir = os.path.abspath(os.path.join(get_project_dir(), log_dir))
                    if not os.path.exists(log_dir):
                        os.makedirs(log_dir)
                    logging_cfg_dict['handlers'][handle_k]['filename'] = os.path.join(log_dir, log_filename)
        logging.config.dictConfig(logging_cfg_dict)
    else:
        print(u'默认日志配置不存在，默认路径：{}'.format(logging_cfg))
    return logging.getLogger(name)



