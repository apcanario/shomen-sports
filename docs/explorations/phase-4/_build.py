#!/usr/bin/env python3
"""Assemble the three Phase 4 layout variants from shared content fragments.

    python docs/explorations/phase-4/_build.py

Content (products, thumbnails, athletes, headings, Compromisso copy) is verbatim from Phase 3
and lives once, here; each variant only changes section order, hero type, product pattern,
athlete pattern, nav and where the display moment sits.
"""
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
A = "../../../assets/img/"

# ---------------------------------------------------------------- content
PRODUCTS = [
    {
        "id": "kit", "n": "01", "ref": "KU01", "name": "Kit Kumite Aka + Ao (2 Casacos + 1 Calça)",
        "excerpt": "Kit Kimono de Competição Kumite (Aka + Ao).",
        "tile": ("img_5415", "", "Casaco de kimono de kumite branco Shomen com cinto vermelho, visto de frente"),
        "desc": ["Kit Kimono de Competição Kumite (Aka + Ao). Kimono Ultra Leve, fabricado com materiais topo de gama.",
                 "Inclui: <strong>Casaco Vermelho (Aka), Casaco Azul (Ao), Calças</strong>"],
        "spec": [("Material", "4oz 100% Polyester"), ("Aprovação", "Aprovado para uso em todas as provas FNK-P.")],
        "sizes": ["150", "155", "160", "165", "170", "175", "180", "185", "190"],
        "sizeinfo": ["<strong>Informação de Tamanhos:</strong>",
                     "O Kimono é verdadeiro à sua altura, com um corte relaxado e casaco comprido. Para um corte slim-fit ou casaco mais curto, escolha o tamanho abaixo. Por exemplo, se medir 178cm recomendamos o tamanho 180 para um corte relaxado e o tamanho 175 para um corte mais cintado."],
        "subject": "Kit%20Kumite%20Aka%20%2B%20Ao%20(REF.%20KU01)",
        "photos": [
            ("img_5415", "jpg", "", 800, 1200, "Casaco de kimono de kumite branco Shomen com cinto vermelho, visto de frente"),
            ("processed_dc9eaefadaf14dd7a26b86563fd0d076", "jpeg", "", 800, 1161, "Atleta de perfil com o kimono de kumite Shomen, cinto vermelho e luvas vermelhas"),
            ("img_5612", "jpg", "", 800, 1200, "Atleta de costas com o kimono de kumite Shomen e cinto vermelho"),
            ("img_5550", "jpg", "", 800, 1200, "Atleta em posição de guarda com o kimono de kumite Shomen e luvas vermelhas"),
            ("img_5796", "jpg", "", 800, 1200, "Kimonos Shomen com as letras bordadas a vermelho e a azul, com cintos vermelho e azul"),
            ("img_5570", "jpg", "", 800, 1200, "Atleta a executar um pontapé com o kimono de kumite Shomen"),
            ("img_5632", "jpg", "", 800, 1200, "Pormenor das letras Shomen bordadas a azul no ombro do casaco"),
            ("img_5512", "jpg", "", 800, 533, "Pormenor do cinto vermelho e da luva vermelha sobre o kimono Shomen"),
            ("processed_8f9180724d1d467d9e040940591ac946", "jpeg", "", 800, 1200, "Casaco de kimono Shomen com cinto azul e letras bordadas a azul no ombro"),
            ("img_5536", "jpg", "", 800, 533, "Pormenor do ombro do casaco com as letras Shomen bordadas a vermelho"),
            ("img_5495", "jpg", "", 800, 533, "Pormenor das calças do kimono Shomen e de uma proteção de pé vermelha"),
            ("img_5480", "jpg", "", 800, 533, "Costas do casaco de kimono Shomen com o logótipo bordado a vermelho na nuca"),
            ("img_5820", "jpg", "", 800, 1200, "Pormenor do logótipo Shomen bordado a azul no tecido do kimono"),
            ("img_5811", "jpg", "", 800, 1200, "Pormenor das letras Shomen bordadas a azul na manga do kimono"),
            ("img_5721", "jpg", "", 800, 1200, "Pormenor do logótipo Shomen bordado a vermelho no tecido do kimono"),
            ("img_5526", "jpg", "", 800, 533, "Atleta com o kimono Shomen a segurar uma luva vermelha"),
            ("processed_02af34c87ba34c368e00a2afd5454093", "jpeg", "", 800, 1067, "Casaco de kimono Shomen com cinto azul, visto de frente"),
            ("processed_c76006b78dc3481c9e852b006b37e263", "jpeg", "", 800, 1200, "Pormenor da gola e do logótipo Shomen bordado a azul nas costas do casaco"),
        ],
    },
    {
        "id": "cintos", "n": "02", "ref": "BE01", "name": "Conjunto 2 Cintos (Aka + Ao)",
        "excerpt": "Conjunto de Cintos Kumite Aka + Ao (Azul + Vermelho)",
        "tile": ("img_5771", "", "Cintos de kumite azul e vermelho Shomen sobre um kimono branco"),
        "desc": ["Conjunto de Cintos Kumite Aka + Ao (Azul + Vermelho)"],
        "spec": [], "sizes": ["280cm", "300cm"], "sizeinfo": [],
        "subject": "Conjunto%202%20Cintos%20(REF.%20BE01)",
        "photos": [
            ("img_5771", "jpg", "", 800, 1200, "Cintos de kumite azul e vermelho Shomen sobre um kimono branco"),
            ("20250913_1801521", "jpg", "", 765, 765, "Cinto vermelho Shomen com etiqueta bordada"),
            ("20250913_1801181-min", "jpg", "", 800, 800, "Cinto azul Shomen com etiqueta bordada"),
            ("img_5651", "jpg", "", 800, 1200, "Cinto azul Shomen atado sobre o kimono, com a etiqueta visível"),
            ("img_5423", "jpg", "", 800, 1200, "Cinto vermelho atado sobre o kimono Shomen, com a etiqueta Shomen Portugal"),
            ("img_5769", "jpg", "", 800, 1200, "Cintos azul e vermelho Shomen com etiquetas bordadas, sobre um kimono"),
        ],
    },
    {
        "id": "corta-vento", "n": "03", "ref": "CV01", "name": "Corta Vento Colapsável",
        "excerpt": "Ideal para aquecimento e viagens.",
        "tile": ("img_5352", "pos-top", "Atleta com o corta-vento preto Shomen com capuz, visto de frente"),
        "desc": ["<!-- TODO: typo? Leve -->Corta Vento Ultra Level, Colapsável. Ideal para aquecimento e viagens."],
        "spec": [], "sizes": [], "sizeinfo": [],
        "subject": "Corta%20Vento%20Colaps%C3%A1vel%20(REF.%20CV01)",
        "photos": [
            ("img_5352", "jpg", "pos-top", 800, 1200, "Atleta com o corta-vento preto Shomen com capuz, visto de frente"),
            ("img_5363", "jpg", "", 800, 533, "Pormenor do logótipo Shomen a vermelho no peito do corta-vento"),
            ("img_5377", "jpg", "", 800, 1200, "Atleta a executar um pontapé com o corta-vento Shomen e luvas vermelhas"),
            ("img_5349", "jpg", "", 800, 533, "Pormenor do logótipo e da palavra Shomen a vermelho no corta-vento preto"),
            ("img_5386", "jpg", "", 800, 1200, "Atleta em posição de guarda com o corta-vento Shomen e luvas vermelhas"),
            ("img_5389", "jpg", "", 800, 533, "Pormenor do tecido preto do corta-vento Shomen"),
        ],
    },
    {
        "id": "tshirt", "n": "04", "ref": "TS02", "name": "T-Shirt Técnica Preta",
        "excerpt": "T-Shirt Técnica ultra leve para treino.",
        "tile": ("img_5312", "pos-top", "Atleta com a t-shirt técnica preta Shomen, com o logótipo bordado a vermelho no peito"),
        "desc": ["T-Shirt Técnica ultra leve para treino.", "Logotipo Bordado para facilidade nas lavagens."],
        "spec": [("Tecido", "Polyester")], "sizes": [], "sizeinfo": [],
        "subject": "T-Shirt%20T%C3%A9cnica%20Preta%20(REF.%20TS02)",
        "photos": [
            ("img_5312", "jpg", "pos-top", 800, 1200, "Atleta com a t-shirt técnica preta Shomen, com o logótipo bordado a vermelho no peito"),
            ("img_5300", "jpg", "", 800, 1200, "Atleta de frente com a t-shirt técnica preta Shomen"),
            ("img_5321", "jpg", "", 800, 1200, "Atleta de costas com a t-shirt técnica preta Shomen"),
        ],
    },
]

