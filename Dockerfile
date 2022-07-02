FROM python:3.9

# create the app user
RUN addgroup --system app && adduser --system --group app

WORKDIR /app/

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV ENVIRONMENT prod
ENV TESTING 0

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# Copy poetry.lock* in case it doesn't exist in the repo
COPY ./pyproject.toml ./poetry.lock* ./run.sh /app/

# Allow installing dev dependencies to run tests
ARG INSTALL_DEV=true

RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --no-dev ; fi"

COPY . /app
RUN chmod +x run.sh

ENV PYTHONPATH=/app

# chown all the files to the app user
RUN chown -R app:app $HOME

# Insall NLTK Data
# https://www.nltk.org/data.html
RUN python -m nltk.downloader -d /usr/local/share/nltk_data punkt

# change to the app user
# Switch to a non-root user, which is recommended by Heroku.
USER app

# Run the run script, it will check for an /app/prestart.sh script (e.g. for migrations)
# And then will start Uvicorn
CMD ["./run.sh"]
