# Pytest API Automatic

Pytest Framework For API Automation Testing

## Table of contents
* [General Info](#General info)
* [Installation](#Installation)
* [Built with](#Built with)
* [Architecture](#Architecture)
  * [testcases](#testcases)
  * [apiobjects](#apiobjects)
  * [config](#config)
  * [resource](#resource)
  * [core](#core)
  * [utils](#utils)
  * [models](#models)
  * [suites](#suites)
* [Run test with](#run-test-with)
* [Help](#help)

## General info
Library with a bunch of useful functions that extend Pytest and make your api testing better.

## Installation

### Install manually
Add dependency with a version that you need
```shell
pip install -r requirement.txt
```

## Built with
* pytest version: 6.2.3
* httpx version: 0.17+



## Architecture

### config
The only class the you need from this module is `SimulationConfig`. It could be used to attach some default variables such as `baseUrl`, `baseAuthUrl`,`testDuration`, `userCount` and some others to your scripts. Also it provides functions to get custom variables fom config.

Import:
```scala
import hccn.qe.gatling.config.SimulationConfig._
```

Using default variables:

```scala
import hccn.qe.gatling.config.SimulationConfig._

val testPlan: Seq[OpenInjectionStep] = List(
    rampUsersPerSec(0).to(userCount).during(rampDuration),
    constantUsersPerSec(userCount).during(testDuration)
)
```

Using functions to get custom variable:

*simulation.conf*
```
stringVariable: "FOO",
intVariable: 1,
doubleVariable: 3.1415,
duration: {
    durationVariable: 3600s
}
```
```scala
import hccn.qe.gatling.config.SimulationConfig._

val stringVariable      = getStringParam("stringVariable")
val intVariable         = getIntParam("intVariable")
val doubleVariable      = getDoubleParam("doubleVariable")
val durationVariable    = getDurationParam("duration.durationVariable")

```

### feeders
This module contains vast number of random feeders. They could be used as regular feeders and realize common needs, i.e random phone number or random digit. Now it supports feeders for dates, numbers and digits, strings, uuids, phones.
There we'll provide some examples, other feeders can be used same way. Now it supports feeders for dates, digits, strings, uuids, phones.

```scala
import hccn.qe.gatling.feeders._

//creates feeder with name 'randomString' that gets random string of length 10
val stringFeeder = RandomStringFeeder("randomString", 10)

//creates feeder with name 'digit' that gets random Int digit
val digitFeeder = RandomDigitFeeder("digit")

//creates feeder with name 'uuid' that gets random uuid
val uuidFeeder = RandomUUIDFeeder("uuid")

//creates feeder with name 'id' that gets id seq
val idFeeder: Feeder[Int] = IdFeeder("id")

```

### loadmodel
This module could be used as load model for common needs, include `Baseline`,`Benchmark`
`Load`,`Stress` stage
```scala
import hccn.qe.gatling.loadmodels._

baseline(mockScenario("Baseline Test")).andThen(
  benchmark_closed(mockScenario("Benchmark Test"),userCount,rampDuration,testDuration).andThen(
    load_closed(mockScenario("Load Test"), userCount,increment,times,testDuration).andThen(
      stress_open(mockScenario("Stress Test"), userRate, 5.minutes,500)
    )
  )
)
```

### amqp
Plugin for support performance testing with AMQP in Gatling(3.4.x) and Scala(2.12.12)

Dependency: ```gatlingImplementation "com.rabbitmq:amqp-client:5.11.0"```

```scala
import hccn.qe.gatling.amqp.Predef._
import hccn.qe.gatling.amqp.protocol.AmqpProtocolBuilder

val amqpConf: AmqpProtocolBuilder = amqp
        .connectionFactory(
          rabbitmq
                  .host("localhost")
                  .port(5672)
                  .username("guest")
                  .password("guest")
                  .vhost("/")
        )
        .usePersistentDeliveryMode

val scn: ScenarioBuilder = scenario("AMQP test")
        .exec(
          amqp("publish to exchange").publish
                  .topicExchange("test_q_in","performance")
                  .textMessage("Hello message")
                  .priority(0)
                  .contentType("application/json")
                  .headers("test"-> "performance")
        )

```

### kafka
Plugin for support performance testing with Kafka(MQTT) in Gatling(3.4.x) and Scala(2.12.12)

Dependency: 
```groovy
gatlingImplementation("org.apache.kafka:kafka-clients:2.7.0") {
exclude group: "org.slf4j", module: "slf4j-api"
}
```

Usage:
```scala
import org.apache.kafka.clients.producer.ProducerConfig
import hccn.qe.gatling.kafka.Predef._
import hccn.qe.gatling.kafka.protocol.KafkaProtocol

val kafkaConf: KafkaProtocol = kafka
        // Kafka topic name
        .topic("test")
        // Kafka producer configs
        .properties(
          Map(
            ProducerConfig.ACKS_CONFIG -> "1",
            // list of Kafka broker hostname and port pairs
            ProducerConfig.BOOTSTRAP_SERVERS_CONFIG -> "localhost:9092",

            // in most cases, StringSerializer or ByteArraySerializer
            ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG ->
                    "org.apache.kafka.common.serialization.StringSerializer",
            ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG ->
                    "org.apache.kafka.common.serialization.StringSerializer"))

val scn: ScenarioBuilder = scenario("Kafka Test")
        .exec(
          kafka("request")
                  // message to send
                  .send[String]("gatling kafka test"))
```
Note:
Also support ByteArray Message

## Build
To build use `gradle clean build`
## Testing
To test your changes use `gradle clean gatling-lib-toolbox:scalatest`.



## Help

mail: moyu6027@gmail.com

pytest docs: https://docs.pytest.org/en/stable/index.html