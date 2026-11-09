---
title: Resume
layout: resume
---
# Matthew Grossman
Staff Software Engineer |
[mrgrossman.com](_index.md) | [linkedin](https://www.linkedin.com/in/matthewryangrossman/) | [github](https://github.com/matthewgrossman/)
## Employment
### Software Engineer @ [NVIDIA](https://nvidia.com) *(2025 - Current)*

#### [NeMo Helix](https://github.com/NVIDIA-NeMo/nemo-helix)
Owned the data storage services for NeMo Helix (formerly the NeMo Microservices Platform), a collection of microservices and tools for training and deploying large language models.

* Inherited NeMo Datastore, a legacy service on life support, and kept it running through customer support, debugging, and bugfixes.
Later drove its full replacement with the new Files service: investigated the core problems with the prior service and wrote and socialized the design RFC.
Implemented the service with heavily optimized upload/download throughput, delegated across engineers, and coordinated migration across consumer teams.
* Led the effort to separate the platform's shipped artifacts into smaller, independently versioned Python wheels, allowing plugin authors to depend on a minimal package rather than the full platform.
Built custom Hatchling tooling to support the per-component build and publish pipeline.
* Replaced our Stainless-generated SDK with an in-house typed client library built on off-the-shelf Python libraries: endpoints are declared once as typed Python signatures, and decorators, `ParamSpec`, overloads, and descriptors turn them into fully typed sync and async clients with streaming, pagination, retries, and auth.
Adopted by every platform service and third-party plugin.
* Owned multiple platform components including core proxying for the inference gateway and job results integration, and drove improvements to developer experience and observability across NeMo services.

---

### Staff Software Engineer @ [Gretel](https://web.archive.org/web/20250602235257/https://gretel.ai/) *(2023 - 2025)*

#### Gretel Navigator
Key engineer on Navigator, a compound AI system that uses an agent-based approach — composing calls across multiple LLMs — to generate, edit, and augment synthetic tabular data from natural language prompts.

* Built and maintained the Python API service powering Navigator, and owned the inference routing layer abstracting over both self-hosted and third-party hosted LLMs.
Developed an LLM configuration system enabling easy experimentation and deployment of models directly from HuggingFace into our Kubernetes cluster.
* To support Navigator's inference backends, load-tested vLLM across GPU configurations, tuned Kubernetes autoscaling policies for LLM workloads, quantized models to reduce resource footprint, and built evaluation scripts to validate output quality.

---

### Infra Tech Lead, Developer Experience @ [Lyft](https://lyft.com) *(2020 - 2023)*

> *Developer Experience* is a platform team focused on creating infrastucture and tooling to safely accelerate developer productivity.

Led team of 5 eng through many successful launches by creating a multi-year roadmap, directly mentoring ICs (junior through senior), and negotiating ownership with cross-team stakeholders (networking/deploys/observability/security).
Represented team in director reviews and 15+ presentations as I evangelized our products across the company.

#### E2E Testing Environment Revamp
* Led a multi-year effort to deprecate our existing E2E testing solution in favor of a more cost-efficient and productive developer environment.
Rather than giving each dev their own expensive EC2, we leveraged our shared staging environment and dynamic routing to enable request-level isolation.
* Worked wherever I was needed, including `python`/`go`/`typescript` libraries, [service mesh](https://github.com/envoyproxy/envoy/pulls?q=is%3Apr+author%3Amatthewgrossman+), github hooks, local tools, pair-programming, project updates, and much more.
* Read more about our work in my [blog post](https://eng.lyft.com/scaling-productivity-on-microservices-at-lyft-part-3-extending-our-envoy-mesh-with-staging-fdaafafca82f), or watch my presentation from _EnvoyCon 2022_ ([recording](https://www.youtube.com/watch?v=p9dYr23MVv0), [abstract](https://envoyconna22.sched.com/event/1AO5k), [slides](assets/envoycon2022.pdf)).
* **Impact**: Reduced infra spend by $170k/mo and lowered maintenance costs for all of infra.

#### Distributed Tracing
* Led relaunch and migration of our distributed tracing system (`OpenTracing` -> `OpenTelemetry`).
* Researched and met external vendors to evaluate cost/functionality tradeoffs, and worked with procurement to finalize commitments.
* Wrote python/go libraries, configured collector agents, surveyed engineers, and managed project status.
* **Impact**: Provided developers an invaluable debugging tool while giving the business contractual flexibility with tracing providers.

---

### Product Tech Lead, Express Drive @ [Lyft](https://lyft.com) *(2016 - 2020)*

> *Express Drive* is a product enabling drivers to rent vehicles through Lyft, creating a valuable supply lever for the business.


Architected and led many customer-facing projects, working with data science, design, product, and operations to launch features.

#### Volume-Based Pricing

* To ensure insurance costs were attributed to high-mileage drivers, we created rentals plans that charged per-mile.
I was the primary technical lead for integration efforts, ensuring multiple work streams (mobile, backend, frontend; 10+ eng) all were unblocked and convened for an on-time launch.
* Led the creation of a high RPS service that subscribed to our fleet's telemetry events, and segmented miles driven in-app versus off-app.
Architected this service from scratch, laying the groundwork for local development, databases, design patterns, and testing.
* **Impact**: Financial reduction of $40/vehicle/wk (~5000 weekly vehicles at the time).

#### Oncall Toil Reduction

* Worked with eng management to reduce burnout and improve velocity by tackling our out-of-control oncall rotation.
Implemented Pagerduty alert tagging policy to ensure properly attributed pages.
* Identified and tactically solved select high-leverage issues (ex. flakey endpoints, underprovisioning).
* **Impact**: Reduced number of oncall alerts from ~50/wk → ~5/wk.

---

### Languages and Technologies
* `python`, `go`
* docker, kubernetes, envoy, opentelemetry
* dynamodb, redis, protobuf

---

### Side projects
* [dotfiles](https://github.com/matthewgrossman/dotfiles): terminal emulators, neovim, and hammerspoon
* [mrgrossman.com](https://github.com/matthewgrossman/website): SSG [Hugo](https://gohugo.io), used for this [resume](resume.md) as well
* homelab: ansible, raspberry pis, tailscale, docker-compose, and traefik

---

### Internships *(2012 - 2016)*

* Promoted Listings @ Etsy
* Unified Notifications @ Google
* iOS @ Facebook

## Education
### **University of Michigan - Ann Arbor** *(2012 - 2016)*
* 3.93 GPA – BSE in Computer Science and Engineering, Class of 2016
* Dean’s List; 2012 - 2016
