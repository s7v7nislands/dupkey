import sys
import ast

class v(ast.NodeVisitor):
    def visit_Dict(self, node):
        keys = set()
        for k in node.keys:
                if isinstance(k, ast.Num):
                    key = k.n
                elif isinstance(k, ast.Str):
                    key = k.s

                if key in keys:
                    print("find duplicate key: %r" % key)
                keys.add(key)

def main():
    if len(sys.argv) <= 1:
        print "usage: %s filename" % sys.argv[0]
        return

    x = v()
    for f in sys.argv[1:]:
        t = ast.parse(open(f).read())
        print("check %s:" % f)
        x.visit(t)

if __name__ == "__main__":
    main()

