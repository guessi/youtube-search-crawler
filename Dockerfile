FROM python:3.10-alpine3.16
WORKDIR /opt
COPY requirements.txt main.py search.py /opt/
RUN pip3 install -r requirements.txt
EXPOSE 8080
CMD ["./main.py"]
