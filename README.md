# Zé Delivery Backend Challenge

## Setting up docker environment:

**Requirements:**
```docker``` and ```docker-compose```

```docker
docker-compose up -d
```

### Local API URL:

``` 
http://localhost:8000
```

### Endpoints:

- **Get All Partners**
``` 
    Endpoint: /partner/
    method: GET
    Example: http://localhost:8000/partner
```

- **Get Partner by id**
``` 
    Endpoint: /partner/{id}
    method: GET
    Example: http://localhost:8000/partner/1
```

- **Get near Partners from location**
``` 
    Endpoint: /partner?lat={lat}&lng{lng}
    method: GET
    params: lat, lng
    Example: http://localhost:8000/partner?lat=-23.5298466&lng=-22.768366
```

- **Create Partner**
``` 
    Endpoint: /partner
    method: POST
    params: body bellow
    Example: http://localhost:8000/partner
```
- Body
```json
{
    "id": "51",
    "tradingName": "Adega do Joao",
    "ownerName": "Pele Maradona",
    "document": "960361.506-44",
    "coverageArea": {
        "type": "MultiPolygon",
        "coordinates": [
            [
                [
                    [
                        -44.04912,
                        -19.87743
                    ],
                    [
                        -44.0493,
                        -19.89438
                    ],
                    [
                        -44.04758,
                        -19.90212
                    ],
                    [
                        -44.04346,
                        -19.90922
                    ],
                    [
                        -44.03385,
                        -19.91923
                    ],
                    [
                        -44.01891,
                        -19.92165
                    ],
                    [
                        -44.01647,
                        -19.92306
                    ],
                    [
                        -44.01436,
                        -19.92319
                    ],
                    [
                        -44.01175,
                        -19.92427
                    ],
                    [
                        -44.00724,
                        -19.92585
                    ],
                    [
                        -43.99909,
                        -19.9185
                    ],
                    [
                        -43.99432,
                        -19.91403
                    ],
                    [
                        -43.99557,
                        -19.90842
                    ],
                    [
                        -43.99582,
                        -19.90285
                    ],
                    [
                        -43.99436,
                        -19.89002
                    ],
                    [
                        -43.99316,
                        -19.8792
                    ],
                    [
                        -43.99436,
                        -19.87371
                    ],
                    [
                        -43.99951,
                        -19.86532
                    ],
                    [
                        -44.01917,
                        -19.85135
                    ],
                    [
                        -44.02801,
                        -19.8545
                    ],
                    [
                        -44.03745,
                        -19.85668
                    ],
                    [
                        -44.04397,
                        -19.8608
                    ],
                    [
                        -44.04912,
                        -19.87743
                    ]
                ]
            ]
        ]
    },
    "address": {
        "type": "Point",
        "coordinates": [
            -44.012478,
            -19.887215
        ]
    }
}
```

###Postman Collection:
[ze delivery backend challenge.postman_collection.json.zip](https://drive.google.com/open?id=1vAzQ-HxMz3eUzZByyH8rtxfHENxvf3Wv)

###Running tests:

```shell script
docker exec -it ze-delivery-backend-challenge_web_1 python manage.py test 
```

###Creating Django Admin Superuser(if you need that...)

```shell script
docker exec -it ze-delivery-backend-challenge_web_1 python manage.py createsuperuser 
```

## Deployment:

**Requirements**: ```Python 3.7``` , ```Pip``` and ```Configurated webserver```.

**After you have sent the changes to the server, go to the project folder and run the following commands:**
- Install the project requirements:
```shell script
    pip install -r requirements.txt
```
- Apply the Django migrations
```shell script
    python manage.py migrate 
```
