import sublime
import sublime_plugin


def getter(_, type, name):
    return (
        "\n\t/**\n"
        + "\t * Accessor method returning GETTER\n"
        + "\t */\n"
        + "\tpublic {} get{}() {{\n".format(type, name.title())
        + "\t\treturn {};\n".format(name)
        + "\t}\n"
    )


def setter(_, type, name):
    return (
        "\n\t/**\n"
        + "\t * Mutator method that sets SETTER\n"
        + "\t */\n"
        + "\tpublic void set{}({} {}) {{\n".format(name.title(), type, name)
        + "\t\tthis.{0} = {0};\n".format(name)
        + "\t}\n"
    )


class Writer(sublime_plugin.TextCommand):
    def run(self, edit):
        self.write(self.writer, self.view, edit)

    def write(self, func, view, edit):
        selection = view.sel()
        end_of_constructor = view.find("}", selection[0].end()).end() + 1

        for region in selection:
            lines = view.substr(region).split("\n")
            for line in lines:
                words = line.split(" ")
                s = func(words[-2], words[-1].strip(";"))
                view.insert(edit, end_of_constructor, s)


class JavaGetterCommand(Writer):
    writer = getter


class JavaSetterCommand(Writer):
    writer = setter
