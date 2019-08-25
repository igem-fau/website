# Web Brick 

## Status

 - [X] Static pages: main page, everything at project, human practices + awards
 - [X] Team members: members page, collaborations + attributions
 - [ ] Parts: Parts overview, basic parts, composite parts and parts collection
 - [ ] Lab Journal

## Deploying

This set comes equipped with a script to deploy the static pages to the iGEM wiki of your team.
For this you have to set the environment variables `IGEM_TEAM`, `IGEM_USERNAME` and `IGEM_PASSWORD`
with your team name (the one you registered with iGEM) and your credentials for login. Then
once you type in your terminal `make deploy`, a Python script is executed that

 - generates the static pages if necessary
 - locates all the assets (images, stylesheets, javascript files, etc.) and uploads them
   to the iGEM website
 - updates the asset locations in the HTML files to the uploaded filenames
 - uploads the static files to the correct Wiki pages

This aims to simplify the whole website creation process significantly.