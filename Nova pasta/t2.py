def verifica_fibonacci_usuario():
    n = int(input("Informe um número para verificar se pertence à sequência: "))
    
    fib_seq = [0, 1]
    
    while fib_seq[-1] < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    
    if n in fib_seq:
        print(f"O número {n} pertence à sequência.")
    else:
        print(f"O número {n} não pertence à sequência.")

verifica_fibonacci_usuario()
