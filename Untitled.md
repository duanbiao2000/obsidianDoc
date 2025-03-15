```mermaid
classDiagram class Client { -service: Service +Client(service: Service) +useService() } class Service { +performAction() } Client --|> Service : uses
```