ATHLETES = [
    {
        "id": "leonor-goncalves", "n": "01", "key": "red", "first": "Leonor", "last": "Gonçalves", "tag": "WKF // KUMITE",
        "photo": ("whatsapp-image-2025-10-30-at-11.12.51_52007c1a", "", 800, 1029, 896, "Leonor Gonçalves de braços cruzados, com kimono Shomen e cinto vermelho"),
        "wins": [("#1", 'WKF Ranking Junior <span class="mono">-53kg</span>'), ("#1", 'WKF Ranking All Time Cadete <span class="mono">-54kg</span>'),
                 ("7x", "Vencedora Karate1 Youth League"), ("5º", "Lugar Campeonato do Mundo WKF"),
                 ("7x", "Campeã Nacional FNK-P"), ("2x", "Vencedora Taça de Portugal FNK-P")],
        "handle": ("leonordsgonc", "https://www.instagram.com/leonordsgonc"),
    },
    {
        "id": "andre-aguiar", "n": "02", "key": "blue", "first": "André", "last": "Aguiar", "tag": "WKF // KUMITE",
        "photo": ("whatsapp-image-2025-10-29-at-23.29.41_64179326", "pos-top", 800, 1429, 896, "André Aguiar de fato azul a segurar um troféu"),
        "wins": [("", 'Vencedor Karate1 Youth League Guadalajara <span class="mono">2025</span> Cadete <span class="mono">+70kg</span>'),
                 ("", 'Medalhista Karate1 Youth League Monterrey <span class="mono">2025</span> Junior <span class="mono">+76kg</span>'),
                 ("", "Campeão Nacional FNK-P"), ("2x", "Vencedor da Taça de Portugal FNK-P"), ("", "Vencedor Taça da Liga FNK-P")],
        # Instagram URL taken from the old site; the rebuild brief listed https://www.instagram.com/aguiar05./
        # TODO: confirm André's Instagram handle (_aguiar05._ on the old site vs aguiar05. in the brief)
        "handle": ("_aguiar05._", "https://www.instagram.com/_aguiar05._/"),
    },
    {
        "id": "martim-sa", "n": "03", "key": "red", "first": "Martim", "last": "Sá", "tag": "",
        "photo": ("whatsapp-image-2025-10-29-at-08.45.16_3fd8c6dc", "pos-top", 800, 1067, 1200, "Martim Sá em cima do tatami, com o corta-vento Shomen e o punho levantado"),
        "wins": [("5º", 'Lugar Open Lisboa <span class="mono">2025</span>')],
        "handle": None,  # TODO: Martim's Instagram (the old site linked Leonor's profile here by mistake)
    },
]

