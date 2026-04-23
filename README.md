# Airflow File Pipeline

Small Apache Airflow project that demonstrates a simple file ingestion workflow.

The DAG validates a source file, prepares a Bronze folder, copies the file, and writes ingestion metadata.

## What This Project Shows

- Airflow DAG structure
- BashOperator usage
- Docker Compose-based local Airflow environment
- Basic orchestration workflow from input to bronze folder
- File validation before ingestion
- Metadata creation after ingestion

## Pipeline Flow

```text
data/input/sample.csv
        |
        v
validate_input_file
        |
        v
prepare_bronze_directory
        |
        v
copy_file_to_bronze
        |
        v
write_ingestion_metadata
        |
        v
data/bronze/sample.csv
data/bronze/sample.metadata.json
```

## Project Structure

```text
dags/
  file_copy_dag.py
docker-compose.yaml
data/
  input/
    sample.csv
docs/
  architecture.md
```

## Run Locally

```bash
docker compose up airflow-init
docker compose up
```

Open Airflow at:

```text
http://localhost:8080
```

Default local credentials:

```text
username: airflow
password: airflow
```

Then trigger the `file_copy_dag` DAG from the Airflow UI.

## Output

After a successful run, the pipeline creates:

```text
data/bronze/sample.csv
data/bronze/sample.metadata.json
```

## Possible Improvements

- Add file size and row count validation
- Add failure notifications
- Add a real object storage source
- Replace BashOperator steps with PythonOperator tasks for richer metadata

## Interview Summary

This project demonstrates Airflow orchestration basics and a simple file-based ingestion pattern that can be extended into a larger batch pipeline.
