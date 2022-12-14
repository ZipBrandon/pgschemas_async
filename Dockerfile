FROM python:3.10-bullseye as python_packages
MAINTAINER blorenz@gmail.com
RUN mkdir /svc
WORKDIR /svc
COPY requirements/requirements.txt .
RUN pip wheel -r requirements.txt --wheel-dir=/svc/wheels

FROM python:3.10-bullseye

COPY --from=python_packages /svc /svc
WORKDIR /svc
RUN sed -i 's/git\+.*\.git #//g' requirements.txt
RUN pip install --no-index --find-links=/svc/wheels -r requirements.txt
RUN mkdir -p /home/docker/code/app
RUN mkdir -p /home/docker/volatile/static
RUN mkdir -p /home/docker/persistent/media

WORKDIR /home/docker/code/app

EXPOSE 8010

CMD ["/bin/bash"]