RETICLE = '<svg class="reticle" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8"/><g class="reticle__arms"><line x1="12" y1="0" x2="12" y2="5"/><line x1="12" y1="19" x2="12" y2="24"/><line x1="0" y1="12" x2="5" y2="12"/><line x1="19" y1="12" x2="24" y2="12"/></g><circle class="reticle__dot" cx="12" cy="12" r="1.5"/></svg>'

TICKER_SPAN = '<span class="micro micro--white"><span>SHOMEN</span><i>//</i><span>KARATE</span><i>//</i><span>PORTUGAL</span><i>//</i><span>KUMITE</span><i>//</i><span>FNK-P</span><i>//</i><span>WKF</span><i>//</i><span class="mono">EST. 2025</span><i>//</i><span>TEAM SHOMEN</span><i>//</i><span>AKA</span><i>//</i><span>AO</span><i>//</i></span>'


# ---------------------------------------------------------------- fragments
def head(title, extra_css):
    return f"""<!DOCTYPE html>
<html lang="pt-PT">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="robots" content="noindex">
  <link rel="stylesheet" href="_base.css">
  <style>
{extra_css}
  </style>
</head>
"""


def nav(rail=False):
    cls = "nav nav--rail" if rail else "nav"
    lcls = "nav__list nav__list--rail" if rail else "nav__list"
    return f"""  <a class="skip-link" href="#conteudo">Saltar para o conteúdo</a>
  <div class="progress" aria-hidden="true"></div>
  <header class="{cls}" id="top">
    <div class="wrap nav__inner" data-reveal>
      <a class="nav__logo" href="#top"><img src="{A}originals/union.png" width="960" height="216" alt="Shomen Sports, início da página"></a>
      <button class="nav__toggle" type="button" aria-expanded="false" aria-controls="nav-menu"><span class="nav__toggle-label">Menu</span></button>
    </div>
    <nav class="nav__menu" id="nav-menu" aria-label="Navegação principal">
      <ul class="{lcls}">
        <li style="--i: 0"><a class="nav__link" href="#top" aria-current="true" data-spy="top">Início</a></li>
        <li style="--i: 1"><a class="nav__link" href="#produtos" data-spy="produtos">Produtos</a></li>
        <li style="--i: 2"><a class="nav__link" href="#atletas" data-spy="atletas">Atletas</a></li>
        <li style="--i: 3"><a class="nav__link" href="#contacto" data-spy="contacto">Contacto</a></li>
        <li class="nav__dot" aria-hidden="true"></li>
      </ul>
      <div class="nav__menu-foot">
        <p class="micro">SHOMEN // KARATE // PORTUGAL</p>
        <a class="handle" href="https://instagram.com/shomen_sports" rel="noopener">@shomen_sports</a>
      </div>
    </nav>
  </header>
"""


HERO_TITLE = """<h1 id="hero-title" class="hero__title">
            <span><span class="w" style="--i: 0">OS</span> <span class="w" style="--i: 1">CAMPEÕES</span></span>
            <span><span class="w" style="--i: 2">DE</span> <span class="w" style="--i: 3">AMANHÃ</span></span>
            <span><span class="w" style="--i: 4">COMEÇAM</span> <span class="w key" style="--i: 5">HOJE</span></span>
          </h1>"""

HERO_MICRO = """<ul class="microbar microbar--start">
            <li><p class="micro micro--dot micro--white" data-reveal data-type style="--i: 1">SHOMEN // KARATE // PORTUGAL</p></li>
            <li><p class="micro" data-reveal data-type style="--i: 2"><span class="mono">EST. 2025</span></p></li>
          </ul>"""

HERO_FOOT = """<div class="hero__foot">
            <div class="actions" data-reveal style="--i: 4">
              <a class="btn btn--primary" href="#produtos">Ver produtos</a>
              <a class="btn" href="#atletas">Conhecer os atletas</a>
            </div>
            <div class="hero__readouts" data-reveal style="--i: 5">
              <div class="readout readout--end readout--sm"><p class="micro readout__label">Atletas apoiados</p><p class="readout__value" data-settle>03</p></div>
              <div class="readout readout--end"><p class="micro readout__label">Est.</p><p class="readout__value" data-settle>2025</p></div>
            </div>
          </div>"""

HERO_IMG = f'<img src="{A}img_5512-1600.webp" srcset="{A}img_5512-800.webp 800w, {A}img_5512-1600.webp 1600w" sizes="100vw" width="1600" height="1067" fetchpriority="high" alt="Pormenor de um kimono de kumite branco Shomen com cinto vermelho e luva vermelha">'


def hero_full():
    return f"""    <section class="hero" aria-labelledby="hero-title">
      <div class="photo hero__photo" data-parallax="0.28" data-mouse>{HERO_IMG}</div>
      <div class="hero__scrim" aria-hidden="true"></div>
      <div class="hero__glow" aria-hidden="true"></div>
      <p class="hero__vword" aria-hidden="true">Shomen</p>
      <div class="hero__ruler" aria-hidden="true"></div>
      <div class="wrap hero__content">
        <div class="stack stack--lg">
          {HERO_MICRO}
          {HERO_TITLE}
          {HERO_FOOT}
        </div>
      </div>
    </section>
"""


