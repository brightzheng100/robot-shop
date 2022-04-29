FROM ubuntu:20.04

# The URL of Robot Shop
ENV HOST="http://web:8080"

# Install Chromium and Chrome WebDriver
RUN \
    apt-get update && \
    apt-get install -y wget curl unzip gnupg2 python3 python3-distutils python3-pip && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    \
    python -m pip install --upgrade --no-cache-dir selenium selenium-wire && \
    \
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y google-chrome-stable && \
    \
    CHROMEDRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE` && \
    mkdir -p /opt/chromedriver-$CHROMEDRIVER_VERSION && \
    curl -sS -o /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip && \
    unzip -qq /tmp/chromedriver.zip -d /opt/chromedriver-$CHROMEDRIVER_VERSION && \
    chmod +x /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver && \
    ln -fs /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver /usr/local/bin/chromedriver && \
    \
    apt-get remove -y wget unzip && \
    rm /tmp/chromedriver.zip && \
    rm -rf /var/lib/apt/lists/*

RUN useradd -m loader
USER loader

WORKDIR /load

COPY --chown=loader:loader entrypoint.sh .
COPY --chown=loader:loader load.py .

ENTRYPOINT ["./entrypoint.sh"]
