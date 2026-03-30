from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

# declare a DAG
with DAG(dag_id='dsde_simplebash', start_date=datetime(2021, 1, 1)):

	# declare a TASK
	echo = BashOperator(task_id='echo_template', bash_command='echo "run_id = {{ run_id }} and ds = {{ ds }}"')
