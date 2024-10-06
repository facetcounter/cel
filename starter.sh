#!/bin/bash
fastapi run main.py --port 8000 &
python weatherFetch.py &
wait -n
exit $?