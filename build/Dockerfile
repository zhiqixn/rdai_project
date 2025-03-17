FROM pytorch/pytorch:2.0.1-cuda11.7-cudnn8-runtime

# Installing python packages
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y 

COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /rdai_project

EXPOSE 8001

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8001"]