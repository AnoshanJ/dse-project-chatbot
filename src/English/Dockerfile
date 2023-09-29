FROM python:3.7-slim

RUN python -m pip install rasa && \
    python -m pip install rasa[spacy] && \
    python -m spacy download en_core_web_md && \
    python -m spacy link en_core_web_md en

WORKDIR /app
COPY . .

# RUN rasa train

# set the user to run, don't run as root
USER 1001

ENTRYPOINT ["rasa"]

CMD ["run", "--enable-api", "--port", "5005"]


