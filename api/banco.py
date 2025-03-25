import os
import gspread
from google.oauth2.service_account import Credentials

# Recuperando as variáveis de ambiente
key_info = {
    "type": "service_account",  # O tipo geralmente é 'service_account'
    "project_id": os.getenv("GOOGLE_CLOUD_PROJECT_ID"),
    "private_key_id": os.getenv("GOOGLE_CLOUD_PRIVATE_KEY_ID"),
    "private_key": os.getenv("GOOGLE_CLOUD_PRIVATE_KEY").replace('\\n', '\n'),  # Corrigindo quebra de linha
    "client_email": os.getenv("GOOGLE_CLOUD_CLIENT_EMAIL"),
    "client_id": os.getenv("GOOGLE_CLOUD_CLIENT_ID"),
    "auth_uri": os.getenv("GOOGLE_CLOUD_AUTH_URI"),
    "token_uri": os.getenv("GOOGLE_CLOUD_TOKEN_URI"),
    "auth_provider_x509_cert_url": os.getenv("GOOGLE_CLOUD_AUTH_PROVIDER_X509_CERT_URL"),
    "client_x509_cert_url": os.getenv("GOOGLE_CLOUD_CLIENT_X509_CERT_URL")
}
key_info["private_key"] = os.getenv("GOOGLE_CLOUD_PRIVATE_KEY").replace('\\n', '\n')
# Verificar se todas as variáveis de ambiente estão presentes
for key, value in key_info.items():
    if value is None:
        raise ValueError(f"A variável de ambiente {key} não está definida.")

# Criar as credenciais com a chave JSON reconstruída
creds = Credentials.from_service_account_info(key_info)

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
