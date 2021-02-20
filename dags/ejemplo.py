
from airflow import DAG 
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

default_args = {
    'owner':"airflow"}

dag = DAG (
    'bash-task',
    schedule_interval=timedelta(minutes=30),
    default_args=default_args,
    start_date=days_ago(2),
)

bash_task = BashOperator (dag=dag,
                          task_id="bash",
                          bash_command="echo 1"
)

bash_task_2 = BashOperator (dag=dag,
                            task_id="bash-2",
                            bash_command="echo 2"
)

bash_task_3 = BashOperator (dag=dag,
                            task_id="bash-3",
                            bash_command="echo 3"
)

bash_task_2.set_upstream(bash_task)

bash_task_3.set_upstream(bash_task)