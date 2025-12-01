# --- Build Stage ---
FROM node:20-slim AS builder

WORKDIR /app
COPY package*.json ./
RUN npm install

# Make sure Vite sees your backend API URL
COPY .env .env

COPY . .
RUN npm run build

# --- Production Stage ---
FROM nginx:alpine

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /app/dist /usr/share/nginx/html

EXPOSE 80

