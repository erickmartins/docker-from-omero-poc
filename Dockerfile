FROM python:3.6

WORKDIR /usr/src/app

COPY test_script.py ./
RUN pip install ezomero

COPY . .

ENTRYPOINT [ "python", "./test_script.py" ]
