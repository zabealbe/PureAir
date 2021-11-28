# Pure Air

Air quality monitoring system.

Pure Air stack is designed to be horizontally scalable through [kubernetes](http://kubernetes.io), both Frontend and
Backend are stateless and designed as a microservice that can be run in a container.

## Getting started

Run our web stack with:

```bash
docker-compose up
```

Once everything started up you can start sending data with your Pure Air IOT device, check out [Hardware](Hardware) for
the source code.

## Frontend

Composed of a Private area and a [Private area](Frontend/user.html) and a [Public area](Frontend/index.html).

| Private area                        | Public area                       |
| ----------------------------------- | --------------------------------- |
| ![Private area](docs/f_private.png) | ![Public area](docs/f_public.png) |

The private area empowers the user by giving him useful insights to make educated decisions, such as suggestsing
the house ventilation schedule by fetching sensor data from the [Pure Air APIs](Backend).

The public area empowers the people by giving everyone a powerful tool to monitor the city pollution. This data can be
used by the authorities to improve the well being of citizens or can be used by citizens themselves to force authorities to take action.

## Backend

Based on [Swagger](https://swagger.io/) and [OpenAPI](https://swagger.io/specification/) and though to be scalable through container-based replication systems such as [kubernetes](https://kubernetes.io).

- Three private APIs endpoints for the user private area

- Public API endpoint `http://[BACKEND_URL]/v1/getPollutionInfo` for third parties to build upon,
  easing the integration process by using the standard format [GeoJSON](https://geojson.org/)

![Backend](docs/b.png)

## Database

MongoDB is our database, flexible enough and optimized for our needs is able to manage well
GeoJSON data with its [2dsphere geospatial index](https://docs.mongodb.com/manual/core/2dsphere/)

For testing purposes we created a [populator](Database/populate/populate.py) script to create, fill and index the
database.

## Home assistant

We empower the user by providing home assist integration that can be used in conjunction within a smart home in a
domotic environment.

![Backend](Hassio/images/home.png)

## Hardware

The board used for the project is a nodemcu with an esp32 microcontroller.

![Temperature sensor](Hardware/images/nodemcu.jpg)

The following sensors are used to obtain the reads:

- Two ds18b20 for indoor and outdoor temperature measurements

  ![Temperature sensor](Hardware/images/temp_sensor.jpg)

- A MQ-135 sensor for indoor CO2 measurement

  ![Temperature sensor](Hardware/images/co2_sensor.jpg)

- A Grove Dust Sensor(PPD42NS) for outdoor pollution levels

  ![Temperature sensor](Hardware/images/pollution_sensor.jpg)

To communicate between the internal and external modules, a normal RJ11 cable can be used,
with the following setup:

- Red wire -> 5v
- Black wire -> GND
- Yellow wire -> Temperature sensor one wire bus
- Green wire -> LO-time dust sensor signal

Here it is the final prototype:

![Prototype](Hardware/images/prototype.jpg)

## License

[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)
Copyright &copy; PureAir team
