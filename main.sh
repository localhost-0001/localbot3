#!/bin/bash

main(){
    python3 main.py
}
while true; do

 until main; do
     echo "'main' crashed with exit code $?.  Restarting..." >&2
     sleep 1
 done
done
