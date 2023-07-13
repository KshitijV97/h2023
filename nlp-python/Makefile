install:
	pip3 install -r requirements.txt

auth:
	gcloud auth application-default login && gcloud auth application-default set-quota-project ac-cntxtlbank-sct-project

run:
	python3 main.py

build-image:
	docker build --no-cache -t h2023-python .

run-image:
	docker run -p 8080:8080 h2023-python

run-in-docker: build-image run-image