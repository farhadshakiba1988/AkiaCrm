FROM i53051287x/farhad-base:1

COPY requirements.txt /app/requirements.txt
RUN /py/bin/pip install -r /app/requirements.txt

COPY . /app
WORKDIR /app
EXPOSE 8000

ENV PATH="/py/bin:$PATH"

COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY ./staticfiles /app/staticfiles

CMD ["/wait-for-it.sh", "db", "/entrypoint.sh"]