#!/usr/bin/env python3
"""Generate the static school website. Python standard library only."""
from pathlib import Path
from html import escape as e
from datetime import date
import json

ROOT = Path(__file__).resolve().parents[1]
NEWS = json.loads((ROOT / 'data/actualites.json').read_text())
DOCS = json.loads((ROOT / 'data/documents.json').read_text())
FB = 'https://www.facebook.com/profile.php?id=61579439886113'
VIDEO = 'https://www.facebook.com/reel/1337547268477914/'
NAV = [('Accueil', 'index.html'), ('Notre école', 'Notre-école/index.html'), ('Actualités', '2026/index.html'), ('Documents', 'Documents/index.html'), ('Contact', 'contact/index.html')]
ARROW = '<span aria-hidden="true">↗</span>'


def external(url, label, cls='text-link'):
    return f'<a class="{cls}" href="{e(url)}" target="_blank" rel="noopener noreferrer">{label} {ARROW}<span class="sr-only"> (nouvel onglet)</span></a>'


def button(path, label, secondary=False):
    return f'<a class="button {"secondary" if secondary else ""}" href="{path}">{label} <span aria-hidden="true">→</span></a>'


def picture(base, cls='school-picture'):
    return f'<figure class="{cls}"><img src="{base}media/actualites/01.jpg" alt="La cour de l’école Saint-Joseph, ses bâtiments et ses espaces verts" width="1200" height="675"><figcaption>Un petit coin de verdure, au cœur de Jemeppe-sur-Sambre.</figcaption></figure>'


def intro(kicker, title, text):
    return f'<section class="page-intro"><div class="wrap"><p class="eyebrow">{kicker}</p><h1>{title}</h1><p class="lead">{text}</p></div></section>'


def visit(base):
    return f'<section class="visit wrap"><div><p class="eyebrow">Et si on se rencontrait ?</p><h2>Une école se découvre aussi en vrai.</h2><p>Venez rencontrer notre équipe, découvrir les lieux et poser toutes vos questions. Nous vous accueillons sur rendez-vous.</p></div>{button(base+"contact/index.html", "Organiser une visite")}</section>'


def hours():
    return '<dl class="hours"><div><dt>Lundi, mardi, jeudi et vendredi</dt><dd>8h35 <span>—</span> 15h15</dd></div><div><dt>Mercredi</dt><dd>8h35 <span>—</span> 12h25</dd></div><div><dt>Étude pour les primaires</dt><dd>15h30 <span>—</span> 16h30</dd></div></dl>'


def cards(base, posts):
    out = ''
    for n in posts:
        d = date.fromisoformat(n['date'])
        thumb = f'<img src="{base}{n["image"]}" alt="" width="600" height="338" loading="lazy">' if n['image'] else '<div class="news-placeholder" aria-hidden="true"><span>Actu</span><i>✳</i></div>'
        out += f'<article class="news-card" data-category="{e(n["category"])}">{thumb}<div class="news-body"><div class="news-meta"><span class="badge">{e(n["category"])}</span><time datetime="{n["date"]}">{d.strftime("%d.%m.%Y")}</time></div><h3>{e(n["title"])}</h3><p>{e(n["text"])}</p>{external(n["url"], "Voir la publication")}</div></article>'
    return f'<div class="news-grid">{out}</div>'


def document_list(base, indices):
    labels = ['Protection des données personnelles', 'Autorisation de sortie', 'Justificatif d’absence à compléter', 'Règlement d’ordre intérieur et livret de rentrée', 'Charte de vie Saint-Joseph', 'Livret de rentrée 2025–2026', 'Attestations fiscales', 'Informations du service P.S.E.', 'Éphémérides 2025–2026', 'Fiche d’inscription recto verso', 'Fiche médicale 2025', 'Informations du centre PMS']
    out = ''
    for i in indices:
        doc = DOCS[i]
        name = labels[i]
        out += f'<a class="document" href="{base}{doc["file"]}" download="{e(name)}.pdf"><span class="pdf">PDF</span><span>{e(name)}<small>{"Archive · " + doc["year"] if doc["year"] else "Document à télécharger"}</small></span><span class="download" aria-hidden="true">↓</span></a>'
    return '<div class="document-list">' + out + '</div>'


