# UBHess Émargement

Ou comment émarger en une ligne de commande, no crontab, no service.

## How-To

Fichier .env :

```
MoodleCourseUrl=https://moodle.univ-ubs.fr/course/view.php?id=10731
MoodleAttendanceUrl=https://moodle.univ-ubs.fr/mod/attendance/view.php?id=433339
MoodleUs=e2xxxxxxx
MoodlePa=ILoveJohanne
MoodleSh=False #True
```
Lancez ensuite le script `emarger.sh`.

Sous OSX, installez Firefox avec Homebrew :

`brew install --cask firefox`

Tips : simplifiez vous la vie en ajoutant un alias à votre bash/zsh-rc, vous pourrez ajouter la compétence flémmard à votre portfolio.

## Ack

Merci à MTlyx pour la gestion de l'intéraction avec Moodle.
