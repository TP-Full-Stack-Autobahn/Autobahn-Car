FROM python:3.7-alpine
WORKDIR /src
ENV FLASK_APP=src/__init__.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5002
RUN apk add --no-cache gcc musl-dev linux-headers
RUN pip install setuptools-scm && pip install --upgrade setuptools
COPY . /src/
RUN python setup.py install
CMD ["flask", "run"]