def page(path, title, description, body, active=None):
    depth = len(Path(path).parts)-1
    base = '../'*depth
    active = active or path
    nav = ''.join(f'<a href="{base}{u}"' + (' aria-current="page"' if u == active else '') + f'>{label}</a>' for label,u in NAV)
    footer_nav = ''.join(f'<a href="{base}{u}">{label}</a>' for label,u in NAV[1:])
    html = f'''<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)} | École Saint-Joseph · Jemeppe-sur-Sambre</title><meta name="description" content="{e(description)}">
<meta name="theme-color" content="#234c3b"><link rel="icon" href="{base}resources/images/logo-esj.png" type="image/png">
<link rel="alternate" type="application/rss+xml" title="Archives de l’école" href="{base}feed/rss.xml"><link rel="alternate" type="application/atom+xml" title="Archives de l’école" href="{base}feed/atom.xml">
<link rel="canonical" href="https://ecolesaintjosephjemeppe.be/{e(path if path != 'index.html' else '')}">
<link rel="stylesheet" href="{base}resources/css/school.css"><script src="{base}resources/js/school.js" defer></script></head>
<body><a class="skip-link" href="#contenu">Aller au contenu</a>
<div class="topbar"><div class="wrap"><span>École maternelle &amp; primaire · Jemeppe-sur-Sambre</span><a href="tel:+32475534482">Une question ? 0475 53 44 82 <span aria-hidden="true">↗</span></a></div></div>
<header class="site-header"><div class="wrap header-inner"><a class="brand" href="{base}index.html" aria-label="École Saint-Joseph — Accueil"><img src="{base}resources/images/logo-esj.png" alt="École Saint-Joseph, Jemeppe-sur-Sambre" width="1385" height="776"></a>
<button class="menu-toggle" type="button" aria-expanded="false" aria-controls="navigation" hidden>Menu <span aria-hidden="true">☰</span></button>
<nav id="navigation" aria-label="Navigation principale">{nav}{button(base+'contact/index.html', 'Une visite ?')}</nav></div></header>
<main id="contenu">{body}</main>
<footer class="site-footer"><div class="wrap footer-grid"><div><img class="footer-logo" src="{base}resources/images/logo-esj.png" alt="École Saint-Joseph" width="1385" height="776"><p>Apprendre, grandir et s’épanouir.<br>Ensemble, tout simplement.</p></div><div><h2>À l’école</h2>{footer_nav}<a href="{base}gallery/index.html">Découvrir les lieux</a></div><div><h2>Nous trouver</h2><address>Ruelle de la Queutrale, 1<br>5190 Jemeppe-sur-Sambre</address><a href="tel:+32475534482">0475 53 44 82</a><a class="email" href="mailto:direction@ecolesaintjosephjemeppe.be">direction@ecolesaintjosephjemeppe.be</a>{external(FB, 'Suivez la vie de l’école sur Facebook')}</div></div><div class="wrap footer-bottom"><span>École Saint-Joseph · Jemeppe-sur-Sambre</span><a href="{base}media/{DOCS[0]['file'].split('/')[-1]}" download="Protection-des-donnees.pdf">Protection des données</a><span>Site d’origine : <a href="https://www.codio.be" target="_blank" rel="noopener noreferrer">CODIO.BE</a></span></div></footer>
</body></html>'''
    (ROOT/path).write_text(html+'\n')


