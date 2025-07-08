
# 🐚 Mini Shell em Python (com histórico, cd e múltiplos comandos)

Este projeto de um mini interpretador de comandos (shell) em Python, simulando um terminal. Usando chamadas ao sistema como `fork()`, `execvp()`, `wait()`, `read()` e `write()` para executar comandos, além de comandos internos como `cd`, `history` e `exit`.

---

## ✅ Como compilar e rodar

### 🧱 Requisitos:
- Linux ou **WSL (Windows Subsystem for Linux)**
- Python 3 instalado

### 🚀 Executar o shell:
1. Abra o terminal ou o WSL
2. Navegue até a pasta do projeto:

   ```bash
   cd /caminho/do/projeto
   ```

3. Execute com:

   ```bash
   python3 minishell.py
   ```

---

## ⚙️ Chamadas ao sistema utilizadas

| Chamada | Função usada no código | Descrição |
|--------|-------------------------|-----------|
| `fork()` | `os.fork()` | Cria um processo filho |
| `execvp()` | `os.execvp()` | Executa o comando no processo filho |
| `wait()` | `os.wait()` | Processo pai aguarda o término do filho |
| `read()` | `os.read(0, BUFFER_SIZE)` | Lê entrada do usuário diretamente da entrada padrão |
| `write()` | `os.write()` | Escreve diretamente no terminal (stdout ou stderr) |

Todas essas chamadas são de baixo nível e fazem parte da interface POSIX do sistema operacional.

---

## 💻 Exemplos de comandos testados

```bash
/home/usuario > echo Olá Mundo
Ola Mundo

/home/usuario > ls -l
(total de arquivos + lista)

/home/usuario > cat mini_shell.py
(exibe o conteúdo do próprio arquivo)

/home/usuario > cd /tmp
/home/usuario > pwd
/tmp

/home/usuario > history
1: echo Olá Mundo
2: ls -l
3: cat mini_shell.py
4: cd /tmp
5: pwd
6: history

/home/usuario > comando_invalido
Comando não encontrado: comando_invalido

/home/usuario > exit
Saindo do shell...
```

Também é possível executar **vários comandos na mesma linha** usando `;`:

```bash
/home/usuario > echo teste; ls; pwd
```

---

## ⚠️ Limitações conhecidas

- ❌ Não possui **autocompletar** ou **histórico com setas** (como ↑ ↓)
- ❌ Não suporta comandos com encadeamento (`&&`, `||`)
- ❌ Não trata variáveis de ambiente (ex: `$HOME`)
- ⚠️ Só roda em sistemas baseados em Unix, como Linux ou WSL (não compatível com Windows puro)

---

## 📁 Estrutura do código

- `mostrar_prompt()` → Exibe o prompt com o diretório atual
- `ler_comando()` → Lê a entrada do usuário com `os.read()`
- `executar_comando()` → Executa comandos internos (`cd`, `exit`, `history`) ou externos via `fork()`/`execvp()`
- `shell_loop()` → Loop principal que mantém o shell rodando
- `historico` → Lista que armazena os comandos digitados

---

## 👨‍💻 Autor

Este mini shell foi desenvolvido para fins educacionais em uma disciplina de Sistemas Operacionais, com foco em prática de chamadas ao sistema e controle de processos no Linux.
