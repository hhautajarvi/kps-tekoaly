class Trie:
    """ Luokka Trie-tietorakenne
        """
    def __init__(self):
        """ Luokan konstruktori

        self._root: Tietorakenteen alkusolmu, jonka tarjoaa Node-luokka
        """
        self._root = Node()

    def find_node(self, path):
        """ Etsii halutun polun solmun jos sellainen on
            Jos ei löydy palauttaa False

        Args:
            path (str): annettu polku merkkijonona

        Returns:
            boolean, node-object: Onko polku olemassa,
                jos on niin myös haluttu solmu
        """
        node = self._root
        if len(node.return_children()) == 0:
            return False, None
        for char in path:
            char_found = False
            for child in node.return_children():
                if child.return_char() == char:
                    char_found  = True
                    node = child
                    break
            if not char_found:
                return False, None
        return True, node

    def add_node(self, path):
        """ Lisää uudet solmut haluttun polun varrelle
            ja lisää päätesolmuun arvon 1

        Args:
            path (str): Haluttu polku merkkijonona
        """
        node = self._root
        for char in path:
            char_found = False
            for child in node.return_children():
                if child.return_char() == char:
                    node = child
                    char_found = True
                    break
            if not char_found:
                new_node = Node(char)
                node.add_child(new_node)
        new_node.add_value()

    def has_key(self, path):
        """ Kertoo onko halutussa solmussa annettu arvo

        Args:
            path (str): Haluttu polku merkkijonona

        Returns:
            boolean: onko halutussa solmussa annettu arvo
        """
        is_node, node = self.find_node(path)
        if is_node:
            return node.return_value() is not None
        return False

    def has_subtrie(self, path):
        """ Kertoo onko halutulla solmulla lapsia

        Args:
            path (str): Haluttu polku merkkijonona

        Returns:
            boolean: onko halutulla solmulla lapsia
        """
        is_node, node = self.find_node(path)
        if is_node:
            return len(node.return_children()) > 0
        return False

    def get_value(self, path):
        """ Palauttaa annetun solmun arvon

        Args:
            path (str): Haluttu polku merkkijonona

        Returns:
            int: annetun solmun arvo
        """
        _, node = self.find_node(path)
        return node.return_value()

    def update_value(self, path):
        """ Päivittää solmun arvoa yhdellä ylöspäin

        Args:
            path (str): Haluttu polku merkkijonona
        """
        _, node = self.find_node(path)
        node.increase_value()

class Node:
    """ Trie-rakenteen solmujen luokka
    """
    def __init__(self, char=None):
        """ Luokan konstruktori

        Args:
            char (str, optional): Solmun nimiarvo/osoite. Defaults to None.

        self._children: Lista solmun lapsisolmuista
        self._char: Solmun nimiarvo/osoite (0/1/2, sakset/kivi/paperi)
        self._value: Solmun numeroarvo (montako kertaa pelaaja on käyttänyt polkua)
        """
        self._children = []
        self._char = char
        self._value = None

    def return_char(self):
        """ Palauttaa solmun nimiarvo/osoite

        Returns:
            str: solmun nimiarvo/osoite
        """
        return self._char

    def return_children(self):
        """ Palauttaa listan solmun lapsisolmuista

        Returns:
            list: solmun lapsisolmut
        """
        return self._children

    def return_value(self):
        """ Palauttaa solmun numeroarvon

        Returns:
            int: solmun numeroarvo
        """
        return self._value

    def add_child(self, child):
        """ Lisää lapsisolmun listaan

        Args:
            child (node): lapsisolmu
        """
        self._children.append(child)

    def add_value(self):
        """ Merkitsee että solmussa on käyty jos sitä ei ole aikaisemmin tehty
        """
        if not self._value:
            self._value = 1

    def increase_value(self):
        """ Lisää solmussa käyntikertoja yhdellä
        """
        self._value += 1
