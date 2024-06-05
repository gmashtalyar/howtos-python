import xml.sax


class GroupHandler(xml.sax.ContentHandler):

    def startElement(self, name, attrs):
        self.current = name
        if self.current == "person":
            print("------Person------")
            print(f"ID: {attrs['id']}")

    def characters(self, content):
        if self.current == "name":
            self.name = content
        elif self.current == "age":
            self.age = content
        elif self.current == "weight":
            self.weight = content
        elif self.current == "height":
            self.height = content

    def endElement(self, name):
        if self.current == "name":
            print(f"Name: {self.name}")
        elif self.current == "age":
            print(f"Age: {self.age}")
        elif self.current == "weight":
            print(f"Weight: {self.weight}")
        elif self.current == "height":
            print(f"Height: {self.height}")
        self.current = ""


handler = GroupHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse('10_data.xml')
