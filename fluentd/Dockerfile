FROM fluent/fluentd:v1.17.1-1.0
# Use root account to use apk
USER root

# below RUN includes plugin as examples elasticsearch is not required
# you may customize including plugins as you wish
RUN apk add --no-cache --update --virtual .build-deps \
        sudo build-base ruby-dev \
&& sudo gem install fluent-plugin-prometheus \
&& sudo gem install fluent-plugin-opensearch \
&& sudo gem install fluent-plugin-beats \
&& sudo gem sources --clear-all \
&& apk del .build-deps \
&& rm -rf /tmp/* /var/tmp/* /usr/lib/ruby/gems/*/cache/*.gem

# COPY fluent.conf /fluentd/etc/
# COPY entrypoint.sh /bin/

# USER fluent
