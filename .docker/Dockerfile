FROM python:3.9

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN apt-get update && apt-get install -y \
  git \
  zlib1g-dev \
  unixodbc \
  unixodbc-dev \
  freetds-dev \
  freetds-bin \
  tdsodbc \
  libicu-dev\
  wget

# Instalação de bibliotecas
RUN pip --no-cache-dir install -r requirements.txt

# Adicionar o /app no PYTHONPATH pra ele encontrar a pasta "src"
ENV PYTHONPATH="${PYTHONPATH}:/app"

CMD python /app/src/app.py