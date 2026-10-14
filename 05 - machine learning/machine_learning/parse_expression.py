import re



# Define the node structure for the tree
class TreeNode:
    def __init__(self, operation=None, left=None, right=None, value=None):
        self.operation = operation  # Either "union" or "intersection"
        self.left = left  # Left subtree
        self.right = right  # Right subtree
        self.value = value  # The value (only if it's a leaf)

    def __repr__(self):
        if self.value:
            return f'"{self.value}"'
        return f'({self.left} {self.operation} {self.right})'


# Tokenize the expression (sets, operators, parentheses)
def tokenize(expression):
    token_pattern = r'("[^"]*"|\*|\+|\(|\))'
    tokens = re.findall(token_pattern, expression)
    return tokens


# Recursive function to parse tokens and create the tree
def parse(tokens):
    def parse_expression(index):
        nodes = []
        current_op = None

        while index < len(tokens):
            token = tokens[index]

            if token == '(':
                subtree, index = parse_expression(index + 1)
                nodes.append(subtree)
            elif token == ')':
                break
            elif token in ('*', '+'):
                current_op = "intersection" if token == '*' else "union"
            else:
                # Assume this is a set (e.g., "mutsig - ALL")
                node = TreeNode(value=token.strip('"'))
                if current_op and nodes:
                    left_node = nodes.pop()
                    nodes.append(TreeNode(operation=current_op, left=left_node, right=node))
                    current_op = None
                else:
                    nodes.append(node)
            index += 1

        return nodes[0], index

    # Start parsing from the beginning
    root, _ = parse_expression(0)
    return root


# Main function to convert expression to tree
def expression_to_tree(expression):
    tokens = tokenize(expression)
    tree = parse(tokens)
    return tree


# Function to evaluate the tree and perform operations
def evaluate_tree(node, sets):
    # If it's a leaf node, return the corresponding set
    if node.value:
        return set(sets[node.value])

    # Recursively evaluate left and right subtrees
    left_set = evaluate_tree(node.left, sets)
    right_set = evaluate_tree(node.right, sets)

    # Perform the operation (union or intersection)
    if node.operation == "union":
        return left_set.union(right_set)
    elif node.operation == "intersection":
        return left_set.intersection(right_set)

    return set()


# Main function to convert expression to tree and evaluate it
def expression_to_tree_and_evaluate(expression, sets):
    tokens = tokenize(expression)
    tree = parse(tokens)
    result = evaluate_tree(tree, sets)
    return result
