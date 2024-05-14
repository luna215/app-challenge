
## Run Locally
You will need to have docker installed and then just run at the root of the project
```
docker-compose up --build
```

Frontend should be running on `localhost:3000`
Backend should be running on `localhost:8000`

### Extra Thoughts Here
- This is a light weight full stack application, and I am aware that there a ton of areas that we can improve on (i.e. authentication, row level security, better validation,..), but this is typically how I would structure either frontend or backend projects
- Also, I typically have more folders but I usually start off with a file and if a feature/component starts to get a lot more intricate, then I start to move it into a separapte folder or file.
- Within `backend/` and `frontend/` I added an empty folder `terraform`. Typically when I create new projects, I have this in there to make sure I create the infrarstructure with terraform so we can easily do deployments to either staging or production, it saves a ton of time.


## Tech Stack
- Backend: FastAPI (Python) & Postgresql
- Frontend: React, Typescript, and Chackra UI

# Takehome Assessment
Pigeon takehome assessment for eng candidates.

## Project Statement
At Pigeon we do a lot of work with documents including uploading, downloading, and displaying. This project will be a simplified version of that system. I would like you to build a fullstack application for storing, creating, viewing, and downloading very simple "documents".

## Requirements
1. Create a database to store documents, where each document model has ONLY the following data. You do not need to deal with uploading, downloading, or storing actual files unless you really want to.
    * Title: string
    * Author: string
2. Create a UI with the following:
    * Form to add a new document to the database
        * If a new document is added with the same name as an existing document, the existing record's author should be updated to the new author
    * List of all document data
    * Button to download list of all document data (format is up to you; txt, csv, etc are all fine)

## Additional Specs
1. Opt for simple and efficient development choices as much as you can. If your code is overly complicated I will be very reluctant to review it.
2. The design of the UI is not a focus of this project, I recommend going for as simple as possible.
3. Use whatever technologies and frameworks you are most comfortable with, you're not required to use anything from our stack.
5. You are not required to finish the entire assessment, **please spend at most 3hrs on it**. I'm looking for insight into how you think about and build a system, not a perfect product. Start with what you're strongest with (db, api, ui, etc), and if you have extra time build out the rest of the application.
