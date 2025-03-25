import os
import gspread
from google.oauth2.service_account import Credentials

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
caminho = "Obrigatórias"
caminho_eletivas = "Eletivas"
caminho_optativas = "Optativas"
excel_obrigatorias = sheet.worksheet(caminho)
excel_eletivas = sheet.worksheet(caminho_eletivas)
excel_optativas = sheet.worksheet(caminho_optativas)

# Obter as contagens
len_semestre1 = len(excel_obrigatorias.col_values(2))
len_semestre2 = len(excel_obrigatorias.col_values(7))
len_semestre3 = len(excel_obrigatorias.col_values(12))
len_semestre4 = len(excel_obrigatorias.col_values(17))
len_semestre5 = len(excel_obrigatorias.col_values(22))
len_semestre6 = len(excel_obrigatorias.col_values(27))
len_semestre7 = len(excel_obrigatorias.col_values(32))
len_semestre8 = len(excel_obrigatorias.col_values(37))

len_semestre4_eletivas = len(excel_eletivas.col_values(2))
len_semestre5_eletivas = len(excel_eletivas.col_values(7))

len_optativas = len(excel_optativas.col_values(2))
