echo "154.8.196.249:8000"
mode=$1
if [ -n "$mode"  -a  "$mode" == "y" ];then
    nohup python manage.py runserver 0.0.0.0:80 &
else
    python manage.py runserver 0.0.0.0:80
fi
