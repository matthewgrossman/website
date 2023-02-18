<style>
    .md-grid {
      max-width: 960px;
    }
</style>
# Resume
---

## Employment


### **Infra Tech Lead, Developer Environments** @ [Lyft](https://lyft.com) *(2020 - Current)*

> *Developer Environments* is a platform team focused on creating infrastucture and tooling to safely accelerate developer productivity.

Led team of 5 eng through many successful launches by creating/aligning on a multi-year vision/roadmap, directly mentoring the ICs (levels 3-5), and negotiating ownership with x-team stakeholders (networking/deploys/obs/security). 
Represented team in director reviews and 15+ presentations as I evangelized our dev product across the company.

#### <u>E2E Testing Environment Revamp</u>
* Led a multi-year effort to deprecate our existing E2E testing solution in favor of a more cost-efficient and productive dev environment. 
Rather than giving each dev their own expensive EC2, we leverage our shared staging environment and dynamic routing to enable request-level isolation. 
* Worked wherever I was needed, including jenkins/deploys, python/go/typescript libraries, networking, devtools, pair-programming, project updates, and much more.
* Read more about our work in my [blog post](https://eng.lyft.com/scaling-productivity-on-microservices-at-lyft-part-3-extending-our-envoy-mesh-with-staging-fdaafafca82f), or watch my presentation from _envoycon 2022_ ([recording](https://www.youtube.com/watch?v=p9dYr23MVv0), [abstract](https://envoyconna22.sched.com/event/1AO5k), [slides](assets/envoycon2022.pdf))

**Impact**: Reduced infra spend by $170k/mo and lowered maintenance costs for all of infra.<br/>
**Technologies**: envoy, docker, kubernetes, a smidge of c++

#### <u>Distributed Tracing</u>
* TODO 

**Impact**: TODO <br/>
**Technologies**: opentracing/opentelemetry, lightstep/X-Ray, procurement red tape
---
### **Product Tech Lead, Express Drive** @ [Lyft](https://lyft.com) *(2016 - 2020)*

> *Express Drive* is a product enabling drivers to rent vehicles through Lyft, creating a valuable supply lever for the business.


Architected and led many customer-facing projects, working with data science, design, product, and operations to launch features.

#### <u>Volume-Based Pricing</u>

* To ensure insurance costs were attributed to high-mileage drivers, we created rentals plans that charged per-mile.
I was the primary technical POC for integration efforts, ensuring multiple work streams (mobile, backend, frontend; 10+ eng) all were unblocked and convened for an on-time launch.
* Led the creation of a high RPS service that subscribed to our fleet's telemetry events, and segmented miles driven in-app versus off-app.
Architected this service from scratch, laying the groundwork for local development, databases, design patterns, and testing.

**Impact**: Financial reduction of $40/vehicle/wk (~5000 weekly vehicles at the time)<br/>
**Technologies**: python, flask, typescript, protobuffers, dynamodb, redis, EC2

#### <u>Oncall Toil Reduction</u>

* Worked with eng management to reduce burnout and improve velocity by tackling our out-of-control oncall rotation.
Implemented Pagerduty alert tagging policy to ensure properly attributed pages.
* Identified and tactically solved select high-leverage issues (ex. flakey endpoints, underprovisioning)

**Impact**: Reduced number of oncall alerts from ~50/wk → ~5/wk <br/>
**Technologies**: SQL, Mode/Superset, GSheets, pagerduty API

---
### **Internships** *(2012 - 2016)*

* Promoted Listings @ Etsy
* Unified Notifications @ Google
* iOS @ Facebook

---
### **Side projects**
* <u>[dotfiles](https://github.com/matthewgrossman/dotfiles)</u>: Talk to me about terminal emulators, neovim, and hammerspoon!
* <u>homelab</u>: Talk to me about ansible, raspberry pis, tailscale, docker-compose, and traefik!

---
## Education
### **University of Michigan - Ann Arbor** *(2012 - 2016)*
* 3.93 GPA – BSE in Computer Science and Engineering, Class of 2016
* Dean’s List; 2012 - 2016
