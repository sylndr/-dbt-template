from datetime import datetime
from pathlib import Path

from airflow.decorators import dag
from airflow.models.baseoperator import chain
from cosmos import DbtTaskGroup
from cosmos.config import ProfileConfig, ProjectConfig, RenderConfig
from cosmos.constants import LoadMode
from cosmos.profiles import (
    GoogleCloudServiceAccountDictProfileMapping,
)

base_directory = Path(__file__).parent.resolve()
dbt_project_path = base_directory.joinpath("dbt").joinpath("{{cookiecutter.project_slug}}").resolve()
profile_config = ProfileConfig(
    profile_name="{{cookiecutter.project_slug}}",
    target_name="{{cookiecutter.default_dataset}}",
    profile_mapping=GoogleCloudServiceAccountDictProfileMapping(  # type: ignore
        conn_id="BIG_QUERY_DBT_CONN",
    ),
)

project_config = ProjectConfig(
    dbt_project_path=dbt_project_path,
)

@dag(
    dag_id="{{cookiecutter.project_dag_name}}",
    start_date=datetime(2023, 1, 1),
    schedule=None,
    catchup=False,
    tags=['dbt', '{{cookiecutter.project_slug}}'],
)
def {{cookiecutter.project_dag_name}}_function():
    transform = DbtTaskGroup(
        group_id="transform",
        project_config=project_config,
        profile_config=profile_config,
        render_config=RenderConfig(
            load_method=LoadMode.DBT_LS, select=["path:models"]
        ),
    )

    transform # type: ignore

{{cookiecutter.project_dag_name}}_function()