def hero_split():
    return f"""    <section class="hero hero--split" aria-labelledby="hero-title">
      <div class="hero__glow" aria-hidden="true"></div>
      <div class="wrap hero__grid">
        <div class="hero__content">
          {HERO_MICRO}
          {HERO_TITLE}
          {HERO_FOOT}
        </div>
        <div class="hero__side">
          <p class="hero__vword" aria-hidden="true">Shomen</p>
          <div class="photo hero__photo photo--vignette" data-parallax="0.18" data-mouse>{HERO_IMG}</div>
        </div>
      </div>
    </section>
"""


def ticker():
    return f"""    <div class="ticker" aria-hidden="true">
      <div class="ticker__track">{TICKER_SPAN}{TICKER_SPAN}</div>
    </div>
"""


def compromisso(sec="01", display=False):
    aside = ('<div class="readout readout--display" data-reveal="right"><p class="micro readout__label">Atletas apoiados</p><p class="readout__value" data-settle>03</p></div>'
             if display else '<div class="readout"><p class="micro readout__label">Atletas apoiados</p><p class="readout__value" data-settle>03</p></div>')
    return f"""    <!-- TODO: copy for Pedro's review (Phase 3 draft: no prize-money claim; focus on equipment quality and the next generation) -->
    <section class="section section--tight" id="compromisso" aria-labelledby="compromisso-title">
      <div class="wrap">
        <div class="panel" data-reveal>
          <div class="panel__head">
            <p class="micro micro--dot" data-type>O NOSSO COMPROMISSO</p>
            <p class="micro"><span class="mono">SEC. {sec}</span></p>
          </div>
          <div class="fact">
            <div class="fact__copy">
              <h2 id="compromisso-title" class="h2--band">Equipamento de competição para a próxima geração de campeões</h2>
              <hr class="rule rule--key">
              <p>A Shomen Sports nasceu em 2025, em Portugal, criada por atletas para atletas.</p>
              <div class="more" id="compromisso-more" hidden>
                <div>
                  <p>O nosso compromisso é produzir equipamento de kumite de alta qualidade, aprovado para competição, para que cada jovem atleta suba ao tatami com o material que o seu talento merece.</p>
                  <p>Apoiamos uma equipa de jovens atletas de nível de seleção nacional e trabalhamos para envolver e fazer crescer a próxima geração de campeões do karate português.</p>
                </div>
              </div>
              <button class="link-btn" type="button" aria-expanded="false" aria-controls="compromisso-more" data-toggle="compromisso-more" data-labels="Ler mais|Ler menos"><span>Ler mais</span></button>
            </div>
            <div class="fact__aside">
              {aside}
              {RETICLE}
            </div>
          </div>
        </div>
      </div>
    </section>
"""


def tile(p, i, extra=""):
    f, cls, alt = p["tile"]
    cls = f' class="{cls}"' if cls else ""
    return f"""          <li class="panel panel--flush panel--hover tile" data-reveal style="--i: {i}">
            <button class="tile__btn" type="button" data-product="{p['id']}" aria-expanded="false" aria-controls="prod-{p['id']}">
              <div class="photo zoom"><img{cls} src="{A}{f}-800.webp" srcset="{A}{f}-800.webp 800w, {A}{f}-1600.webp 1600w" sizes="(min-width: 1280px) 290px, (min-width: 720px) 24vw, 45vw" width="800" height="1200" loading="lazy" alt="{alt}"></div>
              <div class="tile__body">
                <p class="tile__ref"><span>REF. {p['ref']}</span><span class="open"><span>ABRIR</span> →</span></p>
                <h3 class="tile__name">{p['name']}</h3>
                <p class="tile__excerpt">{p['excerpt']}</p>
              </div>
            </button>
          </li>
"""


def product(p, mode, display_ref=False):
    f0, ext0, cls0, w0, h0, alt0 = p["photos"][0]
    cls0 = f' class="{cls0}"' if cls0 else ""
    thumbs = ""
    for j, (f, ext, cls, w, h, alt) in enumerate(p["photos"]):
        cur = ' aria-current="true"' if j == 0 else ""
        cls = f' class="{cls}"' if cls else ""
        thumbs += f'              <li><button type="button"{cur} data-src="{A}{f}-1600.webp" data-full="{A}originals/{f}.{ext}" data-alt="{alt}"><span class="photo"><img{cls} src="{A}{f}-800.webp" width="{w}" height="{h}" loading="lazy" alt="{"" if j == 0 else alt}"></span></button></li>\n'
    n = len(p["photos"])
    gal = f'            <button class="link-btn" type="button" data-gallery><span>Ver galeria completa (<span class="mono">{n:02d}</span>)</span></button>\n' if n > 6 else ""
    desc = "".join(f"<p>{d}</p>" for d in p["desc"])
    spec = ""
    if p["spec"]:
        spec = '<div class="spec">' + "".join(f'<div class="readout readout--text"><p class="micro readout__label">{k}</p><p class="readout__value">{v}</p></div>' for k, v in p["spec"]) + "</div>"
    sizes = ""
    if p["sizes"]:
        chips = "".join(f'<li class="chip">{s}</li>' for s in p["sizes"])
        info = "".join(f"<p>{s}</p>" for s in p["sizeinfo"])
        sizes = f'<div class="stack"><p class="micro micro--dot">Tamanhos</p><ul class="chips">{chips}</ul>{"<div>" + info + "</div>" if info else ""}</div>'
    close = '' if mode == "tabs" else '<button class="btn btn--ghost btn--sm" type="button" data-close-product>Fechar</button>'
    big = f'<p class="product__display mono" aria-hidden="true">{p["ref"]}</p>' if display_ref else ""
    return f"""        <article class="panel product" id="prod-{p['id']}" data-id="{p['id']}" aria-labelledby="prod-{p['id']}-title" hidden>
          <div class="panel__head">
            <ul class="microbar microbar--start">
              <li><p class="micro micro--dot">Produto // <span class="mono">{p['n']}</span></p></li>
              <li><p class="micro"><span class="mono">REF. {p['ref']}</span></p></li>
            </ul>
            {close}
          </div>
          <div class="product__body">
            <div class="product__gallery">
              <a class="product__main-link" href="{A}originals/{f0}.{ext0}" data-main-link>
                <figure class="photo product__main" data-main><img{cls0} src="{A}{f0}-1600.webp" width="{w0}" height="{h0}" loading="lazy" alt="{alt0}"></figure>
              </a>
              <ul class="thumbs thumbs--short" role="list">
{thumbs}              </ul>
{gal}            </div>
            <div class="product__info">
              {big}
              <h2 class="product__name" id="prod-{p['id']}-title">{p['name']}</h2>
              <p class="product__ref">REF. {p['ref']}</p>
              <div>{desc}</div>
              {spec}
              {sizes}
              <div class="actions">
                <a class="btn btn--primary" href="mailto:info@shomen-sports.com?subject={p['subject']}">Encomendar por email</a>
                <a class="btn" href="https://instagram.com/shomen_sports" rel="noopener">@shomen_sports</a>
              </div>
            </div>
          </div>
        </article>
"""


