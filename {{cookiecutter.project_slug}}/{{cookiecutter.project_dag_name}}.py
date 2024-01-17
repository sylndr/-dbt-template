from airflow.decorators import dag, task
from airflow.models.baseoperator import chain
from datetime import datetime

from pathlib import Path
from cosmos.airflow.task_group import DbtTaskGroup
from cosmos.constants import LoadMode
from cosmos.config import ProjectConfig, RenderConfig, ProfileConfig


@dag(
    start_date=datetime(2023, 1, 1),
    schedule=None,
    catchup=False,
    tags=['retail', 'dbt'],
)
def {{cookiecutter.project_slug}}():

    transform = DbtTaskGroup(
        group_id='transform',
        project_config=ProjectConfig(
            dbt_project_path='/opt/airflow/dags/dbt/{{cookiecutter.project_slug}}/',
        ),
        profile_config=ProfileConfig(
            profile_name='{{cookiecutter.project_slug}}',
            target_name='dev',
            profiles_yml_filepath=Path('/opt/airflow/dags/dbt/{{cookiecutter.project_slug}}/{{cookiecutter._profiles_file_name}}.yml')
        ),
        render_config=RenderConfig(
            load_method=LoadMode.DBT_LS,
            select=['path:models/transform']
        )
    )
    report = DbtTaskGroup(
        group_id='report',
            project_config=ProjectConfig(
                dbt_project_path='/opt/airflow/dags/dbt/{{cookiecutter.project_slug}}/',
            ),
        profile_config=ProfileConfig(
            profile_name='{{cookiecutter.project_slug}}',
            target_name='dev',
            profiles_yml_filepath=Path('/opt/airflow/dags/dbt/{{cookiecutter.project_slug}}/{{cookiecutter._profiles_file_name}}.yml')
        ),
        render_config=RenderConfig(
            load_method=LoadMode.DBT_LS,
            select=['path:models/report']
        )
    )

    chain(
        transform,
        report
    )
{{cookiecutter.project_slug}}()