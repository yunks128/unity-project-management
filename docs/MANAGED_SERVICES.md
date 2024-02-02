# Managed Services

Unity is made of managed services- managed in this context means that the deployment, maintenance, monitoring, and lifecycle of a service is handled by Unity developed code. some services are multi-tenant and are owned and operated by the Unity team. These have an SLA and are "available" to unity users through APIs and UIs. Other services are venue services, in which they are deployed specifically for a user or project into a venue. 

### Managed Services all have the following capabilities
* Current and Previous major versions of services shall be supported
* Continuall integrate and be tested in the Unity environment 

### Venue Managed Services have the following additional capabilities:
* Deployable through the management console
* Upgradeable through the management console
* Rollback (where allowed) for managed services is available through the management console
* Desctruction of managed services is available through the management console
* Customizable resources (e.g. cpu, ram, cluster sizes)
* Report or can be polled for health metrics 
* Automatic Validation scripts upon deployment

### Shared Services
* Breaking API changes will be retired after some period to allow for projects to migrate to new endpoints/functionalty on their own schedule
* A defined SLA

### Management Console
* User interface for deployment, monitoring, upgrading, and destruction of venue services
* ability to schedule upgrades for project defined mainteance windows 
* alert users to available updates of managed services
* notify users of pending and in-progress updates
* notify users based on service health metrics

