HERE = $(shell pwd)
BIN = $(HERE)/bin
PYTHON = $(BIN)/python

INSTALL = $(BIN)/pip install
VTENV_OPTS ?= --distribute
ES_VERSION ?= 0.20.4

BUILD_DIRS = bin build elasticsearch include lib lib64 man share

.PHONY: all clean test

all: build

$(PYTHON):
	virtualenv $(VTENV_OPTS) .

build: $(PYTHON)
	$(PYTHON) setup.py develop
	$(INSTALL) monolith-aggregator[test]

clean:
	rm -rf $(BUILD_DIRS)

test: build elasticsearch
	$(BIN)/nosetests -s -d -v --with-coverage --cover-package aggregator aggregator

elasticsearch:
	curl -C - --progress-bar http://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-$(ES_VERSION).tar.gz | tar -zx
	mv elasticsearch-$(ES_VERSION) elasticsearch
	chmod a+x elasticsearch/bin/elasticsearch
	mv elasticsearch/config/elasticsearch.yml elasticsearch/config/elasticsearch.in.yml
	cp elasticsearch.yml elasticsearch/config/elasticsearch.yml
