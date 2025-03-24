FROM python:3.11

WORKDIR /app

COPY . /app

RUN if [ -s requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

ENV SCRIPT_NAME=test.py

CMD ["sh", "-c", "python $SCRIPT_NAME"]

