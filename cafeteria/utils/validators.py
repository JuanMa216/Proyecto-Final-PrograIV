def validar_campos(*campos):
    return all(campo.strip() != "" for campo in campos)