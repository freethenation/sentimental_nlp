FROM python:3.7.0-stretch
COPY ./fastText /usr/local/src/
# RUN cd /usr/local/src/; make
RUN pip install numpy scipy flask pybind11
RUN cd /usr/local/src/; make; pip install .