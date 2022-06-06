# React app lai build garna pani node image download garna parcha    # alpine is linux lightweight distro
FROM node:16-alpine             

WORKDIR /app

# copy package.json to container WORKDIR (i.e /app)
COPY package.json .

# install all the pacakage dependecies
RUN npm install

# copy all source files in computer to the container WORKDIR(i.e /app)
COPY . .

# React app default ma port no: 3000 ma run huncha so tei vayera 3000 ma EXPOSE gareko
EXPOSE 3000
# required for docker desktop port mapping

# Yo command le container ma vayeko react app or project lai run garaucha(i.e npm start or npm run start)
CMD ["npm", "start"]
