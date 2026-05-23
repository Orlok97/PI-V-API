# Projeto Integrador V - Monitoramento da Qualidade do Ar

Sistema desenvolvido em Flask para monitoramento da qualidade do ar, temperatura e umidade através de sensores IoT.

## 📋 Sobre o Projeto

Este projeto tem como objetivo coletar e armazenar dados ambientais enviados por sensores, permitindo o monitoramento de:

- 🌡️ Temperatura
- 💧 Umidade
- 🌫️ Qualidade do ar

Os dados são armazenados em banco de dados e disponibilizados através de endpoints REST.

---

# 🛠️ Tecnologias Utilizadas

- Python 3
- Flask
- SQLAlchemy
- SQLite/MySQL (dependendo da configuração)
- Flask Blueprint

---

# 📦 Instalação

## 1. Clone o repositório

```bash
git clone https://github.com/Orlok97/PI-V-API.git
```

## 2. Acesse a pasta do projeto

```bash
cd PI-V-API
```

## 3. Crie um ambiente virtual

### Linux/macOS

```bash
python -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 4. Instale as dependências

```bash
pip install -r requirements.txt
```

---

# Configuração das Variáveis de Ambiente

Crie um arquivo chamado `.env` na raiz do projeto para configurar a conexão com o banco de dados.

## Exemplo

```env
DATABASE_URI='mysql+pymysql://USER:PASSWORD@HOST:PORT/DATABASE'
```

### Exemplo real

```env
DATABASE_URI='mysql+pymysql://root:123456@localhost:3306/air_monitoring'
```

---

# ▶️ Como Rodar o Projeto

## Executar o servidor Flask

```bash
flask run
```

Ou:

```bash
python app.py
```

---

# 🌐 Acesso da API

Por padrão, a aplicação ficará disponível em:

```txt
http://127.0.0.1:5000
```

---

# 📡 Documentação dos Endpoints

## Base URL

```txt
/api/v1/sensor
```

---

## 🔍 Listar todos os dados dos sensores

### Endpoint

```http
GET /api/v1/sensor
```

### Resposta

```json
[
  {
    "id": 1,
    "temperature": 25.5,
    "humidity": 70,
    "air_quality": 320,
    "date_hour": "2026-05-23 14:30:00"
  }
]
```

---

## ➕ Enviar dados do sensor

### Endpoint

```http
POST /api/v1/sensor
```

### Body JSON

```json
{
  "temperature": 26.4,
  "humidity": 65,
  "air_quality": 280
}
```

### Resposta

```json
{
  "response": "dados enviados",
  "status": "sucesso"
}
```

---

## 🌡️ Obter última leitura registrada

### Endpoint

```http
GET /api/v1/sensor/current-temp
```

### Resposta

```json
{
  "id": 10,
  "temperature": 27.1,
  "humidity": 68,
  "air_quality": 300,
  "date_hour": "2026-05-23 15:10:00"
}
```

---

## 🔎 Buscar leitura por ID

### Endpoint

```http
GET /api/v1/sensor/<id>
```

### Exemplo

```http
GET /api/v1/sensor/1
```

### Resposta

```json
{
  "id": 1,
  "temperature": 25.5,
  "humidity": 70,
  "air_quality": 320,
  "date_hour": "2026-05-23 14:30:00"
}
```

# 👨‍💻 Autores


Projeto desenvolvido para o Projeto Integrador V da UNIVESP.

- Andrey Matos Florencio da Silva
- Bruno Alan Bezerra da Cruz
- Cristian Braz
- Diego Rodrigues de Alcantara 
- Francieli Brito Da Silva Luchetta 
- Lauro Xavier Belardo 
- Rafael Toledo Fernandes de Souza
- Renato Correia Alves 