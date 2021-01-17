# link_shortener2

Link Shortener Service for the [LSESU Data Science Society](https://dsatlse.githu.bio)

## Architecture

![](LinkShortener.png)


## Methods

GET `/{shorturl}}`

Redirects the user to the long url

POST `/addToDB?{data}`

Adds a link to the database by calling an AWS Lambda function to add to S3 Bucket

DELETE `/removeFromDB/{shorturl}`

Queries the database removing it (or setting active = FALSE) if the shorturl is found

POST `/update/{shorturl}`

Updates the entry with new data



## Database Schema

| ID  | shorturl | longurl | active|
| --  | -- | -- | -- |
| 0 | home | https:/dsatlse.github.io | TRUE |