def produtos(mode="accordion", scroller=False, display_ref=False, align="left"):
    tiles = "".join(tile(p, i) for i, p in enumerate(PRODUCTS))
    prods = "".join(product(p, mode, display_ref) for p in PRODUCTS)
    list_cls = "tiles tiles--scroller" if scroller else "tiles"
    head_cls = "section__head" + (" section__head--end" if align == "right" else "")
    lead = ("Abre cada produto para ver a galeria, a descrição e os tamanhos." if mode == "accordion" else
            "Escolhe um produto para ver a galeria, a descrição e os tamanhos.")
    return f"""    <section class="section" id="produtos" aria-labelledby="produtos-title" data-key="blue">
      <div class="wrap">
        <div class="{head_cls}" data-reveal="{align}">
          <ul class="microbar">
            <li><p class="micro micro--dot" data-type>Equipamento</p></li>
            <li><p class="micro"><span class="mono">04 // KU01 · BE01 · CV01 · TS02</span></p></li>
          </ul>
          <h2 id="produtos-title">Equipa-te para a competição</h2>
          <hr class="rule rule--key">
          <p class="grey">{lead} Para encomendas e informações: <a href="mailto:info@shomen-sports.com">info@shomen-sports.com</a></p>
        </div>
        <ul class="{list_cls}">
{tiles}        </ul>
        <div class="sheet" data-mode="{mode}" aria-hidden="true">
          <div class="sheet__clip">
            <div class="sheet__inner">
{prods}            </div>
          </div>
        </div>
      </div>
    </section>
"""


def strip(label_a="Competição", label_b="Materiais"):
    return f"""    <section class="section section--tight" aria-label="Competição e materiais">
      <div class="wrap strip">
        <div class="panel panel--flush statement" data-reveal="left">
          <div class="photo photo--1x1 parallax" data-parallax="0.1"><img src="{A}img_5811-800.webp" width="800" height="1200" loading="lazy" alt="Pormenor das letras Shomen bordadas a azul na manga de um kimono branco"></div>
          <div class="statement__body">
            <p class="micro micro--dot" data-type>{label_a}</p>
            <h2 class="h2--band">prontos para TODAS AS COMPETIÇÕES<br>FNK-P, OPENS nacionais e internacionais</h2>
            <hr class="rule rule--key">
          </div>
        </div>
        <div class="panel panel--flush statement" data-reveal="right" style="--i: 1">
          <div class="photo photo--1x1 parallax" data-parallax="0.1"><img class="pos-20" src="{A}img_5377-800.webp" width="800" height="1200" loading="lazy" alt="Atleta a executar um pontapé com o corta-vento preto Shomen e luvas vermelhas"></div>
          <div class="statement__body">
            <p class="micro micro--dot" data-type>{label_b}</p>
            <h2 class="h2--band">FABRICADOS COM MATERIAIS DE TOPO DE GAMA,<br>PRONTOS PARA TE LEVAR AO TOPO DO pÓDIO</h2>
            <hr class="rule rule--key">
          </div>
        </div>
      </div>
    </section>
"""


def wins_list(a, start=0, cls="readouts"):
    out = f'<ul class="{cls}">'
    for i, (v, lab) in enumerate(a["wins"][start:]):
        out += f'<li style="--i: {i}"><span class="val">{v}</span><span class="lab">{lab}</span></li>'
    return out + "</ul>"


def athlete_photo(a, sizes):
    f, cls, w, h, w16, alt = a["photo"]
    cls = f' class="{cls}"' if cls else ""
    return f'<img{cls} src="{A}{f}-800.webp" srcset="{A}{f}-800.webp 800w, {A}{f}-1600.webp {w16}w" sizes="{sizes}" width="{w}" height="{h}" loading="lazy" alt="{alt}">'


def handle(a):
    if not a["handle"]:
        return "<!-- TODO: Martim's Instagram (the old site linked Leonor's profile here by mistake) -->"
    h, url = a["handle"]
    note = "<!-- TODO: confirm André's Instagram handle (_aguiar05._ on the old site vs aguiar05. in the brief) -->" if a["id"] == "andre-aguiar" else ""
    return f'{note}<a class="handle" href="{url}" rel="noopener">@{h}</a>'


