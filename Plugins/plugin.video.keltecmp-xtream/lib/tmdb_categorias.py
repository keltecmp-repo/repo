# -*- coding: utf-8 -*-
"""
TMDB - Categorias especiais (KelTec Media Play)
================================================
Novelas, Novelas Turcas, Doramas (dramas asiaticos) e Animes, puxados
diretamente do TMDB (endpoint discover/tv), SEMPRE comecando pelos
lancamentos mais recentes (first_air_date.desc, ate a data de hoje).

Este arquivo e independente de lib/tmdb_browser.py de proposito: a rotina de
atualizacao do addon sobrescreve o tmdb_browser.py, entao a logica nova mora
aqui e usa apenas os metodos publicos/estaveis do TMDBBrowser (_get e _norm).

Marcador: KELTEC-TMDB-CATEGORIAS
"""

import datetime

# Filtros comuns: lancamentos primeiro, sem datas futuras/nulas
_BASE = {
    'sort_by': 'first_air_date.desc',
    'include_null_first_air_dates': 'false',
}

# Genero TMDB: 18 = Drama, 16 = Animacao, 10766 = Novela (Soap)
_ORIGENS_DORAMA = ('KR', 'JP', 'CN', 'TW', 'TH')   # Coreia, Japao, China, Taiwan, Tailandia

CATEGORIAS = [
    {
        'mode':   'tmdb_cat_novelas',
        'titulo': 'Novelas',
        'cor':    'hotpink',
        'plot':   'Novelas brasileiras direto do TMDB, dos lancamentos mais recentes para os mais antigos.',
        # Novelas (genero Soap) com origem Brasil
        'fontes': [
            {'with_genres': '10766', 'with_origin_country': 'BR'},
        ],
    },
    {
        'mode':   'tmdb_cat_novelas_turcas',
        'titulo': 'Novelas Turcas',
        'cor':    'crimson',
        'plot':   'Novelas e dizis turcas direto do TMDB, dos lancamentos mais recentes para os mais antigos.',
        # Origem Turquia, idioma turco, genero Drama OU Novela (pipe = OR no TMDB)
        'fontes': [
            {'with_origin_country': 'TR', 'with_original_language': 'tr',
             'with_genres': '18|10766'},
        ],
    },
    {
        'mode':   'tmdb_cat_doramas',
        'titulo': 'Doramas - Dramas Asiaticos',
        'cor':    'violet',
        'plot':   'Doramas e dramas asiaticos (Coreia, Japao, China, Taiwan e Tailandia) direto do TMDB, '
                  'dos lancamentos mais recentes para os mais antigos.',
        # Uma fonte por pais (o resultado e juntado e reordenado por data).
        # without_genres=16 tira animacao, que fica na categoria Animes.
        'fontes': [
            {'with_genres': '18', 'with_origin_country': _pais, 'without_genres': '16'}
            for _pais in _ORIGENS_DORAMA
        ],
    },
    {
        'mode':   'tmdb_cat_animes',
        'titulo': 'Animes',
        'cor':    'orange',
        'plot':   'Animes (animacao de origem japonesa) direto do TMDB, dos lancamentos mais recentes '
                  'para os mais antigos.',
        'fontes': [
            {'with_genres': '16', 'with_original_language': 'ja'},
        ],
    },
]

POR_MODE = {c['mode']: c for c in CATEGORIAS}
MODES = tuple(POR_MODE.keys())


def menu_items(icon=''):
    """Itens de menu (um por categoria) para anexar ao menu TMDB."""
    itens = []
    for c in CATEGORIAS:
        itens.append({
            'title':  f"[COLOR {c['cor']}][B]>> {c['titulo']}[/B][/COLOR]  "
                      f"[COLOR dimgray]Lancamentos primeiro[/COLOR]",
            'plot':   c['plot'],
            'mode':   c['mode'],
            'icon':   icon,
            'folder': True,
        })
    return itens


def listar(browser, mode, page=1):
    """
    Busca uma pagina da categoria no TMDB.
    Retorna (lista_de_itens_normalizados, total_de_paginas).
    Itens no mesmo formato de TMDBBrowser.get_tv() (prontos para
    build_tv_items_with_metadata).
    """
    cat = POR_MODE.get(mode)
    if not cat or not browser:
        return [], 1

    hoje = datetime.date.today().strftime('%Y-%m-%d')
    vistos, brutos, total = set(), [], 1

    for fonte in cat['fontes']:
        params = dict(_BASE)
        params['first_air_date.lte'] = hoje
        params.update(fonte)
        params['page'] = page
        data = browser._get('discover/tv', params)
        if not data:
            continue
        try:
            total = max(total, int(data.get('total_pages', 1) or 1))
        except (TypeError, ValueError):
            pass
        for t in data.get('results', []):
            tid = t.get('id')
            if not tid or tid in vistos or not t.get('poster_path'):
                continue
            vistos.add(tid)
            brutos.append(t)

    # Junta as fontes (ex.: paises dos doramas) e garante lancamentos primeiro
    brutos.sort(key=lambda t: t.get('first_air_date') or '', reverse=True)
    return [browser._norm(t) for t in brutos], min(total, 500)
