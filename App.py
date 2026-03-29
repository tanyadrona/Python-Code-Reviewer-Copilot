import ast

def review_code(file_path):
    with open(file_path, "r") as f:
        code = f.read()
        tree = ast.parse(code)

    for node in ast.walk(tree):

        if isinstance(node, ast.FunctionDef):

            if not ast.get_docstring(node):
                print(f"Function '{node.name}' is missing a docstring")

            if len(node.body) > 20:
                print(f"Function '{node.name}' is too long")

        if isinstance(node, ast.Name):
            if len(node.id) < 3:
                print(f"Variable '{node.id}' name is too short")

if __name__ == "__main__":
    review_code("SampleCode.py")
