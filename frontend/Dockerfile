# Use an official Node.js runtime as a parent image
FROM node:20-alpine

# Set the working directory in the container
WORKDIR /frontend

# Copy the current directory contents into the container at /frontend
COPY . /frontend/

# Install dependencies
RUN npm install

# Expose port
EXPOSE 3000

# Run the React app
CMD ["npm", "start"]