def main():
    b=''
    hero=f'''<section class="hero wrap"><div class="hero-copy"><p class="eyebrow"><span class="little-dot"></span> Bienvenue à Saint-Joseph</p><h1>De petites graines.<br>De <em>grandes</em><br>aventures.</h1><p class="lead">Une école maternelle et primaire à taille humaine, dans un écrin de verdure au cœur de Jemeppe-sur-Sambre.</p><div class="actions">{button('Notre-école/index.html','Découvrir notre école')}{button('contact/index.html','Nous rencontrer',True)}</div><div class="hero-note"><span class="note-flower" aria-hidden="true">✳</span> Un cadre familial, pour apprendre et grandir ensemble.</div></div><div class="hero-visual"><span class="sun-doodle" aria-hidden="true">☀</span>{picture('')}<div class="photo-sticker"><span aria-hidden="true">♡</span> Ici, on grandit<br><strong>à son rythme.</strong></div><span class="caption-label">Notre école, tout simplement.</span></div></section>
<section class="quick-strip"><div class="wrap quick-grid"><a href="#horaires"><span class="quick-icon" aria-hidden="true">◷</span><span><small>Le quotidien</small>Horaires de l’école</span><span aria-hidden="true">↘</span></a><a href="Documents/index.html"><span class="quick-icon" aria-hidden="true">▤</span><span><small>Pour les familles</small>Documents utiles</span><span aria-hidden="true">↗</span></a><a href="contact/index.html"><span class="quick-icon" aria-hidden="true">✎</span><span><small>Envie de nous rejoindre ?</small>Visites &amp; inscriptions</span><span aria-hidden="true">↗</span></a></div></section>
<section class="wrap section school-story"><div><p class="eyebrow">Une école où il fait bon grandir</p><h2>Les pieds dans l’herbe,<br>la tête pleine d’idées.</h2></div><div><p>Au bout de la ruelle de la Queutrale, notre école offre un cadre verdoyant et une ambiance familiale. Un poulailler, de l’espace pour jouer et une équipe attentive à l’épanouissement de chaque enfant.</p><a class="text-link" href="Notre-école/index.html">Bienvenue dans notre école {ARROW}</a></div></section>
<section class="news-section"><div class="wrap section"><div class="section-heading"><div><p class="eyebrow">Des découvertes, des projets, des sourires</p><h2>La vie à Saint-Joseph</h2></div><a class="text-link" href="2026/index.html">Toutes les actualités {ARROW}</a></div>{cards('', NEWS[:3])}<p class="section-footnote">Une sélection de notre vie d’école. {external(FB,'Retrouvez-nous aussi sur Facebook')}</p></div></section>
<section class="wrap section practical" id="horaires"><div><p class="eyebrow">Les petits repères du quotidien</p><h2>Une journée<br>à l’école.</h2><p>Les horaires à garder sous la main, pour organiser sereinement les journées en famille.</p>{button('Documents/index.html','Les documents des parents',True)}</div><div class="hours-panel"><h3>Les horaires</h3>{hours()}</div></section>
<section class="video-band"><div class="wrap"><span class="play-icon" aria-hidden="true">▷</span><div><p class="eyebrow">Poussez la porte</p><h2>Notre école en vidéo</h2><p>Un premier aperçu de notre école, de son cadre et de son ambiance.</p></div>{external(VIDEO,'Voir la vidéo sur Facebook','button secondary')}</div></section>'''
    page('index.html','Accueil','Découvrez l’école maternelle et primaire Saint-Joseph à Jemeppe-sur-Sambre : notre cadre verdoyant, la vie de l’école, les horaires et les inscriptions.',hero+visit(''))
    base='../'
    school=intro('Notre école','Un petit coin de nature.<br>Une grande place pour chacun.','Une école familiale, au cœur de Jemeppe-sur-Sambre, où l’épanouissement de votre enfant guide notre équipe pédagogique.')
    school+=f'<section class="wrap section two-columns">{picture(base)}<div><p class="eyebrow">Un cadre à découvrir</p><h2>Un écrin de verdure,<br>tout près de chez vous.</h2><p>Notre école se situe dans un des cadres de vie les plus agréables de la région. Vous serez accueillis par notre poulailler, qui donne un aspect rural à notre école.</p><p>Situé au bout de la ruelle de la Queutrale, l’établissement bénéficie d’une zone sécurisée devant l’école.</p>{button(base+"gallery/index.html","Découvrir les lieux",True)}</div></section>'
    school+='<section class="values-band"><div class="wrap values-grid"><div><span class="value-number">01</span><h2>S’épanouir</h2><p>Notre équipe pédagogique a comme principal objectif l’épanouissement de votre enfant.</p></div><div><span class="value-number">02</span><h2>Prendre l’air</h2><p>Un espace verdoyant où chacun peut se défouler pour mieux se ressourcer.</p></div><div><span class="value-number">03</span><h2>Se sentir bien</h2><p>Un établissement au bout d’une ruelle, dans un cadre familial et bienveillant.</p></div></div></section>'
    school+=f'<section class="wrap section practical"><div><p class="eyebrow">Au fil des années</p><h2>Un cadre qui évolue.</h2><p>Durant l’été 2017, des travaux de réfection des classes maternelles et de remplacement des châssis ont été entrepris. Une alarme incendie a également été installée pour renforcer la sécurité.</p></div><div class="hours-panel"><h3>Les horaires de l’école</h3>{hours()}</div></section>'+visit(base)
    page('Notre-école/index.html','Notre école','Le cadre verdoyant, le poulailler et l’équipe pédagogique de l’école Saint-Joseph à Jemeppe-sur-Sambre.',school)
    news=intro('Le journal de l’école','Les petits moments<br>font les grands souvenirs.','Projets pédagogiques, découvertes, événements et informations pour les familles : retrouvez la vie de Saint-Joseph au fil des saisons.')
    news+='<section class="wrap section"><h2 class="sr-only">Les actualités</h2><div class="news-filters" aria-label="Filtrer les actualités" hidden><button type="button" data-filter="all" aria-pressed="true">Tout voir</button><button type="button" data-filter="school" aria-pressed="false">La vie de l’école</button><button type="button" data-filter="practical" aria-pressed="false">Infos &amp; inscriptions</button><button type="button" data-filter="archives" aria-pressed="false">Archives</button></div><p class="filter-status sr-only" aria-live="polite"></p>'
    news+=cards(base,sorted(NEWS,key=lambda n:n['date'],reverse=True))
    news+=f'<div class="archive-links"><h2>Les années scolaires</h2><a href="../2025/index.html">2025–2026</a><a href="../2024/index.html">2024–2025</a><a href="../2023/index.html">2023–2024</a></div><p class="section-footnote">{external(FB,"Toutes les nouvelles de l’école sur Facebook")}</p></section>'
    page('2026/index.html','Actualités','Les 20 actualités et archives de l’école Saint-Joseph : projets pédagogiques, événements et informations pour les familles.',news)
    docs=intro('Le coin des parents','Les bons documents,<br>au bon endroit.','Inscriptions, vie quotidienne, santé : tous les documents de l’école sont réunis ici, prêts à être téléchargés au format PDF.')
    docs+='<section class="wrap section documents-layout"><aside><h2>Un document manque ?</h2><p>Les documents datés de 2025 ou 2025–2026 sont conservés à titre d’archives. Pour la version de l’année en cours, contactez le secrétariat.</p><a class="text-link email" href="mailto:secretariat@ecolesaintjosephjemeppe.be">Écrire au secrétariat ↗</a></aside><div>'
    for title,ids in [('Inscriptions & santé',[9,10,7,11]),('Au quotidien',[1,2,6]),('Vie de l’école & règlements',[3,4,5,8,0])]:docs+=f'<section class="document-group"><h2>{title}</h2>{document_list(base,ids)}</section>'
    docs+='</div></section>'
    page('Documents/index.html','Documents','Téléchargez les 12 documents de l’école : inscription, justificatif d’absence, autorisation de sortie, règlement et informations santé.',docs)
    contact=intro('Faisons connaissance','Une question ?<br>Une envie de nous rencontrer ?','Pour une inscription, une visite de l’école ou une question du quotidien, nous sommes à votre écoute.')
    contact+=f'<section class="wrap section contact-grid"><div><h2>Prenons rendez-vous.</h2><p>Le directeur ayant une demi-charge de classe, merci de prendre rendez-vous avant votre visite.</p><a class="phone-large" href="tel:+32475534482">0475 53 44 82 {ARROW}</a><div class="contact-person"><h3>La direction</h3><a class="email" href="mailto:direction@ecolesaintjosephjemeppe.be">direction@ecolesaintjosephjemeppe.be</a></div><div class="contact-person"><h3>Le secrétariat</h3><a class="email" href="mailto:secretariat@ecolesaintjosephjemeppe.be">secretariat@ecolesaintjosephjemeppe.be</a></div>{external(FB,"La page Facebook de l’école")}</div><div class="address-panel"><span class="eyebrow">Bienvenue chez nous</span><h2>Au bout de la ruelle,<br>l’école vous attend.</h2><address>Ruelle de la Queutrale, 1<br>5190 Jemeppe-sur-Sambre</address><p>Notre établissement se trouve au bout de la ruelle, dans un cadre verdoyant.</p><hr><h3>Les horaires</h3>{hours()}</div></section>'
    page('contact/index.html','Contact & inscriptions','Contactez la direction au 0475 53 44 82 ou par e-mail. Visites sur rendez-vous, Ruelle de la Queutrale 1, 5190 Jemeppe-sur-Sambre.',contact)
    gallery=intro('Découvrir les lieux','Notre cadre,<br>un de nos beaux atouts.','Un espace verdoyant où chacun peut se défouler pour mieux se ressourcer.')+f'<section class="wrap section gallery-content">{picture(base)}<div class="gallery-copy"><h2>Un premier regard sur notre école.</h2><p>Découvrez l’école en vidéo, puis venez explorer notre cadre et rencontrer l’équipe lors d’une visite sur rendez-vous.</p>{external(VIDEO,"Découvrir l’école en vidéo","button")}</div></section>'+visit(base)
    page('gallery/index.html','Découvrir les lieux','Découvrez le cadre verdoyant de l’école Saint-Joseph et sa vidéo de présentation avant une visite sur rendez-vous.',gallery,active='Notre-école/index.html')
    for y in [2023,2024,2025]:
        content=intro('Les archives',f'Année scolaire<br>{y}–{y+1}.','Les souvenirs et informations conservés de cette année scolaire.')
        content+='<section class="wrap section archive-content">'
        if y==2024:
            content+=f'<article class="archive-article"><p class="eyebrow">3 novembre 2024</p><h2>Inscription</h2><p>N’hésitez pas à venir rencontrer notre école… et à partager !</p>{button("11/03/partage/index.html","Lire l’article",True)}</article>'
        else:content+='<p>Aucun article n’a été publié sur le site pour cette année scolaire.</p>'
        content+='<nav class="archive-pagination" aria-label="Autres années scolaires">'
        if y>2023:content+=f'<a href="../{y-1}/index.html">← {y-1}–{y}</a>'
        if y<2025:content+=f'<a href="../{y+1}/index.html">{y+1}–{y+2} →</a>'
        content+='<a href="../2026/index.html">Toutes les actualités →</a></nav></section>'
        page(f'{y}/index.html',f'Archives {y}–{y+1}',f'Les archives de l’année scolaire {y}–{y+1} à l’école Saint-Joseph.',content,active='2026/index.html')
    article=intro('Archives · 3 novembre 2024','Venez rencontrer<br>notre école.','N’hésitez pas à venir rencontrer notre école… et à partager !')+'<article class="wrap section archive-poster"><img src="../../../../media/6cc60887-95e2-453f-a2cd-3ffebf6ab356" alt="Affiche d’archive : présentation de l’école Saint-Joseph et invitation aux inscriptions" width="922" height="2048"><p>Cette affiche est une archive de 2024. Pour les coordonnées et les inscriptions actuelles, consultez la page Contact.</p><div class="actions">'+button('../../../../contact/index.html','Contacter l’école')+button('../../../index.html','Retour aux archives',True)+'</div></article>'
    page('2024/11/03/partage/index.html','Inscription · Archive 2024','Invitation à découvrir l’école Saint-Joseph, archive du 3 novembre 2024.',article,active='2026/index.html')
    page('2024/11/03/blog-post.html','Inscription · Archive 2024','Retrouvez l’article sur les inscriptions de novembre 2024.',intro('Archives','Inscription','Retrouvez l’invitation à venir rencontrer notre école.')+'<div class="wrap section">'+button('partage/index.html','Lire l’article')+'</div>',active='2026/index.html')


if __name__ == '__main__':
    main()
