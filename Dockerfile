# lambda base image for Docker from AWS 
FROM public.ecr.aws/lambda/python:latest
# copy all code and lambda handler
RUN yum -y install curl wget tar gzip zlib \
    libdbusmenu.x86_64 \
    libdbusmenu-gtk2.x86_64 \
    libSM.x86_64 \
    xorg-x11-fonts-* \
    google-noto-sans-cjk-fonts.noarch \
    binutils.x86_64 \
    java-1.8.0-openjdk-devel \
    -y && \
    yum clean all

RUN wget https://ftp.halifax.rwth-aachen.de/tdf/libreoffice/stable/7.5.6/rpm/x86_64/LibreOffice_7.5.6_Linux_x86-64_rpm.tar.gz
RUN tar -xvzf LibreOffice_7.5.6_Linux_x86-64_rpm.tar.gz
RUN echo $(ls)
RUN cd LibreOffice_7.5.6.2_Linux_x86-64_rpm/RPMS && \
    yum -y localinstall *.rpm && \
    yum install cairo -y && \
    rm -rf /var/task/LibreOffice_7.5.6* && \
    cd /opt/libreoffice7.5/ && \
    strip ./*/ || true

ENV HOME=/tmp

COPY lambda_handler.py ./
COPY requirements.txt ./
# install packages
RUN python3 -m pip install -r requirements.txt
# run lambda handler
CMD ["lambda_handler.lambda_handler"]
