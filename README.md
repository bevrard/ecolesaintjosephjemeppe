# École Saint-Joseph · Jemeppe-sur-Sambre

Site statique de l’école : <https://ecolesaintjosephjemeppe.be/>.

## Modifier le site

Les pages HTML générées restent à la racine et dans leurs dossiers historiques, compatibles avec GitHub Pages et le domaine déclaré dans `CNAME`.

- Gabarits et contenu des pages : `scripts/build_site.py`.
- Actualités : `data/actualites.json` (3 sélections sur l’accueil, 20 publications sur la page Actualités).
- Documents : `data/documents.json` ; PDF originaux conservés dans `media/`.
- Style et interactions : `resources/css/school.css`, `resources/js/school.js`.
- Logo original inchangé : `resources/images/logo-esj.png`.

Après une modification, régénérer et vérifier avec Python 3 (aucune dépendance nécessaire) :

```sh
python3 scripts/build_site.py
python3 scripts/check_site.py
node --check resources/js/school.js
python3 -m http.server 8765 --bind 127.0.0.1
```

Puis ouvrir <http://127.0.0.1:8765>. Publier également les HTML régénérés dans le commit. Les pages, la navigation et les téléchargements fonctionnent sans JavaScript ; le menu mobile et les filtres sont des améliorations progressives.

## Contenu et liens vérifiés le 4 novembre 2026

- Les 11 adresses HTML historiques sont conservées, dont les archives scolaires et l’article d’inscription de 2024. La page `blog-post.html`, auparavant vide, conduit désormais vers cet article.
- Les informations distinctes de la présentation de l’école sont conservées ; les répétitions sont supprimées. Les travaux de 2017 restent explicitement datés.
- Les 12 fichiers PDF et le logo sont inchangés. Les documents datés de 2025 ou 2025–2026 sont identifiés comme archives ; aucune version 2026–2027 n’a été inventée.
- Les 20 actualités sont conservées avec leurs dates et leurs liens sources. Les résumés sont réécrits pour les familles, en conservant le sujet de chaque publication.
- L’ancienne visite intégrée `https://bevrard.github.io/vrt_esjjemeppe/` renvoie HTTP 404. Son intégration est remplacée par la vidéo existante de présentation et une invitation à visiter l’école sur rendez-vous, tout en conservant l’adresse `gallery/index.html`.
- Les anciennes cibles d’archives `/2022` et les liens d’années mal orientés sont retirés ou corrigés. Les URL des flux RSS et Atom n’utilisent plus l’ancien préfixe `/wlr_esjjemeppe`.
- Le lien de page Facebook est harmonisé vers la page fournie par l’utilisateur (identifiant `61579439886113`). Les publications historiques de l’ancienne page restent accessibles depuis leurs actualités d’archive.
- Les 19 URL d’images Facebook temporaires présentes dans l’ancien site renvoient HTTP 403. Dix images ont pu être récupérées via les métadonnées des publications, uniquement lorsque l’identifiant du média correspondait à l’original, puis enregistrées dans `media/actualites/`. Les autres actualités utilisent le visuel neutre « Actu », conformément à `EDITORIAL_FACEBOOK_NOTES.md`. Aucun collage générique n’est utilisé.
- La photo d’accueil est l’image de prévisualisation de la vidéo existante de présentation de l’école, également utilisée auparavant sur l’accueil.
- Les liens des publications Facebook répondent HTTP 200 et leurs métadonnées ont été consultées. L’accès complet peut dépendre de la connexion à Facebook ; un HTTP 200 ne garantit pas une lecture sans compte.

## Validation

Le vérificateur couvre toutes les pages, cibles locales, ancres, ressources CSS, présence des PDF, textes alternatifs et le nombre d’actualités. La refonte a également été contrôlée dans un navigateur aux formats téléphone, tablette et ordinateur, avec vérification du menu, des filtres et de l’absence de débordement horizontal.
