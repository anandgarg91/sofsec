# slides template Makefile

# PANDOC
# Compile using make pdf. Current slide level is set to 2
# http://jeromyanglim.blogspot.sg/2012/07/beamer-pandoc-markdown.html
# http://pandoc.org/demo/example9/producing-slide-shows-with-pandoc.html

SLIDE_OUT = Sidechannel-slides


LATEX_OPTS = -shell-escape
PANDOC_OPTS = --slide-level 2 -t beamer  --filter pandocfilter-overlay.py
RM_OPTS = -f

TEX_SOURCES =
MD_SOURCES =

slides:
	pandoc mdslides.md $(PANDOC_OPTS) -o mdslides.tex
	pdflatex $(LATEX_OPTS) slides.tex
	pdflatex $(LATEX_OPTS) slides.tex
	mv slides.pdf $(SLIDE_OUT).pdf

slides-bib:
	pandoc mdslides.md $(PANDOC_OPTS) -o mdslides.tex
	pdflatex $(LATEX_OPTS) slides.tex
	pdflatex $(LATEX_OPTS) slides.tex
	bibtex slides
	pdflatex $(LATEX_OPTS) slides.tex
	pdflatex $(LATEX_OPTS) slides.tex
	mv slides.pdf $(SLIDE_OUT).pdf

slides-open:
	-xdg-open $(SLIDE_OUT).pdf &

## pdfpc primer
# -d minute duration
# -l last minutes
# -S force single screen
# -s switch monitors
# -n position notes left, right, bottom, top
slides-present:
	pdfpc -d 30 $(SLIDE_OUT).pdf

slides-clean:
	rm $(RM_OPTS) *~
	rm $(RM_OPTS) slides.aux
	rm $(RM_OPTS) slides.bbl
	rm $(RM_OPTS) slides.blg
	rm $(RM_OPTS) slides.log
	rm $(RM_OPTS) slides.nav
	rm $(RM_OPTS) slides.out
	rm $(RM_OPTS) slides.snm
	rm $(RM_OPTS) slides.toc
	rm $(RM_OPTS) slides.vrb