def atletas_head(align="left", label="TEAM SHOMEN // ÉPOCA 2026/27"):
    cls = "section__head" + (" section__head--end" if align == "right" else "")
    return f"""        <div class="{cls}" data-reveal="{align}">
          <ul class="microbar">
            <li><p class="micro micro--dot" data-type>{label}</p></li>
            <li><p class="micro"><span class="mono">ATLETAS // 03</span></p></li>
          </ul>
          <h2 id="atletas-title">FIca A CONHECER OS NOSSOS ATLETAS</h2>
          <hr class="rule rule--key">
        </div>
"""


def atletas_roster():
    rows = ""
    for i, a in enumerate(ATHLETES):
        rest = len(a["wins"]) - 2
        more = ""
        if rest > 0 or a["handle"]:
            more = f"""            <div class="row__more">
              <div class="more" id="more-{a['id']}" hidden>
                <div>
                  <div class="stack"><p class="micro">Palmarés completo</p>{wins_list(a, 2) if rest > 0 else ""}</div>
                  <div class="stack"><div class="photo photo--4x5 zoom row__big">{athlete_photo(a, "(min-width: 720px) 40vw, calc(100vw - 32px)")}</div>{handle(a)}</div>
                </div>
              </div>
            </div>
"""
        tog = (f'<button class="link-btn row__toggle" type="button" aria-expanded="false" aria-controls="more-{a["id"]}" data-toggle="more-{a["id"]}" data-labels="+ {rest:02d}|Fechar"><span>+ {rest:02d}</span></button>' if rest > 0
               else (f'<button class="link-btn row__toggle" type="button" aria-expanded="false" aria-controls="more-{a["id"]}" data-toggle="more-{a["id"]}" data-labels="Ver|Fechar"><span>Ver</span></button>' if a["handle"] else ""))
        tag = f'<p class="micro"><span class="mono">{a["tag"]}</span></p>' if a["tag"] else ""
        rows += f"""          <li class="panel panel--flush row" id="{a['id']}" data-key="{a['key']}" data-reveal style="--i: {i}">
            <div class="photo row__thumb">{athlete_photo(a, "96px")}</div>
            <div class="row__head">
              <div class="row__idx"><p class="micro micro--dot">Atleta // <span class="mono">{a['n']}</span></p>{tag}</div>
              <h3 class="name"><span class="name__first">{a['first']}</span><span class="name__last">{a['last']}</span></h3>
            </div>
            <ul class="row__top">{"".join(f'<li><span class="val">{v}</span><span class="lab">{lab}</span></li>' for v, lab in a["wins"][:2])}</ul>
            {tog}
{more}          </li>
"""
    return f"""    <section class="section" id="atletas" aria-labelledby="atletas-title">
      <div class="wrap">
{atletas_head()}        <ul class="roster">
{rows}        </ul>
      </div>
    </section>
"""


def atletas_cards():
    cards = ""
    for i, a in enumerate(ATHLETES):
        rest = len(a["wins"]) - 2
        more = ""
        if rest > 0:
            more = f'<div class="more" id="more-{a["id"]}" hidden><div>{wins_list(a, 2)}</div></div><button class="link-btn" type="button" aria-expanded="false" aria-controls="more-{a["id"]}" data-toggle="more-{a["id"]}" data-labels="+ {rest:02d}|Fechar"><span>+ {rest:02d}</span></button>'
        tag = f'<p class="micro"><span class="mono">{a["tag"]}</span></p>' if a["tag"] else ""
        cards += f"""          <li class="panel panel--flush card" id="{a['id']}" data-key="{a['key']}" data-reveal style="--i: {i}">
            <div class="photo card__photo parallax zoom" data-parallax="0.06">{athlete_photo(a, "(min-width: 720px) 30vw, 40vw")}</div>
            <div class="card__body">
              <div class="row__idx"><p class="micro micro--dot">Atleta // <span class="mono">{a['n']}</span></p>{tag}</div>
              <h3 class="name"><span class="name__first">{a['first']}</span><span class="name__last">{a['last']}</span></h3>
              <ul class="row__top">{"".join(f'<li><span class="val">{v}</span><span class="lab">{lab}</span></li>' for v, lab in a["wins"][:2])}</ul>
              {more}
              {handle(a)}
            </div>
          </li>
"""
    return f"""    <section class="section" id="atletas" aria-labelledby="atletas-title">
      <div class="wrap">
{atletas_head("right")}        <ul class="cards">
{cards}        </ul>
      </div>
    </section>
"""


def atletas_names():
    tabs = ""
    panels = ""
    for i, a in enumerate(ATHLETES):
        tabs += f'          <li><button class="name names__btn" type="button" data-product="{a["id"]}" aria-expanded="false" aria-controls="ath-{a["id"]}"><span class="name__first">{a["first"]}</span><span class="name__last">{a["last"]}</span></button></li>\n'
        tag = f'<li><p class="micro"><span class="mono">{a["tag"]}</span></p></li>' if a["tag"] else ""
        panels += f"""          <article class="panel panel--flush athlete product" id="ath-{a['id']}" data-id="{a['id']}" data-key="{a['key']}" hidden>
            <div class="photo athlete__photo parallax zoom" data-parallax="0.08">{athlete_photo(a, "(min-width: 900px) 40vw, calc(100vw - 32px)")}</div>
            <div class="athlete__body">
              <ul class="microbar"><li><p class="micro micro--dot">Atleta // <span class="mono">{a['n']}</span></p></li>{tag}</ul>
              <h3 class="name name--lg product__name"><span class="name__first">{a['first']}</span><span class="name__last">{a['last']}</span></h3>
              <div class="stack"><p class="micro">Palmarés</p>{wins_list(a)}</div>
              {handle(a)}
            </div>
          </article>
"""
    return f"""    <section class="section" id="atletas" aria-labelledby="atletas-title">
      <div class="wrap">
{atletas_head()}        <ul class="names" data-reveal>
{tabs}        </ul>
        <div class="sheet sheet--athletes" data-mode="tabs" data-group="athletes" aria-hidden="true"><div class="sheet__clip"><div class="sheet__inner">
{panels}        </div></div></div>
      </div>
    </section>
"""


