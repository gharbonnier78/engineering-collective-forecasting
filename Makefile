.PHONY: validate test paper clean

validate:
	python scripts/validate_repo.py

test:
	python -m unittest discover -s tests -v

paper:
	cd paper && latexmk -pdf -interaction=nonstopmode -halt-on-error engineering_collective_forecasting.tex

clean:
	cd paper && latexmk -C engineering_collective_forecasting.tex
