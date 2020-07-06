FROM python:3.8.3-slim

WORKDIR /dockerapp
COPY requirements_tests.txt ./
RUN pip install -r requirements_tests.txt
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . ./
RUN chmod +x ./runtests.py

ARG BUKDJANGO_CAPTCHA_RECAPTCHA_V3_SITE
ARG BUKDJANGO_CAPTCHA_RECAPTCHA_V3_SECRET
ARG BUKDJANGO_CAPTCHA_RECAPTCHA_V3_SCORE

ENV BUKDJANGO_CAPTCHA_RECAPTCHA_V3_SITE=$BUKDJANGO_CAPTCHA_RECAPTCHA_V3_SITE
ENV BUKDJANGO_CAPTCHA_RECAPTCHA_V3_SECRET=$BUKDJANGO_CAPTCHA_RECAPTCHA_V3_SECRET
ENV BUKDJANGO_CAPTCHA_RECAPTCHA_V3_SCORE=$BUKDJANGO_CAPTCHA_RECAPTCHA_V3_SCORE
