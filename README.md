# Ievads dabiskās valodas apstrādē
# Eksāmena darbs "Teksta apkopošana"
## Darba mērķis
Teksta apkopošanas mērķis ir no apjomīga teksta izveidot daudz īsāku apkopojumu, nezaudējot oriģinālā teksta būtību.

Eksāmena darba uzdevums ir ar programmu iegūt teksta apkopojumu, izmantojot "Extractive summarization" metodi, kas noņem liekos teikumus no lietotāja ievadītā teksta un atstāj paša lietotāja ievadīto skaitu pašu vērtīgāko teikumu, nemainot to struktūru, bet atstātos teikumus sakārtojot dilstošā secībā pēc aprēķinātās vērtības
##Darba autori
* Māris Kalniņš, mk20126
* Gvido Igaunis, gi20003
##programmas darbība
Teksta apkopošanas programma paņem lietotāja saskarnē ievadīto tekstu, un saglabājamo teikumu skaitu, un veic secīgi šādas darbības:
* Normalizē tekstu un noņem nenozīmīgos vārdus (stop words);
* Tokenizē normalizēto tekstu vārdu biežuma noteikšanai;
* Saskaita tokenu biežumu tekstā;
* Aprēķina tokenu vērtības atkarībā no to biežuma attiecībā pret kopējo tokenu skaitu;
* Ar iegūtajām tokenu vērtībām aprēķina teksta teikumu vērtības un izvēlas saskarnē ievadīto daudzumu pašu vērtīgāko teikumu;
* Lietotāja saskarnē izvada apkopojumu, kas tiek attēlots kā vērtīgākie teksta teikumi dilstošā secībā.
