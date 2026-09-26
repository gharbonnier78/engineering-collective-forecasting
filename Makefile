.PHONY: validate test paper clean paper-repro

validate:
	python scripts/validate_repo.py

test:
	python -m unittest discover -s tests -v

paper:
	bash scripts/build_paper.sh

clean:
	cd paper && latexmk -C engineering_collective_forecasting.tex

paper-repro:
	bash scripts/build_paper.sh
	cp paper/engineering_collective_forecasting.pdf /tmp/ecf-paper-first.pdf
	$(MAKE) clean
	bash scripts/build_paper.sh
	cmp /tmp/ecf-paper-first.pdf paper/engineering_collective_forecasting.pdf
	sha256sum paper/engineering_collective_forecasting.pdf
