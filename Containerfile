FROM fedora:38

RUN dnf install -y \
    binutils \
    bison \
    diffutils \
    gcc \
    g++ \
    less \
    nano \
    patch \
    perl \
    python \
    rpm-build \
    texinfo \
    xz

RUN ln -s /usr/bin/bison /usr/bin/yacc

RUN groupadd lfs && \
    useradd -s /bin/bash -g lfs -m -k /dev/null lfs

COPY version-check.sh /bin/version-check.sh
COPY bashrc /home/lfs/.bashrc
COPY rpmmacros /home/lfs/.rpmmacros
COPY sudoers /etc/sudoers.d/lfs

WORKDIR /home/lfs
USER lfs

CMD [ "tail", "-f", "/dev/null" ]
