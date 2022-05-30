# Crie um decorator que calcule o tempo de execução de uma determinada função
import time
import functools


def timefunc(func):

    @functools.wraps(func)
    def time_closure(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        time_elapsed = time.perf_counter() - start
        print(f"Function: {func.__name__}, Tempo decorrido: {time_elapsed}")
        return result

    return time_closure

# Aplique seu decorator na função abaixo e veja quanto tempo a busca de um mesmo valor em um set e uma lista demoram para serem executadas

@timefunc
def encontrar_item(container, item):
    return item in container

def main():
    tamanho = 100000000
    set_grande = set(range(tamanho))
    lista_grande = list(range(tamanho))
    item = 500399
    encontrar_item(set_grande, item)
    encontrar_item(lista_grande, item)



if __name__ == '__main__':
    main()