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
        if node.return_amount_children() == 0:
            return False, None
        for char in path:
            char_found = False
            child = node.return_child(char)
            if child is not None:
                node = child
                char_found = True
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
            child = node.return_child(char)
            if child is not None:
                node = child
                char_found = True
            if not char_found:
                new_node = Node(char)
                node.add_child(char, new_node)
                node = new_node
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
            return node.return_amount_children() > 0
        return False

    def get_value(self, path):
        """ Palauttaa annetun solmun arvon

        Args:
            path (str): Haluttu polku merkkijonona

        Returns:
            int: annetun solmun arvo
        """
        is_node , node = self.find_node(path)
        if is_node:
            return node.return_value()
        return False

    def update_value(self, path):
        """ Päivittää solmun arvoa yhdellä ylöspäin

        Args:
            path (str): Haluttu polku merkkijonona
        """
        is_node, node = self.find_node(path)
        if is_node:
            node.increase_value()

class Node:
    """ Trie-rakenteen solmujen luokka
    """
    def __init__(self, char=None):
        """ Luokan konstruktori

        Args:
            char (str, optional): Solmun nimiarvo/osoite. Defaults to None.

        self._children: Lista solmun lapsisolmuista (Oletus None, jokaiselle 5 vaihtoehdolle)
        self._char: Solmun nimiarvo/osoite (0/1/2, sakset/kivi/paperi)
        self._value: Solmun numeroarvo (montako kertaa pelaaja on käyttänyt polkua)
        """
        self._children = [None, None, None, None, None]
        self._char = char
        self._value = None

    def return_char(self):
        """ Palauttaa solmun nimiarvo/osoite

        Returns:
            str: solmun nimiarvo/osoite
        """
        return self._char

    def return_amount_children(self):
        """ Palauttaa solmun lapsisolmujen määrän

        Returns:
            int: solmun lapsisolmujen määrä
        """
        amount = 0
        for child in self._children:
            if child is not None:
                amount += 1
        return amount

    def return_child(self, char):
        """ Palauttaa halutun lapsisolmun listasta

        Args:
            char (str): lapsisolmun numero

        Returns:
            Node: lapsisolmu
        """
        return self._children[int(char)]

    def return_value(self):
        """ Palauttaa solmun numeroarvon

        Returns:
            int: solmun numeroarvo
        """
        return self._value

    def add_child(self, char, child):
        """ Lisää lapsisolmun listaan

        Args:
            char (str) = solmun numero lapsilistassa
            child (node): lapsisolmu
        """
        self._children[int(char)] = child

    def add_value(self):
        """ Merkitsee että solmussa on käyty jos sitä ei ole aikaisemmin tehty
        """
        if not self._value:
            self._value = 1

    def increase_value(self):
        """ Lisää solmussa käyntikertoja yhdellä
        """
        self._value += 1
