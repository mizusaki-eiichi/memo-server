FROM postgres:10
ARG DB_LANG=en_US
RUN localedef -i $DB_LANG -c -f UTF-8 -A /usr/share/locale/locale.alias $DB_LANG.UTF-8
ENV LANG $DB_LANG.utf8
RUN apt-get update && apt-get install -y --no-install-recommends \
    bc \
    && apt-get -y clean && rm -rf /var/lib/apt/lists/*
ENV TZ Asia/Tokyo