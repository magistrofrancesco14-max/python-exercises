# Un numero perfetto è un numero naturale uguale alla somma dei suoi divisori positivi, escluso sé stesso. 
# Scrivi una funzione che verifichi se un numero è perfetto oppure no.

def is_perfect_number(n):
    if n < 2:
        return False
    
    divisors_sum = 1  # Iniziamo con 1, che è un divisore di tutti i numeri
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:  # Aggiungiamo anche il divisore complementare se è diverso
                divisors_sum += n // i
    
    return divisors_sum == n