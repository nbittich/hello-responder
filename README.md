- Build the image:
`docker build -t cortexneurons/hello-responder:dev .`

- Create the catalog for cortex under e.g `/home/nbittich/cortex/custome-responders.json`:


```json
[
    {
        "dockerImage": "cortexneurons/hello-responder:dev",
        "name": "Hello",
        "version": "1.0",
        "author": "nbittich",
        "url": "https://github.com/nbittich/hello-responder",
        "license": "AGPL-V3",
        "description": "Say hello",
        "dataTypeList": [
            "thehive:case",
            "thehive:alert",
            "thehive:case_task"
        ],
        "command": "hello-responder/hello.py",
        "baseConfig": "Hello",
        "registration_required": false,
        "subscription_required": false,
        "free_subscription": true,
        "configurationItems": [
            {
                "name": "message",
                "description": "Message to output",
                "type": "string",
                "multi": false,
                "required": true,
                "defaultValue": "Hello, world!"
            }
        ]
    }
]
```
- Map the volume under the cortex service in docker-compose.yml:

```yml
    volumes:
      ... other volumes
      - /home/nbittich/cortex/custome-responders.json:/opt/custom-responders/responders.json
```


- Modify your cortex config (application.conf):

```
responder {
  urls = [
    "https://download.thehive-project.org/responders.json"
    "/opt/cortexneurons/responders"
    "/opt/custom-responders/responders.json"
  ]

  fork-join-executor {
    parallelism-min = 2
    parallelism-factor = 2.0
    parallelism-max = 4
  }
}
```
