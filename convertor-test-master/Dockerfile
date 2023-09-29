# lambda base image for Docker from AWS
FROM public.ecr.aws/lambda/python:latest
# copy all code and lambda handler
RUN yum -y install curl wget tar gzip zlib freetype-devel \
    libxslt \
    libxslt1-dev \
    gcc \
    ghostscript \
    lcms2-devel \
    libffi-devel \
    libimagequant-devel \
    libjpeg-devel \
    libraqm-devel \
    libtiff-devel \
    libwebp-devel \
    make \
    openjpeg2-devel \
    rh-python36 \
    rh-python36-python-virtualenv \
    sudo \
    tcl-devel \
    tk-devel \
    tkinter \
    which \
    xorg-x11-server-Xvfb \
    zlib-devel \
    java \
    && yum clean all

RUN wget http://download.documentfoundation.org/libreoffice/stable/7.6.2/rpm/x86_64/LibreOffice_7.6.2_Linux_x86-64_rpm.tar.gz 
RUN tar -xvzf LibreOffice_7.6.2_Linux_x86-64_rpm.tar.gz
RUN cd LibreOffice_7.6.2.2_Linux_x86-64_rpm/RPMS; yum -y localinstall *.rpm;
RUN yum -y install cairo
RUN echo $(ls /opt/)
RUN echo $(ls /usr/bin)

COPY lambda_handler.py ./
COPY requirements.txt ./
# install packages
RUN yum install -y gcc-c++ pkgconfig poppler-cpp-devel
RUN python3 -m pip install -r requirements.txt
# run lambda handler
CMD ["lambda_handler.lambda_handler"]