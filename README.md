## Detener todos los contenedores en ejecucion 
```bash
docker stop $(docker ps -q)
```


## Eliminar todos los contenedores en ejecucion
```bash
docker rm $(docker ps -a -q)
```


## Eliminar todas las imágenes (incluso las que están en uso)
```bash
docker rmi $(docker images -q)
```

## Levantar contedores
```bash
docker compose up --build
```

## Bajar contenedores

```bash
docker compose down
```



## Acceder a phpmyAdmin
``` bash
http://localhost:8080/
```


## Acceder a la base de datos
```
"host": "localhost"
"port": 4208,  
"user": "administrador",
"password": "1234",
"database": "base_de_datos"
```