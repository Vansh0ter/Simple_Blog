# Simple Blog App

## Standart deployment
1. Clone the repo.
2. Ensure that docker is installed on your system.
3. Intialize PgSQL DB. 
4. Create .env file in with keys: POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB. 
5. ```bash
	docker-compose up --build
	```
6. App will be deployed momenteraly on localhost:8000 by default

## Docker-less deployment
1. Clone the repo
2. Create .env file in root with keys: POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB.
3. Create python venv with 
```bash
pytnon3 -m venv venv
```
4. Activate venv with 
```bash
source venv/bin/activate
```
5. Install dependecies 
```bash
pip install --no-cache-dir -r app/requirements.txt
```
6. Run the application with 
```bash
uvicorn app.main:app --reload --log-config=logs/log_config.json
```

## Example .env file
```
POSTGRES_USER=admin
POSTGRES_PASSWORD=123
POSTGRES_DB=test
```
