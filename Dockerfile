FROM python:3.11-alpine3.17
WORKDIR /opt
COPY requirements.txt main.py search.py /opt/
RUN pip3 install -r requirements.txt
EXPOSE 8080
CMD ["./main.py"]
