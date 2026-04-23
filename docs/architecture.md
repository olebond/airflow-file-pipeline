# Architecture Notes

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

## Purpose

This project demonstrates a small Airflow orchestration workflow for a file ingestion process.

The DAG validates that an input file exists, prepares a Bronze folder, copies the file, and writes a simple metadata record for traceability.

## Portfolio Notes

This is intentionally small. The goal is to show Airflow fundamentals: DAG structure, task dependencies, retries, Docker Compose setup, and a simple ingestion pattern.
