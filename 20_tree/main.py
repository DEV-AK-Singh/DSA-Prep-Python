class Tree:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level    

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()  

def main():
    root = Tree("Electronics")

    tv = Tree("Televisions")
    tv.add_child(Tree("Samsung"))
    tv.add_child(Tree("LG"))
    tv.add_child(Tree("Acer"))

    mobile = Tree("Mobiles")
    mobile.add_child(Tree("Vivo"))
    mobile.add_child(Tree("Redmi"))
    mobile.add_child(Tree("Apple"))

    headphones = Tree("Headphones")
    headphones.add_child(Tree("Boat"))
    headphones.add_child(Tree("Bluepunkt"))
    headphones.add_child(Tree("Hammer"))

    root.add_child(tv)
    root.add_child(mobile)
    root.add_child(headphones)

    root.print_tree()

if __name__ == "__main__":
    main()