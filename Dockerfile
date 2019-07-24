FROM python:3.7-alpine3.10
WORKDIR /opt
COPY requirements.txt main.py search.py /opt/
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD ["./main.py"]
