
from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RasaNLUInterpreter


def run_bot(serve_forever=True):
        interpreter = RasaNLUInterpreter('/home/user/shixy/12368/src/rasa/nlu/model/default/model_20200407-175416')
        agent = Agent.load('./models/dialogue', interpreter = interpreter)

        if serve_forever:
                agent.handle_channel(ConsoleInputChannel())

        return agent

if __name__ == '__main__':
        run_bot()