#!/usr/bin/env python3
"""Criar um ambiente virtual Python e instalar as dependências do requirements.txt."""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
PYTHON3_DIR = Path(__file__).resolve().parent
REQUIREMENTS_FILE = PYTHON3_DIR / "requirements.txt"
GITIGNORE_FILE = REPO_ROOT / ".gitignore"


def print_explanation() -> None:
    print("\n=== Ambiente virtual Python (venv) ===\n")
    print(
        "Um ambiente virtual (venv) isola as dependências do projeto de outras instalações "
        "do Python no sistema. Isso evita conflitos e permite usar versões específicas "
        "de pacotes apenas para este projeto."
    )
    print()
    print("Como criar manualmente:")
    print("  python3 -m venv <nome_do_venv>")
    print("  source <nome_do_venv>/bin/activate")
    print("  python -m pip install -r python3/requirements.txt")
    print()
    print("Para usar uma versão específica do Python instalada no sistema:")
    print("  python3.11 -m venv python3/<nome_do_venv>")
    print("  python3.12 -m venv python3/<nome_do_venv>")
    print("  python3.13 -m venv python3/<nome_do_venv>")
    print()
    print(
        "Se você não tiver a versão desejada instalada, instale-a pelo gerenciador do sistema "
        "ou use pyenv / conda. O importante é executar o módulo venv com o Python correto."
    )
    print()
    print("Este script cria o venv no diretório python3/ e também adiciona o caminho ao .gitignore.")
    print(
        "Você pode instalar as dependências depois com: python -m pip install -r python3/requirements.txt"
    )
    print("Assim, seu ambiente local não será versionado acidentalmente.\n")


def ask_yes_no(prompt: str, default: bool = False) -> bool:
    yes = {"s", "sim", "y", "yes"}
    no = {"n", "nao", "não", "no"}
    default_label = "S/n" if default else "s/N"
    answer = input(f"{prompt} [{default_label}] ").strip().lower()
    if not answer:
        return default
    if answer in yes:
        return True
    if answer in no:
        return False
    print("Resposta inválida. Use 's' ou 'n'.")
    return ask_yes_no(prompt, default=default)


def normalize_env_name(name: str) -> str:
    value = name.strip()
    if not value:
        raise ValueError("O nome do ambiente virtual não pode estar vazio.")
    if value.startswith("/") or value.startswith(".") or ".." in value or "/" in value or "\\" in value:
        raise ValueError(
            "Use apenas um nome simples para o ambiente virtual, sem caminhos ou caracteres especiais."
        )
    return value


def ensure_gitignore_entry(relative_path: str) -> bool:
    entry = relative_path.rstrip("/") + "/"
    if not GITIGNORE_FILE.exists():
        GITIGNORE_FILE.write_text("# .gitignore criado automaticamente\n", encoding="utf-8")

    lines = GITIGNORE_FILE.read_text(encoding="utf-8").splitlines()
    if entry in [line.strip() for line in lines if line.strip() and not line.strip().startswith("#")]:
        return False

    with GITIGNORE_FILE.open("a", encoding="utf-8", newline="\n") as handle:
        if lines and lines[-1].strip() != "":
            handle.write("\n")
        handle.write(f"# Ignorar ambiente virtual local criado por python3/setup_venv.py\n")
        handle.write(f"{entry}\n")
    return True


def get_venv_python(venv_path: Path) -> Path:
    candidates = [venv_path / "bin" / "python", venv_path / "Scripts" / "python.exe"]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    raise FileNotFoundError("Não foi possível encontrar o executável Python dentro do venv.")


def run_command(command: list[str], cwd: Path | None = None) -> None:
    print(f"Executando: {' '.join(command)}")
    subprocess.run(command, cwd=cwd, check=True)


def create_venv(venv_path: Path) -> None:
    print(f"Criando ambiente virtual em: {venv_path}")
    run_command([sys.executable, "-m", "venv", str(venv_path)])


def install_requirements(venv_path: Path) -> None:
    if not REQUIREMENTS_FILE.exists():
        print(f"Arquivo de requisitos não encontrado: {REQUIREMENTS_FILE}")
        return
    python_bin = get_venv_python(venv_path)
    print("Atualizando pip dentro do ambiente virtual...")
    run_command([str(python_bin), "-m", "pip", "install", "--upgrade", "pip"])
    print(f"Instalando dependências de {REQUIREMENTS_FILE}...")
    run_command([str(python_bin), "-m", "pip", "install", "-r", str(REQUIREMENTS_FILE)])


def main() -> None:
    print_explanation()

    if not ask_yes_no("Deseja criar um ambiente virtual Python agora no diretório python3/ ?", default=False):
        print("Nenhum ambiente virtual foi criado. Execute manualmente se desejar.")
        return

    try:
        env_name = normalize_env_name(input("Digite o nome do ambiente virtual (por exemplo .venv, venv, meu_venv): ").strip())
    except ValueError as exc:
        print(f"Erro: {exc}")
        sys.exit(1)

    env_path = PYTHON3_DIR / env_name
    if env_path.exists():
        if ask_yes_no(f"O diretório {env_path} já existe. Deseja recriar o ambiente?", default=False):
            print(f"Removendo {env_path}...")
            shutil.rmtree(env_path)
        else:
            print("Usando o ambiente existente.")

    try:
        create_venv(env_path)
    except subprocess.CalledProcessError as exc:
        print(f"Falha ao criar o ambiente virtual: {exc}")
        sys.exit(1)

    try:
        install_requirements(env_path)
    except subprocess.CalledProcessError as exc:
        print(f"Falha ao instalar dependências: {exc}")
        sys.exit(1)

    relative_path = env_path.relative_to(REPO_ROOT).as_posix()
    if ensure_gitignore_entry(relative_path):
        print(f"Adicionado {relative_path}/ ao .gitignore")
    else:
        print(f"O caminho {relative_path}/ já estava no .gitignore.")

    print("\nAmbiente virtual criado e configurado com sucesso.")
    print("Para ativar o ambiente no Linux/macOS, execute:")
    print(f"  source {relative_path}/bin/activate")
    print("Para sair, use: deactivate")


if __name__ == "__main__":
    main()
