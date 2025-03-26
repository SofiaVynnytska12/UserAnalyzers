FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt || echo "No requirements.txt found!"

COPY . .

CMD ["sh", "-c", "python $SCRIPT_NAME"]
