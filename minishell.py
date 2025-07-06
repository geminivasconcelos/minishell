import os # Importa o módulo para chamadas ao sistema (fork, execvp, wait, read, write)
import sys # Importa para poder usar sys.exit()

BUFFER_SIZE = 1024  # Define o tamanho máximo de bytes que serão lidos da entrada (teclado)

def mostrar_prompt():
    os.write(1, b'> ')  # Escreve o símbolo do prompt na saída padrão (1 = stdout(stdout = saída padrão))
    #os.write(fd, bytes): escreve bytes em um descritor de arquivo. Aqui, está escrevendo na saída padrão (1).

def ler_comando():
    try:
        comando = os.read(0, BUFFER_SIZE).decode().strip()  # Lê da entrada padrão (0 = stdin)
        return comando
    except Exception as e:
        os.write(2, f"Erro ao ler entrada: {str(e)}\n".encode())   # Escreve o erro no stderr (2)
        return ""

    # os.read(0, BUFFER_SIZE): lê diretamente do teclado (entrada padrão).
    # decode() converte de bytes para string.
    # strip() remove espaços em branco do começo e fim.
    # Se houver erro, mostra mensagem amigável no terminal e retorna string vazia.



def executar_comando(comando):
    partes = comando.strip().split()
    if not partes:
        return

    if partes[0] == "exit":
        os.write(1, b"Saindo do shell...\n")
        sys.exit(0)

    try:
        pid = os.fork()
    except OSError as e:
        os.write(2, f"Erro ao criar processo: {os.strerror(e.errno)}\n".encode())
        return

    if pid == 0:
        # Processo filho
        try:
            os.execvp(partes[0], partes)
        except FileNotFoundError:
            os.write(2, f"Comando não encontrado: {partes[0]}\n".encode())
        except Exception as e:
            os.write(2, f"Erro ao executar comando: {str(e)}\n".encode())
        sys.exit(1)
    else:
        # Processo pai
        _, status = os.wait()
        if os.WIFEXITED(status):
            exit_code = os.WEXITSTATUS(status)
            if exit_code != 0:
                os.write(2, f"Processo terminou com código {exit_code}\n".encode())

def shell_loop():
    while True:
        mostrar_prompt()
        comando = ler_comando()
        executar_comando(comando)

if __name__ == "__main__":
    try:
        shell_loop()
    except KeyboardInterrupt:
        os.write(1, b"\nEncerrando shell com Ctrl+C\n")
        sys.exit(0)
