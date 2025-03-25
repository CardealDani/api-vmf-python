import os
import time
import gspread
from google.oauth2.service_account import Credentials
from gspread.exceptions import APIError

# Recuperando as variáveis de ambiente
key_info = {
    "type": "service_account",
    "project_id": os.getenv("project_id"),
    "private_key_id": os.getenv("private_key_id"),
    "client_email": os.getenv("client_email"),
    "client_id": os.getenv("client_id"),
    "auth_uri": os.getenv("auth_uri"),
    "token_uri": os.getenv("token_uri"),
    "auth_provider_x509_cert_url": os.getenv("auth_provider_x509_cert_url"),
    "client_x509_cert_url": os.getenv("client_x509_cert_url"),
    "universe_domain": os.getenv("universe_domain"),
}

# Garantir que todas as variáveis estejam definidas
for key, value in key_info.items():
    if value is None:
        raise ValueError(f"A variável de ambiente {key} não está definida.")

# Corrigir a chave privada (substituindo \n)
private_key = os.getenv("private_key")
if private_key:
    private_key = private_key.replace('\\n', '\n')
else:
    raise ValueError("A chave privada não foi encontrada na variável de ambiente.")

key_info["private_key"] = private_key

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# Criar as credenciais com a chave JSON reconstruída
creds = Credentials.from_service_account_info(key_info, scopes=SCOPES)

# Usar gspread com as credenciais
gc = gspread.authorize(creds)

# Acessar a planilha
CODE = "1B7huX51Ta8nyxYw-Jh04GUSzlhJTezBP6XcpHvErwx4"
sheet = gc.open_by_key(CODE)

# Acessar as abas da planilha
caminhos = {
    "obrigatorias": "Obrigatórias",
    "eletivas": "Eletivas",
    "optativas": "Optativas"
}

planilhas = {}

# Sistema de Retry com cache
def get_planilha(nome):
    if nome in planilhas:
        return planilhas[nome]  # Retorna do cache
    
    retries = 3
    for tentativa in range(retries):
        try:
            planilhas[nome] = sheet.worksheet(caminhos[nome])  # Busca e armazena no cache
            return planilhas[nome]
        except APIError as e:
            if "Quota exceeded" in str(e):
                espera = 2 ** tentativa  # 2, 4, 8 segundos
                print(f"Quota excedida. Tentando novamente em {espera} segundos...")
                time.sleep(espera)
            else:
                raise e  # Se for outro erro, levanta a exceção normalmente
    raise APIError(f"Falha ao carregar a planilha {nome} após várias tentativas.")

# Obtendo as planilhas com retry e cache
excel_obrigatorias = get_planilha("obrigatorias")
excel_eletivas = get_planilha("eletivas")
excel_optativas = get_planilha("optativas")

# Função otimizada para contar valores em uma coluna sem chamadas repetidas
def contar_coluna(planilha, col_num):
    col_values = planilha.col_values(col_num)  # Pega toda a coluna de uma vez
    return len(col_values)

# Obter as contagens
len_semestre1 = contar_coluna(excel_obrigatorias, 2)
len_semestre2 = contar_coluna(excel_obrigatorias, 7)
len_semestre3 = contar_coluna(excel_obrigatorias, 12)
len_semestre4 = contar_coluna(excel_obrigatorias, 17)
len_semestre5 = contar_coluna(excel_obrigatorias, 22)
len_semestre6 = contar_coluna(excel_obrigatorias, 27)
len_semestre7 = contar_coluna(excel_obrigatorias, 32)
len_semestre8 = contar_coluna(excel_obrigatorias, 37)

len_semestre4_eletivas = contar_coluna(excel_eletivas, 2)
len_semestre5_eletivas = contar_coluna(excel_eletivas, 7)

len_optativas = contar_coluna(excel_optativas, 2)
