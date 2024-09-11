.PHONY: clean
.SUFFIXES: .md .rst .html .pdf

PANDOCVARS=-V documentclass:article -V geometry:margin=.75in -Vcolorlinks:true
SOURCE=Lab1.md 
TEMPLATES=Lab1.py ../through_the_looking_glass.txt
TARGETS=Lab1.pdf Lab1.html Lab1.zip ${TEMPLATES}
OUTDIR=../../docs/labs/lab01

all: ${TARGETS}
	mkdir -p ${OUTDIR}
	cp Lab1.html ${OUTDIR}/index.html
	cp Lab1.zip ${OUTDIR}

Lab1.pdf: ${SOURCE}

Lab1.html: ${SOURCE}

Lab1.zip: Lab1.pdf 
	zip -r -9 Lab1.zip Lab1.pdf ${TEMPLATES}

clean:
	${RM} *.html Lab1.pdf Lab1.zip
	${RM} -rf __pycache__

tidy:
	${RM} ${TARGETS}

spotless:
	${RM} -rf ${OUTDIR}

.md.pdf:
	pandoc ${PANDOCVARS} --pdf-engine=xelatex -o $@ $<

.rst.pdf:
	pandoc ${PANDOCVARS} --pdf-engine=xelatex -o $@ $<

.md.html:
	pandoc $< -t html -s -o $@
