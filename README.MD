# Simple Blog App

## Standard deployment
1. Clone the repo.
2. Ensure that docker is installed on your system. 
3. Create .env file in with keys: POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB. 
4. 
	```bash
	docker-compose up --build
	```
5. App will be deployed momenteraly on localhost:8000 by default

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

## Usage
Once succesfully deployed, you can interact with the application via simple GET/POST requests.
To show all posts:
```bash
curl -X GET yourhostname:8000/posts
```
To make a new one:
```
curl -X POST yourhostname:8000/posts \
  -H "Content-Type: application/json" \
  -d '{"title": "Another post", "content": "Some content here"}'
```

## Example .env file(.env should be placed in the root of the application(alongside with README.MD)
```
POSTGRES_USER=admin
POSTGRES_PASSWORD=123
POSTGRES_DB=test
```
