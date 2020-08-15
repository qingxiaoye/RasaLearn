# -*- coding:utf-8 -*-

from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter
import os
from src.libs.path_utils import get_nlu_model_dir, get_data_path

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


def train_stories_online(input_channel,
                         interpreter,
                         domain_file=os.path.join(get_data_path(), 'court/domain.yml'),
                         training_data_file=os.path.join(get_data_path(), 'court/court_stories.md')):
    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(),
                            KerasPolicy()],
                  interpreter=interpreter)

    agent.train_online(training_data_file,
                       input_channel=input_channel,
                       max_history=2,
                       batch_size=20,
                       epochs=100)
    return agent


if __name__ == '__main__':
    _path = os.path.join(get_nlu_model_dir(), 'court/default/')
    _model = os.listdir(_path)[-1]
    nlu_interpreter = RasaNLUInterpreter(_path + '/' + _model)
    train_stories_online(ConsoleInputChannel(), nlu_interpreter)
