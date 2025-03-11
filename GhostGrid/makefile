.PHONY: all mapgen mapview activate

VENV := ghostenv
PYTHON := $(VENV)/bin/python

all: mapgen mapview

$(VENV)/bin/activate:
	python3 -m venv $(VENV)
	$(PYTHON) -m pip install -r requirements.txt

mapgen: $(VENV)/bin/activate
	$(PYTHON) mapgen.py

mapview: $(VENV)/bin/activate
	$(PYTHON) mapview.py

activate: $(VENV)/bin/activate
	@echo "Virtual environment activated. Use 'source $(VENV)/bin/activate' to activate it in your shell."