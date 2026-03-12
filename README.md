# Bem vindo (a) ao SRE Platform Lab !!

![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![Prometheus](https://img.shields.io/badge/Monitoring-Prometheus-orange)
![Grafana](https://img.shields.io/badge/Dashboard-Grafana-yellow)
![SRE](https://img.shields.io/badge/SRE-Lab-green)

Este laboratório de estudo é focado em práticas de Site Reliability Engineering (SRE), observabilidade e confiabilidade de microserviços.

O objetivo deste projeto é simular um ambiente real de produção utilizando ferramentas comuns nas arquiteturas.



# Arquitetura do laboratório

O ambiente é composto por microserviços simples executando em containers Docker e orquestrados com Docker Compose.

Os serviços atualmente simulados são:

- auth-service → responsável por autenticação
- analytics-service → responsável pelo processamento de eventos

Esses serviços geram métricas que são coletadas pela stack de observabilidade.

---

# Stack utilizada

Infraestrutura:

- Docker
- Docker Compose

Monitoramento:

- Prometheus
- Grafana

---

# Como o laboratório funciona

1️⃣ Os microserviços são executados em containers Docker  
2️⃣ O Docker Compose gerencia toda a infraestrutura local  
3️⃣ O Prometheus coleta métricas expostas pelos serviços  
4️⃣ O Grafana visualiza essas métricas em dashboards  

Isso permite simular um ambiente semelhante ao utilizado em sistemas distribuídos modernos.

---

# Estrutura do projeto


```text
sre-platform-lab
│
├── docker
│   └── docker-compose.yml
│
├── monitoring
│   └── prometheus.yml
│
├── services
│   ├── auth-service
│   └── analytics-service
```


---

# Objetivo do laboratório

Este laboratório foi criado para estudar e praticar conceitos de:

- observabilidade
- monitoramento de microserviços
- confiabilidade de sistemas distribuídos
- troubleshooting em ambientes cloud-native e on-premisses

---

# Próximos passos

Evoluções planejadas para o laboratório:

- criação de alertas com Alertmanager
- centralização de logs
- observabilidade completa do sistema

