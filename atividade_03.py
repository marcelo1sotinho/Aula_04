from InquirerPy import prompt

codigo = [
    {
    "type": "list",
    "message": "Infome o código:",
    "choices": ["codigo 1", "codigo 2"]
    }
    
]

resultado = prompt(codigo)

# codigo = float(input("Informe o código: "))

# match codigo:
#     case 1:
#         print("Sul")
#     case 2:
#         print("Norte")
#     case 3:
#         print("leste")
#     case 4:
#         print("Oeste")
#     case 5 |6:
#         print("Nordeste")
#     case n if 7 <= n <= 9:
#         print("Sudeste")
#     case 10:
#         print("Centro-Oeste")
#     case 11:
#         print("Noroeste")
#     case _:
#         print('Código Inválido')
    

    
    