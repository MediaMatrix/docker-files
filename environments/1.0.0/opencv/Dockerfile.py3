FROM datmo/dl-deps:cpu-py35

MAINTAINER Datmo devs <dev@datmo.com>

ARG OPENCV_VERSION=3.2.0

RUN cd ~/ && \
    git clone https://github.com/Itseez/opencv.git --branch ${OPENCV_VERSION} --single-branch && \
    git clone https://github.com/Itseez/opencv_contrib.git --branch ${OPENCV_VERSION} --single-branch && \
    cd opencv && \
    mkdir build && \
    cd build && \
    cmake -D CMAKE_BUILD_TYPE=RELEASE \
        -DWITH_QT=ON \
        -DWITH_OPENGL=ON \
        -D ENABLE_FAST_MATH=1 \
        -DFORCE_VTK=ON \
        -DWITH_TBB=ON \
        -DWITH_GDAL=ON \
        -DWITH_XINE=ON \
        -DBUILD_EXAMPLES=ON \
        -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
        .. && \
    make -j"$(nproc)" && \
    make install && \
    ldconfig && \
 # Remove the opencv folders to reduce image size
    rm -rf ~/opencv*