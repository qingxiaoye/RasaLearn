

"""
训练core模型
"""""
from rasa_core.agent import Agent
from rasa_core.policies.fallback import FallbackPolicy
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from src.libs.path_utils import get_data_path, get_core_model_dir
import os

if __name__ == '__main__':
    training_data_file = os.path.join(get_data_path(), 'court/court_stories.md')
    domain_file = os.path.join(get_data_path(), 'court/domain.yml')
    model_path = os.path.join(get_core_model_dir(), 'court/dialogue')
    print(training_data_file,domain_file,model_path)
    fallback = FallbackPolicy(fallback_action_name='utter_default', nlu_threshold=0.5, core_threshold=0.3)
    agent = Agent(domain_file, policies=[MemoizationPolicy(max_history=2), KerasPolicy()])
    # agent = Agent(domain_file)
    training_data = agent.load_data(training_data_file)
    agent.train(training_data_file,
                epochs=100,
                batch_size=30,
                validation_split=0.2,
                augmentation_factor=50)
    agent.persist(model_path)
