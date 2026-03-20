# 🚀 SRE Platform Lab

Laboratório prático de observabilidade, confiabilidade e SRE inspirado em ambientes reais de produção.

![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![Prometheus](https://img.shields.io/badge/Monitoring-Prometheus-orange)
![Grafana](https://img.shields.io/badge/Dashboard-Grafana-yellow)
![SRE](https://img.shields.io/badge/SRE-Lab-green)

---

# Arquitetura

```
App → Prometheus → Alertmanager → Slack
        ↘ Grafana
        ↘ Loki
        ↘ Tempo
```

---

# Arquitetura do laboratório

O ambiente é composto por microserviços simples executados em containers Docker e orquestrados com Docker Compose, onde são aplicadas práticas de monitoramento, instrumentação e correlação de logs e traces, além da configuração de alertas com Alertmanager e envio de notificações via Slack.

### Microserviços simulados:

* auth-service → responsável por autenticação
* analytics-service → responsável pelo processamento de eventos
* app → serviço principal instrumentado

Esses serviços geram métricas que são coletadas pela stack de observabilidade.

---

# Stack utilizada

### Infraestrutura

* Docker
* Docker Compose

### Monitoramento

* Prometheus
* Grafana
* Alertmanager

### Observabilidade

* Loki (logs)
* Tempo (traces)
* OpenTelemetry (instrumentação)

---

# Como o laboratório funciona

- Microserviços executados em containers Docker  
- Orquestração via Docker Compose  
- Coleta de métricas com Prometheus  
- Visualização com Grafana  
- Gerenciamento de alertas com Alertmanager  
- Notificações em tempo real via Slack  

Isso permite simular um ambiente semelhante ao utilizado em sistemas distribuídos modernos.

---

# Serviços e portas

| Serviço           | Porta |
| ----------------- | ----- |
| Grafana           | 3000  |
| Prometheus        | 9090  |
| Loki              | 3100  |
| Alertmanager      | 9093  |
| Analytics Service | 8002  |
| Auth Service      | 8001  |

---

# Estrutura do projeto

```text
sre-platform-lab/
│
├── docker/
│   └── docker-compose.yml
│
├── monitoring/
│   ├── prometheus.yml
│   ├── alerts.yml
│   ├── alertmanager.yml
│   ├── loki/
│   ├── promtail/
│   └── tempo/
│
├── services/
│   ├── auth-service/
│   ├── analytics-service/
│   └── app/
│
├── chaos/
│   └── (em breve...)
│
├── dashboards/
│
│
└── README.md
```

---

## Funcionalidades implementadas

* Métricas customizadas (requests, erros, latência)
* Alertas baseados em SLO (error rate, latency, no traffic)
* Integração com Slack (notificação em tempo real)
* Correlação logs ↔ traces (Loki + Tempo)
* Dashboard estilo NOC no Grafana

---


## Como executar

```bash
docker-compose up -d --build
```

Acessos:

* Grafana → http://localhost:3000
* Prometheus → http://localhost:9090
* Alertmanager → http://localhost:9093


---






## Prometheus
<img width="1911" height="593" alt="Grafana" src="https://github.com/user-attachments/assets/e49256d5-6249-43ee-803a-f723ab589f79" />

## Grafana
<img width="1889" height="539" alt="prometheus" src="https://github.com/user-attachments/assets/ec52480a-7e3e-4c97-a17c-d67a36f91270" />

## Correlação Logs e Traces (Loki + Tempo)
<img width="1890" height="874" alt="correlação" src="https://github.com/user-attachments/assets/d5677825-3323-4474-9a39-4ca8f219fcf4" />

## Notificação no Slack
<img width="590" height="435" alt="Slack" src="https://github.com/user-attachments/assets/350fcaec-2983-4f88-8441-643b0c9dd280" />

## Alertas no Alertmanager
<img width="860" height="786" alt="Alertmanager" src="https://github.com/user-attachments/assets/187de70e-4ff3-491e-8a44-9b3e55f36140" />



---






