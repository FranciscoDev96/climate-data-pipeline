End-to-end data pipeline that consumes climate data from an API, processes it through multiple layers (Bronze, Silver and Gold), stores it in SQL database, and provides insights through Power BI dashboards. 

Architecture:

API ->  RAW (JSON) -> Processed -> CSV -> SQL -> Power BI 

Project Status

- [X] Ingest data from API
- [X] Store in raw layers (JSON)
- [X] Transform and clean data (Silver Layer)
- [ ] Put all totgether in an only dataset (CSV)
- [ ] Store in SQL dataset
- [ ] Dashboard in Power BI

Technologies 

- Python
- Requests
- JSON
- SQL (planned)
- Power BI (planned)

How to run 

'''bash

python src/ingest.py
python src/transform.py

Notes

Raw and processed data are not versioned in this repository.

To reproduce the pipeline, run the ingestion and transformation scripts.

