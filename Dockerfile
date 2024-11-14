ARG BASEIMAGE_TAG='21-bookworm-slim'
FROM "node:${BASEIMAGE_TAG}"

RUN set -ex \
  mkdir -p /var/www/data

WORKDIR /var/www

COPY /3dwebclient ./3dwebclient
COPY /js ./js
COPY /theme ./theme
COPY /ThirdParty ./ThirdParty
COPY /docker/package.json /docker/server.js /docker/html/ ./

RUN set -ex && \
  npm install --omit=dev && \
  npm cache clean --force && \
  chown -R node:node .

USER node
EXPOSE 8000
CMD [ "node", "server.js", "--public"]
