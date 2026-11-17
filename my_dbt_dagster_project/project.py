import os
from pathlib import Path

from dagster_dbt import DbtProject

# Folder that contains this repo (two levels up from this file)
REPO_ROOT = Path(__file__).resolve().parents[1]

# dbt project: DBT_PROJECT_DIR if set, otherwise a sibling clone of dbt-airbnb-project
DBT_PROJECT_DIR = Path(
    os.getenv("DBT_PROJECT_DIR", REPO_ROOT.parent / "dbt-airbnb-project")
).resolve()

airbnb_project = DbtProject(
    project_dir=DBT_PROJECT_DIR,
    packaged_project_dir=REPO_ROOT / "dbt-project",
    profiles_dir=DBT_PROJECT_DIR / "_prod_profiles",
    install_deps=False,
)
airbnb_project.prepare_if_dev()