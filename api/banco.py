import os
import json
import base64
import gspread
from google.oauth2.service_account import Credentials

# Recuperar a variável de ambiente
key_json_data = os.getenv("GOOGLE_KEY_JSON")

# Verificar se a variável está definida
if key_json_data is None:
    raise ValueError("A variável de ambiente GOOGLE_KEY_JSON não está definida.")

# Decodificar a chave base64
try:
    key_info = json.loads(base64.b64decode(key_json_data).decode('utf-8'))
except Exception as e:
    raise ValueError(f"Erro ao decodificar a chave: {e}")

# Criar as credenciais com a chave decodificada
creds = Credentials.from_service_account_info(key_info)

# Usar gspread com as credenciais
gc = gspread.authorize(creds)

CODE = "1B7huX51Ta8nyxYw-Jh04GUSzlhJTezBP6XcpHvErwx4"
sheet = gc.open_by_key(CODE)

caminho = "Obrigatórias"
caminho_eletivas = "Eletivas"
caminho_optativas = "Optativas"
excel_obrigatorias = sheet.worksheet(caminho)
excel_eletivas = sheet.worksheet(caminho_eletivas)
excel_optativas = sheet.worksheet(caminho_optativas)

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
