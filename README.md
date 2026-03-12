# SRE Platform Lab

Laboratório de estudo para práticas de **Site Reliability Engineering (SRE)** focado em **observabilidade, monitoramento e confiabilidade de microserviços**.

O objetivo deste projeto é simular um ambiente real de produção utilizando ferramentas amplamente utilizadas em ambientes **cloud-native**.

---

# Arquitetura

Este laboratório utiliza um stack completo de observabilidade baseado em ferramentas open source.

Arquitetura simplificada:

Microservices
│
├── Metrics → Prometheus
│
├── Logs → Loki
│ └── Promtail
│
├── Dashboards → Grafana
│
└── Alerts → Alertmanager


Componentes adicionais:

- Node Exporter (métricas do host)
- cAdvisor (métricas de containers)

---

# Tecnologias utilizadas

Este laboratório utiliza ferramentas comuns em ambientes DevOps e SRE.

- Docker
- Docker Compose
- Prometheus
- Grafana
- Loki
- Promtail
- Alertmanager
- Node Exporter
- cAdvisor

---

# Estrutura do projeto

sre-platform-lab
│
├── docker
│ └── docker-compose.yml
│
├── monitoring
│ ├── prometheus.yml
│ ├── loki
│ │ └── loki-config.yml
│ └── alertmanager
│
├── services
│ ├── analytics-service
│ └── auth-service
│
└── docs
└── images


---

# Como executar o laboratório

Clone o repositório:

```bash
git clone https://github.com/erick-projetos/sre-platform-lab.git
cd sre-platform-lab/docker

# Suba o ambiente:
comando docker-compose up -d


# Serviços e suas portas:
| Serviço           | Porta |
| ----------------- | ----- |
| Grafana           | 3000  |
| Prometheus        | 9090  |
| Loki              | 3100  |
| Alertmanager      | 9093  |
| Analytics Service | 8002  |
| Auth Service      | 8001  |

# Dashboards

Os dashboards do Grafana exibem métricas importantes da aplicação.

Exemplos de métricas monitoradas:

Request rate

Latência de requisições

Taxa de erro

Eventos processados

Uso de CPU


# Alertas implementados

Este laboratório possui exemplos de alertas utilizados em ambientes SRE.

Alertas configurados:

Analytics Service Down

High Error Rate

High Latency

Os alertas são gerenciados pelo Alertmanager.

# Observabilidade

Este laboratório demonstra os três pilares da observabilidade.

Pilar	Ferramenta
Metrics	Prometheus
Logs	Loki
Visualization	Grafana

# Logs

Os logs das aplicações são coletados usando:

Promtail → Loki → Grafana

Isso permite consultar logs diretamente no Grafana usando LogQL.

# Objetivo do projeto

Este projeto foi criado como laboratório pessoal para estudo de:

Observabilidade

Monitoramento de microserviços

Práticas de Site Reliability Engineering

Arquiteturas cloud-native

Operação de sistemas distribuídos



# Evoluções planejadas para o laboratório:

Traces distribuidos no Grafana

Deploy em Kubernetes

Chaos Engineering

Integração com CI/CD

Testes de carga

# Autor Erick Saraiva

Projeto desenvolvido como laboratório pessoal para estudo de DevOps e Site Reliability Engineering.
