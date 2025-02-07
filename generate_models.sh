#!/bin/bash

if [ ! -e fhir-parser ]; then
	git submodule update --init --recursive
fi

cp fhir-parser-resources/settings.py fhir-parser/settings.py
cd fhir-parser
pipenv run python ./generate.py $1
cd ..
