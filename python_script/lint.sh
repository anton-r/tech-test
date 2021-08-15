#!/bin/bash

for i in $(ls | grep .py); do pylint $i; done
