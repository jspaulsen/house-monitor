# House Monitor Sub
Subscribes to MQTT and publishes to Timescale database

## Running locally
### Dependencies
#### Ubuntu

```
sudo apt-get install libpq-dev
```

## Testing

### Running against local database

## Releasing
```
docker buildx create --platform linux/amd64,linux/arm64,linux/arm/v7 --use
docker run --privileged --rm tonistiigi/binfmt --install all
```
