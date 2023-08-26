# qr-code-rw

Read QR codes from and write QR codes to PNG images.

## Usage

Build docker image:

```sh
docker build --tag qr-code-rw:latest .
```

Read QR code:

```sh
docker run --rm --interactive qr-code-rw:latest read < ./some_image.png
```

Write QR code:

```sh
docker run --rm qr-code-rw:latest write "some_data" > ./some_image.png
```
