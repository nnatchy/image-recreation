#!/bin/sh

poetry install --no-root --no-dev

poetry run streamlit run app/streamlit.py --server.port 8501 --server.address 0.0.0.0 --server.runOnSave true

wait -n

exit $?
