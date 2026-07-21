# Notes de reprise, publications Facebook vers le site

## Principe retenu

Ne pas intégrer de plugin Facebook live sur le site.

À la place, transformer les publications Facebook en contenu éditorialisé et statique.

## Règles à respecter

- Accueil: afficher seulement **3 publications**.
- Page actualité: afficher une sélection élargie, par défaut **20 publications**.
- Garder uniquement des posts **utiles, clairs, représentatifs** de la vie de l'école.
- Écarter les posts faibles ou bruités:
  - posts vides
  - photos seules sans contexte
  - messages trop internes
  - liens bruts
  - publications conflictuelles ou peu compréhensibles hors Facebook

## Règle image

Très important:

- **si l'image ne vient pas réellement du post Facebook, ne pas l'utiliser**
- si le post n'a pas de vraie image exploitable, utiliser un placeholder visuel simple avec le libellé **"Actu"**
- éviter les collages génériques si on veut rester fidèle au post source

## Vidéos

Ne pas réintégrer un embed Facebook fragile.

Pour une vidéo ou un reel:

- utiliser une **image de preview** du post
- enveloppée dans un lien vers Facebook
- garder une mise en page propre et stable côté site

## Mise en forme éditoriale

Chaque carte doit idéalement contenir:

- date
- badge de type
- titre court et lisible
- petit texte de contexte réécrit pour le site
- lien vers la publication Facebook

## Types de badges utiles

- Inscriptions
- Événement
- Vie de l'école
- Projet pédagogique
- Archives
- Infos pratiques
- Lecture
- Maternelle
- Présentation
- Projet artistique

## Fichiers touchés lors de cette mise en place

- `index.html`
- `2026/index.html`
- `resources/css/style.css`

## Approche recommandée si on doit le refaire

1. Exporter ou récupérer les posts Facebook sources.
2. Faire un tri éditorial.
3. Sélectionner 3 posts forts pour l'accueil.
4. Sélectionner une liste plus large pour la page actualité.
5. Vérifier image par image qu'elle provient bien du post.
6. Si pas d'image fiable, mettre le placeholder `Actu`.
7. Réécrire les titres et résumés pour une lecture web plus propre.
8. Vérifier le rendu responsive.

## Pourquoi cette approche est meilleure

- plus stable qu'un plugin Facebook
- plus rapide à charger
- plus propre visuellement
- meilleur contrôle éditorial
- évite les surprises de rendu ou de contenu cassé
