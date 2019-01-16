echo "154.8.196.249:8000"
mode=$1
if [ -n "$mode"  -a  "$mode" == "y" ];then
    nohup python manage.py runserver 0.0.0.0:8000 &
else
    python manage.py runserver 0.0.0.0:8000
fi
