// install docker, docker desktop and docker-compose
// make sure docker engine is running

// run command to pull image 
command: docker pull mudassirali89/studentinsight:1.0

// run command to start sql and django containers
command: docker-compose up --build -d

// check running containers mysql and django_container
command: docker ps

// run command to migrate changes from django containers to your sql database
command: docker exec -it django_container python predicting_at_risk_students/manage.py migrate     

// if you recieve error like column name already exists or table name already exists run command below to fake that migration. Increase the number for every error.(like 0003 to 0004 and so on...)
command: docker exec -it django_container python predicting_at_risk_students/manage.py migrate Remote_User 0003 --fake

// open localhost:8000 app 

// run command below to stop containers
command: docker-compose down


