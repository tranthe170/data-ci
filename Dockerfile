FROM python:3.9.5

WORKDIR /code
ENV PYTHONPATH=/code/src

ADD ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

ADD ./ /code/

ENTRYPOINT [ "tail", "-f", "/dev/null" ]