def footband():
    return f"""    <footer class="footband" id="contacto" aria-labelledby="contacto-title">
      <div class="wrap">
        <div class="contact" data-reveal>
          <p class="micro micro--dot" data-type>Contacto // encomendas e parcerias</p>
          <h2 id="contacto-title" class="h2">CONTACTa-NOS</h2>
          <hr class="rule rule--key">
          <p>Pretendes mais informação sobre os produtos ou é um clube e pretende discutir parcerias? Entra em contacto!</p>
          <div class="actions">
            <a class="btn btn--primary" href="mailto:info@shomen-sports.com">info@shomen-sports.com</a>
            <a class="btn" href="https://instagram.com/shomen_sports" rel="noopener">@shomen_sports</a>
          </div>
        </div>
        <div class="footer__meta">
          <a class="footer__logo" href="#top"><img src="{A}originals/union.png" width="960" height="216" alt="Shomen Sports, início da página"></a>
          <nav class="footer__nav" aria-label="Rodapé">
            <ul>
              <li><a class="micro micro--white" href="#top">Início</a></li>
              <li><a class="micro micro--white" href="#produtos">Produtos</a></li>
              <li><a class="micro micro--white" href="#atletas">Atletas</a></li>
              <li><a class="micro micro--white" href="#contacto">Contacto</a></li>
            </ul>
          </nav>
          <address class="footer__links">
            <ul>
              <li><a class="handle" href="https://instagram.com/shomen_sports" rel="noopener">@shomen_sports</a></li>
              <li><a class="micro micro--white" href="mailto:info@shomen-sports.com">info@shomen-sports.com</a></li>
            </ul>
          </address>
          <p class="micro footer__copy">SHOMEN © 2026</p>
        </div>
      </div>
    </footer>
"""


def gallery_dialog():
    return """  <dialog class="modal" id="galeria" data-key="blue" aria-labelledby="galeria-title">
    <div class="panel modal__panel">
      <div class="modal__head">
        <div class="stack"><p class="micro micro--dot">Galeria completa</p><h2 class="h3" id="galeria-title" data-gallery-title>Produto</h2></div>
        <button class="btn btn--ghost modal__close" type="button" data-close>Fechar</button>
      </div>
      <ul class="modal__grid"></ul>
    </div>
  </dialog>
"""


def page(title, css, body_sections, rail=False):
    return (head(title, css) + '<body data-key="red">\n' + nav(rail) + '\n  <main id="conteudo">\n' + "".join(body_sections)
            + '  </main>\n' + gallery_dialog() + '  <script src="_base.js"></script>\n</body>\n</html>\n')


# ---------------------------------------------------------------- variants
CSS_A = """/* Variant A — "Directo": top bar, full-bleed hero, products first (expanding panel), roster. */
.product__display { display: none; }
.row__big { display: none; }
@media (min-width: 720px) { .row__big { display: block; max-width: 320px; } }
"""

