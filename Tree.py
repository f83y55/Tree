#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Tree :
    html_code_1 = """<!DOCTYPE html>
<html>
<!-- https://codepen.io/philippkuehn/pen/QbrOaN -->
<head>
    <meta charset="utf-8">
    <title>"""
    html_code_2 = """</title>
    <style type="text/css">
        body {
            font-family: sans-serif;
            font-size: 15px;
        }

        .tree ul {
            position: relative;
            padding: 1em 0;
            white-space: nowrap;
            margin: 0 auto;
            text-align: center;
        }
        .tree ul::after {
            content: "";
            display: table;
            clear: both;
        }

        .tree li {
            display: inline-block;
            vertical-align: top;
            text-align: center;
            list-style-type: none;
            position: relative;
            padding: 1em 0.5em 0 0.5em;
        }
        .tree li::before, .tree li::after {
            content: "";
            position: absolute;
            top: 0;
            right: 50%;
            border-top: 1px solid #ccc;
            width: 50%;
            height: 1em;
            }
        .tree li::after {
            right: auto;
            left: 50%;
            border-left: 1px solid #ccc;
        }
        .tree li:only-child::after, .tree li:only-child::before {
            display: none;
        }
        .tree li:only-child {
            padding-top: 0;
        }
        .tree li:first-child::before, .tree li:last-child::after {
            border: 0 none;
        }
        .tree li:last-child::before {
            border-right: 1px solid #ccc;
            border-radius: 0 5px 0 0;
        }
        .tree li:first-child::after {
            border-radius: 5px 0 0 0;
        }

        .tree ul ul::before {
            content: "";
            position: absolute;
            top: 0;
            left: 50%;
            border-left: 1px solid #ccc;
            width: 0;
            height: 1em;
        }

        .tree li a {
            border: 1px solid #ccc;
            padding: 0.5em 0.75em;
            text-decoration: none;
            display: inline-block;
            border-radius: 5px;
            color: #333;
            position: relative;
            top: 1px;
        }

        .tree li a:hover,
        .tree li a:hover + ul li a {
            background: #e9453f;
            color: #fff;
            border: 1px solid #e9453f;
        }

        .tree li a:hover + ul li::after,
        .tree li a:hover + ul li::before,
        .tree li a:hover + ul::before,
        .tree li a:hover + ul ul::before {
            border-color: #e9453f;
        }
    </style>
    </head>
    <body>
    <div class="tree">
    <ul>
    """
    html_code_3 = """
    </ul>
    </div>
    </body>
</html>"""

    instances = []

    def __init__(self, *args_start, **kwargs_start) :
        Tree.instances.append(self)
        self.function = None
        self.args = args_start
        self.kwargs = kwargs_start
        self.content = {}
        self.html = ""
    
    def write_html(self) :
        def _recurse(d = self.content, depth = 2) :
            for(k, di) in d.items() :
                yield "{}<li> <a href=\"#\"> {} </a>".format("    "*depth, k)
                if di :
                    yield "{}<ul>\n{}\n{}</ul></li>".format("    "*depth, "\n".join(_recurse(di, depth+1)), "    "*depth)
                else :
                    yield "{}</li>".format("    "*depth)
        if len(self.args) == 1 :
            name = "Tree_{}({})".format(self.function.__name__, str(*self.args))
        else :
            name = "Tree_{}{}".format(self.function.__name__, str(self.args))
        self.html = Tree.html_code_1 + name + Tree.html_code_2 + ("\n".join(_recurse())) + Tree.html_code_3
        with open(name+".html", "w") as fichier_html :
            fichier_html.write(self.html)

    def do() :    # static
        for self in Tree.instances :
            self.write_html()

def make(f) :
    tree = Tree()
    tree.function = f
    make.ref, make.count, make.depth, make.capture_args = tree.content, 0, 0, True
    def wrapper(*args, **kwargs) : 
        if make.capture_args : tree.args, tree.kwargs, make.capture_args = args, kwargs, False
        make.count += 1
        count, ref = make.count, make.ref
        make.ref[count]={}
        make.ref = make.ref[count]        # on avance par référence pour l'appel
        make.depth += 1
        res = f(*args, **kwargs)          # appel récursif
        make.depth -= 1
        make.ref = ref                    # on revient à la ref précédente après l'appel
        if len(args) == 1 :
            make.ref["[{}] {}({}) = {}".format(count, f.__name__, str(*args), res)]=make.ref.pop(count)
        else :
            make.ref["[{}] {}{} = {}".format(count, f.__name__, str(args), res)]=make.ref.pop(count)
        return res
    return wrapper


