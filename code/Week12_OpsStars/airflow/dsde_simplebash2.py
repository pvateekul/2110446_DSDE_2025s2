from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

# declare a DAG
with DAG(dag_id='dsde_simplebash_2', start_date=datetime(2021, 1, 1)):

	# declare 2 TASKS
	echo = BashOperator(task_id='echo_template', bash_command='echo "run_id = {{ run_id }} and ds = {{ ds }}"')
	echo2 = BashOperator(task_id='echo_template_2', bash_command='echo "run_id_2 = {{ run_id }} and ds = {{ ds }}"')

	# declare TASK dependency
	echo >> echo2
