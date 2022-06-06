# Docker hub batw node version 17 lai download gar & linux distro chai alpine use gar vaneko
FROM node:17-alpine

# nodemon use garna ko lagi nodemon lai globally install gareko
RUN npm install -g nodemon

WORKDIR /app

# computer directory ko package.json lai copy garera container ko app or WORKDIR ma lagera rakheko
COPY package.json .

# container ma sabai npm pacakages or dependecies haru lai install gareko
RUN npm install

# local computer ma vayeko sabai source code files haru lai container ma copy garera rakheko
COPY . .

EXPOSE 4000
# required for docker desktop port mapping

# npm run dev vanni command execute gareko (i.e dev vanni command chai package.json file ma cha)
CMD ["npm", "run", "dev"]

