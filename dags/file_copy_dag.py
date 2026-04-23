from __future__ import annotations

from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

INPUT_FILE = "/opt/airflow/data/input/sample.csv"
BRONZE_DIR = "/opt/airflow/data/bronze"
BRONZE_FILE = f"{BRONZE_DIR}/sample.csv"
METADATA_FILE = f"{BRONZE_DIR}/sample.metadata.json"


def _default_args():
    return {
        "owner": "oleksii",
        "depends_on_past": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=1),
    }


with DAG(
    dag_id="file_copy_dag",
    default_args=_default_args(),
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=["bronze", "file-transfer"],
) as dag:
    validate_input = BashOperator(
        task_id="validate_input_file",
        bash_command=f"test -s {INPUT_FILE}",
    )

    prepare_bronze = BashOperator(
        task_id="prepare_bronze_directory",
        bash_command=f"mkdir -p {BRONZE_DIR}",
    )

    copy_task = BashOperator(
        task_id="copy_file_to_bronze",
        bash_command=f"cp -f {INPUT_FILE} {BRONZE_FILE}",
    )

    write_metadata = BashOperator(
        task_id="write_ingestion_metadata",
        bash_command=(
            "python - <<'PY'\n"
            "from datetime import datetime, timezone\n"
            "import json\n"
            f"metadata_path = '{METADATA_FILE}'\n"
            "metadata = {\n"
            f"    'source_file': '{INPUT_FILE}',\n"
            f"    'target_file': '{BRONZE_FILE}',\n"
            "    'ingested_at_utc': datetime.now(timezone.utc).isoformat(),\n"
            "}\n"
            "with open(metadata_path, 'w', encoding='utf-8') as file:\n"
            "    json.dump(metadata, file, indent=2)\n"
            "PY"
        ),
    )

    validate_input >> prepare_bronze >> copy_task >> write_metadata
