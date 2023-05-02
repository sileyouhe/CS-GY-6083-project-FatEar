# CS-GY 6083 project FatEar

<!-- ABOUT THE PROJECT -->
## About The Project

FatEar is a web application where users can join the network and to review, recommend, and rate music. Users can also “friend” and “follow” other users, which allows them to share reviews and recommendations with others.

### Built With
Built Using Languages and Libraries Listed Below 
* Python
* Flask
* PyMySQL
* bcrypt




<!-- GETTING STARTED -->
## Getting Started

### Installation

1. Clone the repository
```sh
git clone https://github.com/sileyouhe/CS-GY-6083-project-FatEar.git
```
2. Installing Python Packages From a Requirements File
```python
pip install -r requirements.txt 
```
3. Import data from fatear.sql 

4. database configuration
```python
# config.py 
# default database configuration
SECRET_KEY = "secret key"
HOST = 'localhost'
PORT = 3306
USERNAME = "root"
PASSWORD = "root"
DBNAME = 'fatear'
CHARSET = 'utf8mb4'
CURSORCLASS = pymysql.cursors.DictCursor

```

5. Run flask app using command:
```shell 
$ flask --app app.py run
```

<!-- Authors -->

## Author
Kaiyu Pei



<!-- CONTACT -->

[//]: # (## Contact Me)
