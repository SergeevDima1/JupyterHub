FROM jupyter/scipy-notebook:ed2908bbb62e

RUN conda install --quiet --yes \
 'r-base' \
 'r-irkernel' && \
 conda clean -tipy && \
 fix-permissions $CONDA_DIR

RUN pip install \
 sas7bdat && \
 fix-permissions $CONDA_DIR
