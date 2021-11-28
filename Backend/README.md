---
title: PureAir v1.0.0
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - ruby: Ruby
  - python: Python
  - php: PHP
  - java: Java
  - go: Go
toc_footers: []
includes: []
search: true
highlight_theme: darkula
headingLevel: 2

---

<h1 id="pureair">PureAir APIs v1.0.0</h1>
Built with <a href="https://swagger.io">swagger.io</a>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

Base URLs:

* <a href="http://[HOSTNAME]/v1">http://[HOSTNAME]/v1</a>

 License: Apache 2.0

<h1 id="pureair-iot">iot</h1>

## get_pollution_info

<a id="opIdget_pollution_info"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://[HOSTNAME]/v1/iot/getPollutionInfo \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST http://[HOSTNAME]/v1/iot/getPollutionInfo HTTP/1.1
Host: [hostname]
Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "lat": 46.6179554,
  "lng": 13.8247993,
  "range": 10000
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('http://[HOSTNAME]/v1/iot/getPollutionInfo',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post 'http://[HOSTNAME]/v1/iot/getPollutionInfo',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('http://[HOSTNAME]/v1/iot/getPollutionInfo', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','http://[HOSTNAME]/v1/iot/getPollutionInfo', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://[HOSTNAME]/v1/iot/getPollutionInfo");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://[HOSTNAME]/v1/iot/getPollutionInfo", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /iot/getPollutionInfo`

*Get pollution info on your zone*

> Body parameter

```json
{
  "lat": 46.6179554,
  "lng": 13.8247993,
  "range": 10000
}
```

<h3 id="get_pollution_info-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[GetPollutionInfoData](#schemagetpollutioninfodata)|true|none|

> Example responses

> 200 Response

```json
[
  {
    "lng": 13.8247993,
    "lat": 46.6179554
  }
]
```

<h3 id="get_pollution_info-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns pollution info for that zone and nearby places|Inline|

<h3 id="get_pollution_info-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[PollutionInfo](#schemapollutioninfo)]|false|none|none|
|» lat|number|false|none|Latitude|
|» lng|number|false|none|Longitude|
|» LPOTime|number|false|none|Longitude|

<aside class="success">
This operation does not require authentication
</aside>

## get_device_data

<a id="opIdget_device_data"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://[HOSTNAME]/v1/iot/getDeviceData/{UUID} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST http://[HOSTNAME]/v1/iot/getDeviceData/{UUID} HTTP/1.1
Host: [hostname]
Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "startDate": "YYYY-MM-DD HH:MM:SS",
  "endDate": "YYYY-MM-DD HH:MM:SS"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('http://[HOSTNAME]/v1/iot/getDeviceData/{UUID}',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post 'http://[HOSTNAME]/v1/iot/getDeviceData/{UUID}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('http://[HOSTNAME]/v1/iot/getDeviceData/{UUID}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','http://[HOSTNAME]/v1/iot/getDeviceData/{UUID}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://[HOSTNAME]/v1/iot/getDeviceData/{UUID}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://[HOSTNAME]/v1/iot/getDeviceData/{UUID}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /iot/getDeviceData/{UUID}`

*Get pollution info on your zone*

> Body parameter

```json
{
  "startDate": "YYYY-MM-DD HH:MM:SS",
  "endDate": "YYYY-MM-DD HH:MM:SS"
}
```

<h3 id="get_device_data-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|UUID|path|integer|true|UUID of the device|
|body|body|[DateRange](#schemadaterange)|true|none|

> Example responses

> 200 Response

```json
[
  {
    "lng": 13.8247993,
    "lat": 46.6179554
  }
]
```

<h3 id="get_device_data-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns pollution info for that zone and nearby places|Inline|

<h3 id="get_device_data-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[PollutionInfo](#schemapollutioninfo)]|false|none|none|
|» lat|number|false|none|Latitude|
|» lng|number|false|none|Longitude|
|» LPOTime|number|false|none|Longitude|

<aside class="success">
This operation does not require authentication
</aside>

## put_device_data

<a id="opIdput_device_data"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://[HOSTNAME]/v1/iot/putDeviceData/{UUID} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST http://[HOSTNAME]/v1/iot/putDeviceData/{UUID} HTTP/1.1
Host: [hostname]
Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "inTemp": 0,
  "outTemp": 0,
  "LPOTime": 0,
  "CO2": 0
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('http://[HOSTNAME]/v1/iot/putDeviceData/{UUID}',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post 'http://[HOSTNAME]/v1/iot/putDeviceData/{UUID}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('http://[HOSTNAME]/v1/iot/putDeviceData/{UUID}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','http://[HOSTNAME]/v1/iot/putDeviceData/{UUID}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://[HOSTNAME]/v1/iot/putDeviceData/{UUID}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://[HOSTNAME]/v1/iot/putDeviceData/{UUID}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /iot/putDeviceData/{UUID}`

*Update Pollution Info for a zone*

> Body parameter

```json
{
  "inTemp": 0,
  "outTemp": 0,
  "LPOTime": 0,
  "CO2": 0
}
```

<h3 id="put_device_data-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|UUID|path|integer|true|UUID of the device|
|body|body|[PollutionUploadData](#schemapollutionuploaddata)|true|none|

> Example responses

> 200 Response

```json
[
  {
    "lng": 13.8247993,
    "lat": 46.6179554
  }
]
```

<h3 id="put_device_data-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Invalid input|Inline|

<h3 id="put_device_data-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[PollutionInfo](#schemapollutioninfo)]|false|none|none|
|» lat|number|false|none|Latitude|
|» lng|number|false|none|Longitude|
|» LPOTime|number|false|none|Longitude|

<aside class="success">
This operation does not require authentication
</aside>

## update_device_position

<a id="opIdupdate_device_position"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://[HOSTNAME]/v1/iot/updateDevicePosition/{UUID} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST http://[HOSTNAME]/v1/iot/updateDevicePosition/{UUID} HTTP/1.1
Host: [hostname]
Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '[
  {
    "macAddress": "88:78:73:84:B9:C6",
    "strength": "-43",
    "SNR": "0",
    "channel": "11"
  }
]';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('http://[HOSTNAME]/v1/iot/updateDevicePosition/{UUID}',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post 'http://[HOSTNAME]/v1/iot/updateDevicePosition/{UUID}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('http://[HOSTNAME]/v1/iot/updateDevicePosition/{UUID}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','http://[HOSTNAME]/v1/iot/updateDevicePosition/{UUID}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://[HOSTNAME]/v1/iot/updateDevicePosition/{UUID}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "http://[HOSTNAME]/v1/iot/updateDevicePosition/{UUID}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /iot/updateDevicePosition/{UUID}`

*Update Pollution Info for a zone*

> Body parameter

```json
[
  {
    "macAddress": "88:78:73:84:B9:C6",
    "strength": "-43",
    "SNR": "0",
    "channel": "11"
  }
]
```

<h3 id="update_device_position-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|UUID|path|integer|true|UUID of the device|
|body|body|[WiFiList](#schemawifilist)|true|none|

> Example responses

> 200 Response

```json
[
  {
    "lng": 13.8247993,
    "lat": 46.6179554
  }
]
```

<h3 id="update_device_position-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Invalid input|Inline|

<h3 id="update_device_position-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[PollutionInfo](#schemapollutioninfo)]|false|none|none|
|» lat|number|false|none|Latitude|
|» lng|number|false|none|Longitude|
|» LPOTime|number|false|none|Longitude|

<aside class="success">
This operation does not require authentication
</aside>

## get_home_assistant

<a id="opIdget_home_assistant"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://[HOSTNAME]/v1/iot/getHomeAssistant/{UUID} \
  -H 'Accept: application/json'

```

```http
GET http://[HOSTNAME]/v1/iot/getHomeAssistant/{UUID} HTTP/1.1
Host: [hostname]
Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('http://[HOSTNAME]/v1/iot/getHomeAssistant/{UUID}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get 'http://[HOSTNAME]/v1/iot/getHomeAssistant/{UUID}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('http://[HOSTNAME]/v1/iot/getHomeAssistant/{UUID}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','http://[HOSTNAME]/v1/iot/getHomeAssistant/{UUID}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("http://[HOSTNAME]/v1/iot/getHomeAssistant/{UUID}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "http://[HOSTNAME]/v1/iot/getHomeAssistant/{UUID}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /iot/getHomeAssistant/{UUID}`

*Get pollution info endpoint for Home Assistant*

<h3 id="get_home_assistant-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|UUID|path|integer|true|UUID of the device|

> Example responses

> 200 Response

```json
50
```

<h3 id="get_home_assistant-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns latest pollution reading for that sensor|integer|

<aside class="success">
This operation does not require authentication
</aside>

# Schemas

<h2 id="tocS_PollutionInfo">PollutionInfo</h2>
<!-- backwards compatibility -->
<a id="schemapollutioninfo"></a>
<a id="schema_PollutionInfo"></a>
<a id="tocSpollutioninfo"></a>
<a id="tocspollutioninfo"></a>

```json
{
  "lng": 13.8247993,
  "lat": 46.6179554
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|lat|number|false|none|Latitude|
|lng|number|false|none|Longitude|
|LPOTime|number|false|none|Longitude|

<h2 id="tocS_PollutionUploadData">PollutionUploadData</h2>
<!-- backwards compatibility -->
<a id="schemapollutionuploaddata"></a>
<a id="schema_PollutionUploadData"></a>
<a id="tocSpollutionuploaddata"></a>
<a id="tocspollutionuploaddata"></a>

```json
{
  "inTemp": 0,
  "outTemp": 0,
  "LPOTime": 0,
  "CO2": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|inTemp|number|false|none|none|
|outTemp|number|false|none|none|
|LPOTime|number|false|none|none|
|CO2|number|false|none|none|

<h2 id="tocS_GetPollutionInfoData">GetPollutionInfoData</h2>
<!-- backwards compatibility -->
<a id="schemagetpollutioninfodata"></a>
<a id="schema_GetPollutionInfoData"></a>
<a id="tocSgetpollutioninfodata"></a>
<a id="tocsgetpollutioninfodata"></a>

```json
{
  "lat": 46.6179554,
  "lng": 13.8247993,
  "range": 10000
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|lat|number|false|none|Latitude|
|lng|number|false|none|Longitude|
|range|number|false|none|Range in meters to get sensor data|

<h2 id="tocS_DateRange">DateRange</h2>
<!-- backwards compatibility -->
<a id="schemadaterange"></a>
<a id="schema_DateRange"></a>
<a id="tocSdaterange"></a>
<a id="tocsdaterange"></a>

```json
{
  "startDate": "YYYY-MM-DD HH:MM:SS",
  "endDate": "YYYY-MM-DD HH:MM:SS"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|startDate|string|false|none|Start date|
|endDate|string|false|none|End date|

<h2 id="tocS_WiFiList">WiFiList</h2>
<!-- backwards compatibility -->
<a id="schemawifilist"></a>
<a id="schema_WiFiList"></a>
<a id="tocSwifilist"></a>
<a id="tocswifilist"></a>

```json
[
  {
    "macAddress": "88:78:73:84:B9:C6",
    "strength": "-43",
    "SNR": "0",
    "channel": "11"
  }
]

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[WiFiList_inner](#schemawifilist_inner)]|false|none|none|

<h2 id="tocS_WiFiList_inner">WiFiList_inner</h2>
<!-- backwards compatibility -->
<a id="schemawifilist_inner"></a>
<a id="schema_WiFiList_inner"></a>
<a id="tocSwifilist_inner"></a>
<a id="tocswifilist_inner"></a>

```json
{
  "macAddress": "88:78:73:84:B9:C6",
  "strength": "-43",
  "SNR": "0",
  "channel": "11"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|macAddress|string|false|none|none|
|strength|string|false|none|none|
|SNR|string|false|none|none|
|channel|string|false|none|none|
