import ast
import operator


class Calculator:
    def __init__(self):
        self.operators = {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
        }

    def evaluate(self, expression: str):
        try:
            tree = ast.parse(expression, mode="eval")
            return self.eval_node(tree.body)
        except SyntaxError:
            return "Error Invalid Expression"

    def eval_node(self, node):
        if isinstance(node, ast.Constant):
            if node.value % 1 == 0:
                return int(node.value)
            else:
                return float(node.value)
        elif isinstance(node, ast.BinOp):
            left = self.eval_node(node.left)
            right = self.eval_node(node.right)
            op = self.operators.get(type(node.op))
            try:
                if op(left, right) % 1 == 0:
                    return int(op(left, right))
                else:
                    return op(left, right)
            except ZeroDivisionError:
                return "Error Division By Zero"
            except SyntaxError:
                return "Error Invalid Expression"
