# École Saint-Joseph · Jemeppe-sur-Sambre

Site statique de l’école : <https://ecolesaintjosephjemeppe.be/>.

## Modifier le site

Les pages HTML générées restent à la racine et dans leurs dossiers historiques, compatibles avec GitHub Pages et le domaine déclaré dans `CNAME`.

- Gabarits et contenu des pages : `scripts/build_site.py`.
- Contenu durable : `data/vie-ecole.json` (3 sujets illustrés sans dates ni liens vers des publications).
- Historique éditorial conservé dans `data/actualites.json`, sans affichage sur le site.
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

## Contenu et liens vérifiés

- Les adresses HTML historiques restent accessibles ; la nouvelle page `vie-ecole/index.html` présente les thèmes durables de la vie de l’école. Les anciennes pages annuelles reprennent ce contenu sans journal daté ni renvois vers des publications.
- La présentation, les horaires, les coordonnées et les informations utiles de l’école sont conservés. Les répétitions sont supprimées et les travaux sont présentés sans date.
- Les 12 fichiers PDF et le logo sont inchangés. Les documents anciens sont identifiés comme « archive » ; le secrétariat reste le contact pour les versions en vigueur. Les fichiers PDF eux-mêmes peuvent contenir leurs dates d’origine.
- Les photos retenues pour le contenu public montrent la cour, le cadre de vie et une activité collective. Aucune affiche comportant une date ni aucun collage générique n’est affiché.
- Il n’y a plus de dates visibles, de cartes de publications, de filtres d’actualités, d’intégration Facebook ni de liens vers des posts ou vidéos individuels. Les liens Facebook mènent uniquement à la page de l’école avec le libellé « Suivre l’actualité sur Facebook ».
- Le contenu historique et ses sources restent dans `data/actualites.json` pour référence, sans être affichés. Les anciens flux RSS et Atom restent disponibles pour leurs anciens abonnés mais ne sont plus annoncés dans les pages.
- L’ancienne visite virtuelle en erreur 404 n’est plus intégrée ; la page de découverte des lieux présente des photographies et invite les familles à prendre rendez-vous.
- Les photographies servies localement dans `media/actualites/` ont été récupérées depuis les métadonnées des publications existantes lorsque leur identifiant de média correspondait à l’original.

## Validation

Le vérificateur couvre toutes les pages, cibles locales, ancres, ressources CSS, présence des 12 PDF et textes alternatifs. Il contrôle aussi l’absence de dates visibles et de liens vers des publications Facebook. Les pages principales ont été parcourues dans le navigateur ; les liens de navigation et le menu mobile sont vérifiés.
