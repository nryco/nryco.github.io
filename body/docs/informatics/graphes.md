---
layout: page
title: Mes Projets
permalink: /info/graphes/1
---

# Graphes en toute généralité

- Un <span class="vocab">graphe</span> est un ensemble de points où des relations entre deux points apparaissent. Ces relations sont représentées par des <span class="vocab">flèches</span> (<span class="vocab">graphe orienté</span>, liens appelés <span class="vocab">arcs</span>) ou des <span class="vocab">segments</span> (<span class="vocab">graphe non orienté</span>, liens appelés <span class="vocab">arêtes</span>).
- Les points sont appelés <span class="vocab">sommets</span> (en référence aux polyèdres) ou <span class="vocab">nœuds</span> (en référence à la loi des nœuds).

## Graphe simple non orienté

### Définition

Un <span class="vocab">graphe simple non orienté</span> $G$ est un couple $(V, E)$ où :

- $E \subseteq \mathcal{P}(V)$ est un ensemble de paires ou de singletons d’éléments de $V$.
- On appelle <span class="vocab">sommets</span> les éléments de $V$ et <span class="vocab">arcs</span> ceux de $E$.

#### Détails

- La lettre $E$ désigne les <span class="vocab">arcs</span> (en anglais, _edge_). Certains auteurs utilisent un vocabulaire spécifique pour les <span class="vocab">graphes non orientés</span>, par exemple une <span class="vocab">arête</span> (_undirected edge_) pour un <span class="vocab">arc</span>.
- Soit $a = \{x, y\}$ :
  - $a$ relie les <span class="vocab">sommets</span> $x$ et $y$ ($x$ et $y$ sont <span class="vocab">adjacents</span> ou encore <span class="vocab">voisins</span>),
  - $a$ est <span class="vocab">incidente</span> à $x$ et $y$ (ou encore $x$ et $y$ sont <span class="vocab">incidents</span> avec $a$).

---

## Graphe simple orienté

**Note** : Au programme, on ne considère que les graphes avec au plus un seul <span class="vocab">arc</span> d’un <span class="vocab">sommet</span> à un autre.

### Définition

Un <span class="vocab">graphe simple orienté</span> $G$ est un couple $(V, E)$ où :

- $V$ est l’<span class="vocab">ensemble des sommets</span> de $G$,
- $A \subseteq V^2$ est un <span class="vocab">ensemble de couples</span> d’éléments de $V$ appelé <span class="vocab">ensemble des arcs</span> de $G$.

#### Détails

- La lettre $V$ désigne les <span class="vocab">sommets</span> (en anglais, _vertex_, au pluriel _vertices_).
- Un <span class="vocab">arbre</span> est un cas particulier de <span class="vocab">graphe orienté simple</span>.
- Cependant, pour certains auteurs, un <span class="vocab">arbre</span> est un <span class="vocab">graphe non orienté</span> <span class="vocab">connexe</span> et <span class="vocab">acyclique</span> (voir définitions plus loin).
