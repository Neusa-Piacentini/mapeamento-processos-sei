"""Perfil do estudo de caso SEI-480002/001314/2024 (fiscalização programada 2024 da Águas do Rio 1, AGENERSA/CASAN).

Mesmo órgão do caso de referência: herda todos os valores de rj_agenersa.py (calendário, unidades, custo-hora,
regras) e muda só o escopo — um processo único, código P06 do catálogo. Uso: export PERFIL=rj_agenersa_caso_001314"""
import importlib.util
from pathlib import Path

_arq = Path(__file__).with_name("rj_agenersa.py")
_spec = importlib.util.spec_from_file_location("perfil_rj_agenersa_base", _arq)
_base = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_base)
globals().update({k: v for k, v in vars(_base).items() if not k.startswith("__")})

DESCRICAO_BASE = "processo único SEI-480002/001314/2024 (Pesquisa Pública do SEI-RJ, coletado em 04/11/2026)"
CODIGOS_FASE3 = ["P06"]  # só o código do processo estudado
FAMILIA_BENCHMARK = {"P06": "fiscalizacao"}  # reaproveita os casos verificados do caso de referência (mesma família)
# estudo de caso único: o processo entra na coorte da fase 2 (procedimento.py o marca como "estudo de caso")
MIN_CASOS_COORTE = 1
