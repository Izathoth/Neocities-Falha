import requests
import time
import threading
import random
import logging
from datetime import datetime
from fake_useragent import UserAgent

# Configuração do log
logging.basicConfig(
    filename="pentest_requests.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Classe para lidar com requisições
class RequisicoesPentest:
    def __init__(self, url, num_requisicoes, intervalo, num_threads, retries=3):
        self.url = url
        self.num_requisicoes = num_requisicoes
        self.intervalo = intervalo
        self.num_threads = num_threads
        self.retries = retries  # Número de tentativas em caso de falha
        self.ua = UserAgent()  # Para gerar user agents aleatórios

    def enviar_requisicao(self, i):
        try:
            # Escolher um método aleatório entre GET, POST, PUT, DELETE
            metodo = random.choice(['GET', 'POST', 'PUT', 'DELETE'])
            
            headers = {
                "User-Agent": self.ua.random,
                "Accept-Language": "en-US,en;q=0.9",  # Cabeçalhos adicionais para simular comportamento real
                "Accept-Encoding": "gzip, deflate, br"
            }

            # Adicionando cookies aleatórios
            cookies = {
                'session': f'{random.randint(100000, 999999)}',
                'auth_token': f'{random.randint(100000, 999999)}'
            }

            # Tentativas múltiplas em caso de erro
            for attempt in range(self.retries):
                try:
                    response = requests.request(metodo, self.url, headers=headers, cookies=cookies, timeout=5)
                    if response.status_code == 200:
                        logging.info(f"Requisição {i+1} {metodo} bem sucedida: {response.status_code} - Tempo de resposta: {response.elapsed.total_seconds()} segundos")
                        print(f"Requisição {i+1} {metodo} bem sucedida: {response.status_code} - Tempo de resposta: {response.elapsed.total_seconds()} segundos")
                    else:
                        logging.warning(f"Requisição {i+1} {metodo} falhou: Status {response.status_code}")
                        print(f"Requisição {i+1} {metodo} falhou: Status {response.status_code}")
                    break
                except requests.exceptions.RequestException as e:
                    if attempt == self.retries - 1:
                        logging.error(f"Erro na requisição {i+1}: {e}")
                        print(f"Erro na requisição {i+1}: {e}")
                    else:
                        logging.warning(f"Tentativa {attempt+1} falhou para a requisição {i+1}, tentando novamente...")
                        print(f"Tentativa {attempt+1} falhou para a requisição {i+1}, tentando novamente...")
                    time.sleep(2)  # Espera 2 segundos antes de tentar novamente

        except Exception as e:
            logging.error(f"Erro geral na requisição {i+1}: {e}")
            print(f"Erro geral na requisição {i+1}: {e}")

    def enviar_requisicoes(self):
        while True:
            threads = []
            for i in range(self.num_requisicoes):
                # Usar threads para enviar as requisições paralelamente
                t = threading.Thread(target=self.enviar_requisicao, args=(i,))
                threads.append(t)
                t.start()
            
            # Aguardar todas as threads finalizarem
            for t in threads:
                t.join()
            
            # Intervalo entre os blocos de requisições
            intervalos_aleatorios = random.randint(self.intervalo - 1, self.intervalo + 3)
            print(f"Esperando {intervalos_aleatorios} segundos antes de enviar mais requisições...\n")
            logging.info(f"Aguardando {intervalos_aleatorios} segundos antes de enviar mais requisições.")
            time.sleep(intervalos_aleatorios)

# Configuração
url = "              "  # URL alvo

# Parâmetros
num_requisicoes = 20  # Número de requisições por intervalo
intervalo = 3  # Intervalo médio entre os blocos de requisições (em segundos)
num_threads = 10  # Número de threads para enviar as requisições em paralelo

# Criando o objeto de requisições e iniciando
pentest = RequisicoesPentest(url, num_requisicoes, intervalo, num_threads)
pentest.enviar_requisicoes()