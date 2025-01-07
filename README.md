# UBHess Émargement

Ou comment émarger en une ligne de commande, no crontab, no service.

<img src="https://i.imgflip.com/9fxodg.jpg" title="Je ne suis pas responsable de vos conneries.">. ![image](https://github.com/user-attachments/assets/90d5590d-8bd8-450e-bcb2-fea1bdbcd294)


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
