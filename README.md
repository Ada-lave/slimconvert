# Slimconvert

Simple app for converting docx document to pdf file.

## Quick start

For quick start you can run docker container using this sh command:

```sh
docker build -t slimconvert:latest .
docker run -p 8000:8000 --rm -d --name slimconvert slimconvert
```

> --rm and -d is optional args, and also you can change your port {port}:8000

Now you can send a docx file to localhost:8000 using form-data. The field with the name `file` your document.

Example cURL:

```sh
curl --location 'localhost:8000/convert-docx' \
--form 'file=@"/home/user1/downloads/example.docx"'
```

## Configuring

You can limit the maximum size of the input file in MB by using the `MAX_FILE_SIZE` environment variable.

Example:

```sh
docker run -p 8000:8000 -e MAX_FILE_SIZE=100 --name slimconvert slimconvert
```
