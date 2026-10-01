# Red Team Reconnaissance & Banner Grabbing Tool

Aviso Legal: Esta ferramenta foi desenvolvida estritamente para fins educacionais e testes de intrusão autorizados. O autor não se responsabiliza por qualquer uso indevido ou danos causados pelo software em redes de terceiros. Utilize apenas em ambientes controlados e com permissão explícita.


> **Projeto Pratico de Ciberseguranca:** Criacao de uma ferramenta modular em Python para reconhecimento de rede, varredura de portas TCP e captura de banners de servicos, com foco em automacao e analise ofensiva.
> 
> 

---

## Sobre o Projeto

Como estudante de Ciberseguranca, desenvolvi esta ferramenta para entender na pratica o funcionamento de varreduras de rede e enumeracao de servicos. O objetivo principal foi criar um script robusto, utilizando apenas bibliotecas nativas do Python para garantir portabilidade maxima, capaz de realizar descoberta de alvos, paralelizacao de tarefas e geracao de relatorios automatizados.

Neste projeto, utilizei conceitos de *socket programming*, threads concorrentes (`ThreadPoolExecutor`) e engenharia de software para estruturar a logica de forma limpa e modularizada, separando a configuracao, o banner grabbing, o escaneamento e a exportacao de dados em formatos compativeis com automacao (JSON) e leitura executiva (TXT).

---

## Arquitetura e Tecnologias

* **Linguagem:** Python 3


* **Rede & Conexoes:** Biblioteca nativa `socket` (comunicacao TCP/IPv4)


* **Paralelismo:** Biblioteca nativa `concurrent.futures` (`ThreadPoolExecutor` com 10 workers)


* **Manipulacao de Dados:** Biblioteca nativa `json`

* **Formatos de Saida:** Relatorios duplos em `.json` e `.txt`


---

## Modulos do Codigo

O projeto foi estruturado em quatro blocos logicos bem definidos para facilitar a manutencao e leitura:

1. **Configuracoes e Imports:** Declaracao das bibliotecas padrao e definicao da lista de portas comuns mais visadas em auditorias.


2. **Banner Grabbing:** Funcao dedicada a conectar no servico ativo, extrair assinaturas de banner e injetar requisicoes HTTP para forcar respostas em servidores web (portas 80 e 8080).


3. **Logica de Escaneamento:** Validacao do estado das portas (`open` ou `closed`) utilizando `connect_ex` e integracao com as threads em paralelo.


4. **Execucao Principal (Main):** Gerenciamento da entrada do usuario, resolucao automatica de DNS para IP, controle do pool de threads e gravacao simultanea dos arquivos de relatorio.



---

## Passo a Passo de Execucao & Explicativo dos Comandos

### 1. Inicializacao do Script

```bash
python3 recon_scanner.py

```

* **O que faz:** Executa o script principal a partir do terminal do Kali Linux.



---

### 2. Fornecimento do Alvo

Digite o IP ou dominio desejado (ex: `127.0.0.1` ou `scanme.nmap.org`). O script resolve o endereco automaticamente e inicia o pool de 10 threads em paralelo.

---

### 3. Analise dos Relatorios Gerados

Apos a conclusao, o script gera dois arquivos na mesma pasta:

* `scan_[IP].json`: Arquivo estruturado contendo todos os dados da varredura, perfeito para integracao com outras ferramentas e automacoes.


* `scan_[IP].txt`: Relatorio formatado e limpo, ideal para leitura humana direta ou composicao de relatorios de auditoria.



---

## Aprendizados Alcancados

* **Programacao de Redes em Python:** Compreensao pratica de como *sockets* de baixo nivel lidam com *handshakes* TCP e *timeout* de conexoes.


* **Concorrencia e Performance:** Como o uso de `ThreadPoolExecutor` acelera drasticamente varreduras de portas em comparacao a execucoes sequenciais.


* **Engenharia de Relatorios:** Importancia de fornecer saidas multiplas (dados estruturados e texto legivel) para atender tanto a automacoes quanto a analises executivas em testes de intrusao.
