FROM node:18-alpine AS base
WORKDIR /app

FROM base AS dev
WORKDIR /app
COPY package.json package-lock.json ./
RUN --mount=type=cache,target=/app/.npm \
    npm set cache /app/.npm && \
    npm install
COPY . .
CMD ["npm", "run", "dev"]

FROM base AS prod-build
WORKDIR /app
COPY package.json package-lock.json ./
RUN --mount=type=cache,target=/app/.npm \
    npm set cache /app/.npm && \
    npm ci
COPY . .
RUN npm run build

FROM nginxinc/nginx-unprivileged:1.22-alpine AS prod
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=prod-build /app/dist /usr/share/nginx/html
EXPOSE 8080
CMD ["nginx", "-g", "daemon off;"]
