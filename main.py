while True: 
    print('=== CONTROLE DE ESTOQUE ===\n')
    print('[1] Cadastrar produtos')
    print('[2] Listar produtos')
    print('[0] Sair\n')
    opcao = input('Digite a opção: ')

    while opcao not in ('0', '1', '2'):
        opcao = input('Opção inválida, Digite novamente: ')        

    if opcao == '1':
        print('Cadastro de produtos em desenvolvimento.')
    elif opcao == '2':
        print('Consulta de produtos em desenvolvimento.')
    else:
        print('Programa encerrado!')
        break
