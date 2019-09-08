# projet-vasarely

<p align="justify">Exercice de programmation fonctionnelle en Python, réalisé dans le cadre du MOOC <a href="https://www.fun-mooc.fr/courses/course-v1:ulb+44013+session01/about">"Apprendre à coder avec Python"</a> proposé par la plateforme France Université Numérique en partenariat avec l'Université de La Réunion et avec l'Université Libre de Bruxelles.</p>

<p align="justify">L'objectif était de développer un programme utilisant Turtle, le module graphique de Python, pour dessiner automatiquement des œuvres d'art optique en fonction de paramètres saisis par l'utilisateur. Ces œuvres sont en réalité des canevas de pavés hexagonaux déformés semblables à <a href="http://www.artnet.fr/artistes/victor-vasarely/pulsar-3-a-2jRF9khsVg3f7yUsRVgEaw2">ceci,</a> dont les dimensions, les couleurs, ou encore la déformation (le cas échéant), sont personnalisables en fonction de ces paramètres. Pour ce qui est de la méthode, il était également demandé d'utiliser plusieurs fonctions imbriquées (détail dans le code joint) et de respecter un certain nombre de règles de bonne pratique et/ou de "pythonicité" :snake:</p>

<p align="justify">Le principe de base est relativement simple avec un programme en quatre parties :</p>

<ul>
  <li><p align="justify">le code principal qui recueille et enregistre les paramètres saisis par l'utilisateur : dimensions de la page et des pavés, couleurs notamment ;</p></li>
  <li><p align="justify">une fonction "pavage" qui détermine la position du centre de chaque pavé d'après ces dimensions ;</p></li>
  <li><p align="justify">une fonction "hexagone" chargée de dessiner chaque pavé d'après la position du centre (transmise par "pavage") ;</p></li>
  <li><p align="justify">une fonction "deformation", fournie par le MOOC et importée, chargée de... "déformer" les coordonnées des points, le cas échéant.</p></li>
</ul>

<p align="justify">Car oui, il est possible, comme dans l'original, de donner l'illusion d'une sphère "poussant" sous la texture. Pour ce faire, le programme recalcule automatiquement les coordonnées des points situés dans le rayon de la sphère tel que défini par l'utilisateur : c'est à cela que sert la fonction "deformation".</p>

<p align="justify">Dans le détail, les paramètres demandés sont les suivants :</p>

<ul>
  <li><p align="justify">coordonnées des angles inférieur gauche et supérieur droit de la page, sous la forme d'un seul entier valant x et y ;</p></li>
  <li><p align="justify">longueur des côtés des pavés, à nouveau sous la forme d'un entier (pas d'unité) ;</p></li>
  <li><p align="justify">couleurs de remplissage, que vous pouvez choisir <a href="https://trinket.io/docs/colors">ici</a> ;</p></li>
  <li><p align="justify">coordonnées du centre de la sphère de déformation, sous la forme de trois entiers (= x, y, z) séparés par des espaces ;</p></li>
  <li><p align="justify">rayon de la sphère = un entier (pas d'unité), pouvant être nul pour "ignorer" la déformation.</p></li>
</ul>

<p align="justify">Ainsi et à titre d'exemple, l'image "test" ci-dessous a été obtenue en saisissant les valeurs suivantes :</p>

<ul>
  <li><p align="justify">coordonnées des angles inférieur gauche et supérieur droit de la page = -250 et 250, respectivement ;</p></li>
  <li><p align="justify">longueur des côtés des pavés = 25 ;</p></li>
  <li><p align="justify">couleurs de remplissage : light gray, dark gray, dim gray, respectivement ;</p></li>
  <li><p align="justify">coordonnées du centre de la sphère de déformation = 0 0 0 ;</p></li>
  <li><p align="justify">rayon de la sphère = 225 :globe_with_meridians:</p></li>
</ul>

<img width="100%" src="https://raw.githubusercontent.com/baptl/Projet-Vasarely/master/shades_of_gray.png" />

<p align="justify">Fichiers joints :</p>

<ul>
  <li><p align="justify">projet_vasarely.py = programme principal, celui que j'ai rédigé ;</p></li>
  <li><p align="justify">deformation.py = module fourni par l'équipe pédagogique du MOOC, importé et utilisé par le programme principal pour produire l'effet de... "déformation" (évidemment) !</p></li>
</ul>

<p align="justify">Pour tester le programme, téléchargez simplement les deux fichiers dans un même répertoire (pour que le programme principal puisse reconnaître le module *) et lancez projet_vasarely.py en ligne de commande.</p>

<p align="justify">Alors, prêt/e à devenir un/e artiste renommé/e ? :smirk:</p>
