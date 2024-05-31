FROM ubuntu

RUN apt update
RUN apt install -y python3 python3-pip
RUN apt install -y python3-dev


COPY . /prami/flask/

RUN pip3 install -r /prami/flask/requirements.txt --break-system-packages

# ENTRYPOINT [ "flask", "run" ]
CMD flask run -h 0.0.0.0