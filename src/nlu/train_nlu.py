# --*-- coding:utf-8 --*--

from rasa_nlu_gao.training_data.loading import load_data
from rasa_nlu_gao import config as nlu_config
from rasa_nlu_gao.model import Trainer
import os
from src.libs.path_utils import get_project_dir, get_data_path, get_src_dir
from src.libs.cfg_utils import get_config_dict
from rasa_nlu.model import Interpreter
from rasa_core import server

dic = get_config_dict().get('DataPath', None)
court_nlu = dic.get('court')


def train_nlu(data=os.path.join(get_data_path(), 'court/court_nlu.md'),
              config=os.path.join(get_project_dir(), 'cfg/policy_config.yml'),
              model_dir=os.path.join(get_project_dir(), 'models/nlu/court')):
    print(data,config,model_dir)
    training_data = load_data(data)
    trainer = Trainer(nlu_config.load(config))
    trainer.train(training_data)
    trainer.persist(model_dir)




def test_nlu(sentence):
    _path = os.path.join(get_project_dir(), 'models/nlu/court/default')
    _model = os.listdir(_path)[-1]
    interpreter = Interpreter.load(_path + '/' + _model)
    print(interpreter.parse(sentence))


train_nlu()
