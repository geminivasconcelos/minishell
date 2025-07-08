import os
import sys

BUFFER_SIZE = 1024
historico = []

def mostrar_prompt():
    cwd = os.getcwd()
    os.write(1, f"{cwd} > ".encode())

def ler_comando():
    try:
        comando = os.read(0, BUFFER_SIZE).decode().strip()
        return comando
    except Exception as e:
        os.write(2, f"Erro ao ler entrada: {str(e)}\n".encode())
        return ""
        
def executar_comando(comando):
    comandos = comando.split(';')

    for cmd in comandos:
        partes = cmd.strip().split()

        if not partes:
            continue

        if partes[0] == "exit":
            os.write(1, b"Saindo do shell...\n")
            sys.exit(0)

        if partes[0] == "cd":
            if len(partes) > 1:
                try:
                    os.chdir(partes[1])
                except FileNotFoundError:
                    os.write(2, f"Diretório não encontrado: {partes[1]}\n".encode())
            else:
                os.write(2, b"Uso: cd <diretorio>\n")
            continue

        if partes[0] == "history":
            for i, h in enumerate(historico):
                os.write(1, f"{i + 1}: {h}\n".encode())
            continue
        try:
            pid = os.fork()
        except OSError as e:
            os.write(2, f"Erro ao criar processo: {os.strerror(e.errno)}\n".encode())
            return

        if pid == 0:
            try:
                os.execvp(partes[0], partes)
            except FileNotFoundError:
                os.write(2, f"Comando não encontrado: {partes[0]}\n".encode())
            except Exception as e:
                os.write(2, f"Erro ao executar comando: {str(e)}\n".encode())
            sys.exit(1)

        else:
            _, status = os.wait()
            if os.WIFEXITED(status):
                exit_code = os.WEXITSTATUS(status)
                if exit_code != 0:
                    os.write(2, f"Processo terminou com código {exit_code}\n".encode())
def shell_loop():
    while True:
        mostrar_prompt()
        comando = ler_comando()
        if comando:
            historico.append(comando)
        executar_comando(comando)
if __name__ == "__main__":
    try:
        shell_loop()  # Inicia o shell
    except KeyboardInterrupt:
        os.write(1, b"\nEncerrando shell com Ctrl+C\n")  # Mensagem se o usuário apertar Ctrl+C
        sys.exit(0)