CSS_B = """/* Variant B — "Rail": left rail nav on desktop, split hero with the vertical word, Compromisso first
   with the 03 display moment, products as a horizontal scroller with an active card, athletes as compact cards. */
.hero--split { align-items: stretch; height: auto; min-height: 0; max-height: none; }
.hero__grid { display: grid; gap: 24px; padding-block: calc(var(--nav-h) + 16px) 32px; }
.hero--split .hero__content { padding: 0; align-content: end; }
.hero--split .hero__title { font-size: clamp(44px, 6.6vw, 100px); }
.hero--split .hero__side { position: relative; }
.hero--split .hero__photo { position: relative; inset: auto; aspect-ratio: 16 / 10; }
.hero--split .hero__photo img { filter: brightness(.8) saturate(.95); object-position: 50% 30%; }
.hero--split .hero__vword { display: block; right: auto; left: -8px; top: 0; transform: none; animation: none; border-left: 0; padding: 0; font-size: 13px; letter-spacing: .14em; font-weight: 300; color: var(--grey); }
.hero--split .hero__glow { left: auto; right: 0; top: -10%; width: 50vw; height: 50vw; }
@media (min-width: 960px) {
  .hero--split { height: min(92vh, 900px); height: min(92svh, 900px); }
  .hero__grid { grid-template-columns: 7fr 5fr; align-items: stretch; height: 100%; }
  .hero--split .hero__side { display: grid; grid-template-columns: 48px 1fr; }
  .hero--split .hero__vword { position: static; writing-mode: vertical-rl; font-size: 32px; font-weight: 900; color: var(--white); letter-spacing: .04em; border-left: 2px solid var(--key); padding-left: 12px; align-self: center; justify-self: center; animation: drift 9s ease-in-out infinite; }
  .hero--split .hero__photo { aspect-ratio: auto; height: 100%; }
  .hero__readouts { justify-content: flex-start; text-align: left; }
}
/* rail nav */
@media (min-width: 960px) {
  .nav--rail { position: fixed; top: 0; left: 0; bottom: 0; width: 72px; border-bottom: 0; border-right: 1px solid var(--line); z-index: 50; }
  .nav--rail .nav__inner { min-height: 0; flex-direction: column; justify-content: flex-start; padding: 16px 0 0; }
  .nav--rail .nav__logo img { height: 14px; }
  .nav--rail .nav__menu { position: absolute; top: 50%; left: 0; right: 0; height: auto; transform: translateY(-50%); justify-content: center; }
  .nav__list--rail { flex-direction: column; gap: 8px; align-items: center; }
  .nav__list--rail .nav__link { writing-mode: vertical-rl; transform: rotate(180deg); padding: 10px 0; min-height: 0; }
  .nav__list--rail .nav__dot { left: auto; right: 8px; bottom: auto; top: 0; transform: translateY(var(--y, 0px)); }
  body { padding-left: 72px; }
  .progress { left: 72px; width: calc(100% - 72px); }
}
/* scroller */
.tiles--scroller { display: flex; gap: var(--gap); overflow-x: auto; scroll-snap-type: x mandatory; padding-bottom: 8px; scrollbar-width: thin; scrollbar-color: var(--dim) transparent; }
.tiles--scroller .tile { flex: 0 0 62vw; scroll-snap-align: start; }
.tiles--scroller .tile .photo { aspect-ratio: 4 / 5; }
.tiles--scroller .tile.is-active { transform: none; }
.tiles--scroller .tile.is-active .photo { aspect-ratio: 4 / 5; }
@media (min-width: 720px) { .tiles--scroller .tile { flex: 0 0 300px; } .tiles--scroller .tile.is-active { flex-basis: 360px; } }
.tile { transition: transform .5s var(--ease-out), flex-basis .5s var(--ease-out); }
/* cards */
.cards { list-style: none; margin: 0; padding: 0; display: grid; gap: var(--gap); }
.card { display: grid; grid-template-columns: 38% 1fr; }
.card__photo { aspect-ratio: 4 / 5; align-self: start; }
.card__body { display: grid; gap: 10px; align-content: start; padding: 14px; }
.card .name { font-size: clamp(22px, 2.2vw, 30px); line-height: 1; }
.card .name span { display: inline; } .card .name__first::after { content: " "; }
.card .name__last { color: var(--key); }
@media (min-width: 720px) { .cards { grid-template-columns: repeat(3, 1fr); } .card { grid-template-columns: 1fr; } .card__photo { aspect-ratio: 1; height: auto; } }
.product__display { display: none; }
"""

CSS_C = """/* Variant C — "Ficha": top bar, full-bleed hero, products as a tabbed spec sheet (always one open,
   the REF code is the display moment), strip, Compromisso later, athletes as name tabs + detail panel. */
.tiles .tile .photo { aspect-ratio: 4 / 3; }
.tile.is-active { transform: none; }
.tile.is-active::before { --tick: var(--key); }
.tile__btn[aria-expanded="true"] .open::before { content: "ABERTO"; }
.product__display { font-family: var(--font-mono); font-weight: 700; font-size: clamp(64px, 12vw, 160px); line-height: .85; letter-spacing: -.05em; color: var(--key); margin: 0 0 8px; opacity: .9; }
.sheet--athletes .sheet__inner { margin-top: var(--gap); }
.names { list-style: none; margin: 0 0 4px; padding: 0; display: flex; flex-wrap: wrap; gap: 8px 32px; }
.names__btn { border: 0; background: none; padding: 6px 0; cursor: pointer; font-size: clamp(28px, 4.5vw, 56px); color: var(--grey); text-align: left; }
.names__btn .name__first, .names__btn .name__last { display: inline; }
.names__btn .name__first { font-weight: 300; } .names__btn .name__first::after { content: " "; }
.names__btn .name__last { font-weight: 900; }
.names__btn:hover, .names__btn[aria-expanded="true"] { color: var(--white); }
.names__btn[aria-expanded="true"] .name__last { color: var(--key); }
.athlete { display: grid; }
.athlete__photo { aspect-ratio: 4 / 5; }
.athlete__media { position: relative; }
.athlete__body { display: grid; gap: 16px; align-content: start; padding: clamp(18px, 3vw, 32px); }
.name--lg { font-size: clamp(32px, 3.4vw, 52px); }
.name--lg .name__last { color: var(--key); }
@media (min-width: 900px) { .athlete { grid-template-columns: minmax(0, 5fr) minmax(0, 7fr); } .athlete__photo { aspect-ratio: auto; min-height: 420px; } .athlete__photo img { position: absolute; inset: 0; } }
@media (max-width: 899.98px) { .athlete__photo { aspect-ratio: 1; } }
"""


def build():
    a = page("Phase 4 — Variant A (Directo)", CSS_A,
             [hero_full(), ticker(), produtos("accordion"), compromisso("02"), strip(), atletas_roster(), footband()])
    b = page("Phase 4 — Variant B (Rail)", CSS_B,
             [hero_split(), compromisso("01", display=True), produtos("tabs", scroller=True, align="right"), atletas_cards(), strip(), footband()], rail=True)
    c = page("Phase 4 — Variant C (Ficha)", CSS_C,
             [hero_full(), ticker(), produtos("tabs", display_ref=True), strip(), compromisso("03"), atletas_names(), footband()])
    for name, html in (("variant-a.html", a), ("variant-b.html", b), ("variant-c.html", c)):
        (HERE / name).write_text(html, encoding="utf-8")
        print(name, len(html) // 1024, "KB")


if __name__ == "__main__":
    build()
