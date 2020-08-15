- 安装的包 
    - pip install rasa-core
    - pip install rasa_nlu[tensorflow]
- 模型的训练
    - rasa_core.train -d domain.yml -s stories.md -o models/dialogue

rasa_core.train -d ./configs/domain.yml -s ./data/stories/stories.md -o ./models/dialogue

- 模型的启动
    -  source  chat_env/bin/activate
    - 
python -m rasa_core.server -d ./models/core/court/dialogue   -u ./models/nlu/court/default/model_20200814-112041 -p 9900 --cors *
       
       
       
python -m rasa_core.visualize -d ./data/court/domain.yml  -s ./data/court/court_stories.md -o graph.html -c ./cfg/policy_config.yml 
 F:\yjcloud-learn\RasaLearn\cfg\policy_config.yml      
./data/court/domain.yml
./data/court/domain.yml192.168.100.210:9901/conversations/uuuoeh/respond