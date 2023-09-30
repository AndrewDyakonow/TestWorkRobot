FROM python:3.11.4-alpine3.17

WORKDIR /R4C/

COPY . .

RUN chmod +x entrypoint.sh

RUN pip install -r requirements.txt

CMD ["sh", "entrypoint.sh"]