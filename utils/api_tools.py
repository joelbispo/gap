from enum import Enum


ERROR_MESSAGE = {
    'EMAIL_NOT_FOUND': 'Este E-mail não está cadastrado',
    'INVALID_PASSWORD': 'Senha incorreta'
}


def error_formatter(message):
    return ERROR_MESSAGE.get(message, 'Desculpa, algo deu errado')
