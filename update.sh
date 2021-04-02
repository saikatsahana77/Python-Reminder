#!/bin/bash

kill $(pgrep -f 'python3 notification.py')
python3 notification.py