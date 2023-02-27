<style>
    <!-- .md-grid { -->
    <!--   max-width: 960px; -->
    <!-- } -->
    * {
      font-size: .72rem;
    }
    .md-typeset h1 {
      margin: 0em;
    }
</style>
# Matthew Grossman
## Employment
### Infra Tech Lead, Developer Environments @ [Lyft](https://lyft.com) *(2020 - Current)*

> *Developer Environments* is a platform team focused on creating infrastucture and tooling to safely accelerate developer productivity.

Led team of 5 eng through many successful launches by creating a multi-year roadmap, directly mentoring ICs (junior through senior), and negotiating ownership with cross-team stakeholders (networking/deploys/observability/security). 
Represented team in director reviews and 15+ presentations as I evangelized our products across the company.

#### Project: <u>E2E Testing Environment Revamp</u>
* Led a multi-year effort to deprecate our existing E2E testing solution in favor of a more cost-efficient and productive developer environment. 
Rather than giving each dev their own expensive EC2, we leverage our shared staging environment and dynamic routing to enable request-level isolation. 
* Worked wherever I was needed, including python/go/typescript libraries, [service mesh](https://github.com/envoyproxy/envoy/pulls?q=is%3Apr+author%3Amatthewgrossman+), github hooks, local tools, pair-programming, project updates, and much more.
* Read more about our work in my [blog post](https://eng.lyft.com/scaling-productivity-on-microservices-at-lyft-part-3-extending-our-envoy-mesh-with-staging-fdaafafca82f), or watch my presentation from _envoycon 2022_ ([recording](https://www.youtube.com/watch?v=p9dYr23MVv0), [abstract](https://envoyconna22.sched.com/event/1AO5k), [slides](assets/envoycon2022.pdf)).
* **Impact**: Reduced infra spend by $170k/mo and lowered maintenance costs for all of infra.

#### Project: <u>Distributed Tracing</u>
* Led relaunch and migration of our distributed tracing system (`OpenTracing` -> `OpenTelemetry`).
* Researched and met external vendors to evaluate cost/functionality tradeoffs, and worked with procurement to finalize commitments.
* Wrote python/go libraries, configured collector agents, surveyed engineers, and managed project status.
* **Impact**: Provided developers an invaluable debugging tool while giving the business contractual flexibility with tracing providers.

### Product Tech Lead, Express Drive @ [Lyft](https://lyft.com) *(2016 - 2020)*

> *Express Drive* is a product enabling drivers to rent vehicles through Lyft, creating a valuable supply lever for the business.


Architected and led many customer-facing projects, working with data science, design, product, and operations to launch features.

#### Project: <u>Volume-Based Pricing</u>

* To ensure insurance costs were attributed to high-mileage drivers, we created rentals plans that charged per-mile.
I was the primary technical lead for integration efforts, ensuring multiple work streams (mobile, backend, frontend; 10+ eng) all were unblocked and convened for an on-time launch.
* Led the creation of a high RPS service that subscribed to our fleet's telemetry events, and segmented miles driven in-app versus off-app.
Architected this service from scratch, laying the groundwork for local development, databases, design patterns, and testing.
* **Impact**: Financial reduction of $40/vehicle/wk (~5000 weekly vehicles at the time).

#### Project: <u>Oncall Toil Reduction</u>

* Worked with eng management to reduce burnout and improve velocity by tackling our out-of-control oncall rotation.
Implemented Pagerduty alert tagging policy to ensure properly attributed pages.
* Identified and tactically solved select high-leverage issues (ex. flakey endpoints, underprovisioning).
* **Impact**: Reduced number of oncall alerts from ~50/wk → ~5/wk.

### Languages and Technologies
* `python`, `go` (familiarity with `typescript`, `c++`)
* docker, kubernetes, envoy, opentelemetry
* dynamodb, redis, protobuf

### Side projects
* <u>[dotfiles](https://github.com/matthewgrossman/dotfiles)</u>: terminal emulators, neovim, and hammerspoon
* <u>[mrgrossman.com](https://mrgrossman.com)</u>: SSG [mkdocs-material](https://squidfunk.github.io/mkdocs-material/), used for this [resume](https://mrgrossman.com/resume) as well
* homelab: ansible, raspberry pis, tailscale, docker-compose, and traefik

### Internships *(2012 - 2016)*

* Promoted Listings @ Etsy
* Unified Notifications @ Google
* iOS @ Facebook

## Education
### **University of Michigan - Ann Arbor** *(2012 - 2016)*
* 3.93 GPA – BSE in Computer Science and Engineering, Class of 2016
* Dean’s List; 2012 - 2016
