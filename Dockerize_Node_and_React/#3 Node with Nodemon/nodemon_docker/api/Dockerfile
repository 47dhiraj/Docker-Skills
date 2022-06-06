FROM node:17-alpine

# nodemon vanni node package install gareko to reflect the changes on code by automatically restarting the server
RUN npm install -g nodemon 
# install nodemon package globally

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

EXPOSE 4000
# required for docker desktop port mapping

CMD ["npm", "run", "dev"]
# npm run dev vannale npm run nodemon -L app.js ho (i.e dev chai pacakage.json file ma cha)