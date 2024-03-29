## Backend Repository of Jingil Integrated Management


### About JIM

[Notion](https://melon-form-217.notion.site/6eda48f52f87451f86efbd7434730b80)

### Tech Stack

[Notion](https://melon-form-217.notion.site/Tech-Stack-f9992555ea9344b99f16a95351fea0fb)

### API Documentation

[Notion](https://melon-form-217.notion.site/API-Docs-2d250934d308441ab740c9029b993613)

### Licensing

Licensed under [Apache 2.0 License](https://github.com/Jingil-Integrated-Management/JIM_backend/blob/master/License.md).

### Local Usage

``` Shell
# Execute at root directory
# ex) /Users/therealjamesjung/JIM

# If you dont have pipenv installed
$ pip install pipenv

# Install required packages
$ pipenv install
# Enable virtual environment
$ pipenv shell

$ sh scripts/clear_db.sh # clear existing db.sqlite
$ sh scripts/migrate.sh # migrate

# parse data from xlsx file
# NOTE) download data file to apps/Utils
$ sh scripts/parse.sh 

# Create superuser b.c. no signup process is available
$ python manage.py createsuperuser


$ python manage.py runserver

# Django version 3.2.8, using settings 'JIM.settings.dev_settings'
# Starting development server at http://127.0.0.1:8000/
# Quit the server with CONTROL-C.
```