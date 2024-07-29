## Project description
Script Python to upload files from a local directory into a AWS S3 bucket (Supabase provided).

## Requirements
* Pyenv
* Poetry
* Supabase s3  bucket credentials

## How to run this project

1. Clone this repository locally:

```bash
git clone https://github.com/lamorasjr/load-to-supabase-s3.git
cd oad-to-supabase-s3.git
```

2. Install and setup the required Python version with `pyenv`:

```bash
pyenv install 3.12.4
pyenv local 3.12.4
```

3. Setup poetry to use the required Python version and activate the virtual enviroment:

```bash
poetry env use 3.12.3
poetry shell
```

4. Instal the project depencencies:

```bash
poetry install
```

5. Create a directory in the main folder named `data` containing the files to be uploaded to the s3 bucket
```bash
mkdir data
```

6. Create the `.env` file as per `.env example` and update the Supabase s3 variables.


