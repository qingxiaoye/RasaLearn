stop_server(){
    for port in 5889 8851 8852 8853;do
        _pid=`netstat -nltp | grep $port | awk '{print $7}' | cut -d \/ -f 1`
        if [ ! -z $_pid ];then
            echo "killing..." $_pid
            kill -9 $_pid
        else
            echo "done"
        fi
    done

    pid=`ps -ef | grep run_ws | grep -v grep | awk '{print $2}'`

    if [ ! -z $pid ];then
        echo "killing..." $pid
        kill -9 $pid
    else
        echo "done"
    fi

}


stop_server
