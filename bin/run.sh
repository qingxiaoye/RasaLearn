#!/bin/bash
source /home/user/shixy/pythonflow/venv/bin/activate
bin_path="$( cd "$( dirname "$0"  )" && pwd  )"
model_path=$(dirname $bin_path)/models
log_path=$(dirname $bin_path)/log
src_path=$(dirname $bin_path)/src
court_core_model="$model_path/core/court/dialogue"
case_core_model="$model_path/core/case/dialogue"
judge_core_model="$model_path/core/judge/dialogue"
court_nlu_model="${model_path}/nlu/court/default"
case_nlu_model="${model_path}/nlu/case/default"
judge_nlu_model="${model_path}/nlu/judge/default"
cd $case_nlu_model
filename=`ls -l | tail -n 1 | awk '{print $9}'`
case_nlu="$case_nlu_model/$filename"
cd $court_nlu_model
filename=`ls -l | tail -n 1 | awk '{print $9}'`
court_nlu="${court_nlu_model}/$filename"
cd $judge_nlu_model
filename=`ls -l | tail -n 1 | awk '{print $9}'`
judge_nlu="${judge_nlu_model}/$filename"

PYTHONPATH=$(dirname $bin_path)

echo "开始启rasa"
echo "启动 8853 case"
nohup python -m rasa_core.server -d $case_core_model -u $case_nlu -p 8853 --cors * -o $log_path/case_parser.log > /dev/null 2>&1 &
echo "启动8852 court"
nohup python -m rasa_core.server -d $court_core_model -u $court_nlu -p 8852 --cors * -o $log_path/court_parser.log > /dev/null 2>&1 &
echo "启动8851 judge"
nohup python -m rasa_core.server -d $judge_core_model -u $judge_nlu -p 8851 --cors * -o $log_path/judge_parser.log > /dev/null 2>&1 &

echo "启动 server"
nohup python $src_path/run_ws.py > /dev/null 2>&1 &
#python $src_path/run_server.py &

echo "成功"
