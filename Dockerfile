FROM python:3.6-alpine
ADD . /
WORKDIR /
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
CMD python app.py