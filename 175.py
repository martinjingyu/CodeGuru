import ast
import sys
import subprocess

# Define the types of control flow statements we want to count
CONTROL_FLOW_NODES = {
    'If': ast.If,
    'For': ast.For,
    'While': ast.While,
    'Try': ast.Try,
    'With': ast.With,
    'AsyncFor': ast.AsyncFor,
    'AsyncWith': ast.AsyncWith
}

def count_control_flow_statements(node):
    """Recursively count control flow statements in the AST."""
    counts = {key: 0 for key in CONTROL_FLOW_NODES}
    
    if isinstance(node, tuple(CONTROL_FLOW_NODES.values())):
        counts[CONTROL_FLOW_NODES[type(node).__name__].__name__] += 1
    
    for child in ast.iter_child_nodes(node):
        child_counts = count_control_flow_statements(child)
        for key in counts:
            counts[key] += child_counts[key]
    
    return counts

def analyze_python_module(file_path):
    """Analyze the Python module and count control flow statements."""
    with open(file_path, 'r', encoding='utf-8') as file:
        tree = ast.parse(file.read(), filename=file_path)
    
    counts = count_control_flow_statements(tree)
    
    print("Control Flow Statement Counts:")
    for statement, count in counts.items():
        print(f"{statement}: {count}")

def execute_command(command):
    """Execute a specified command."""
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Command output:")
        print(result.stdout.decode())
    except subprocess.CalledProcessError as e:
        print("An error occurred while executing the command:")
        print(e.stderr.decode())

def main():
    if len(sys.argv) != 3:
        print("Usage: python analyze_and_run.py <path_to_python_module> '<command_to_execute>'")
        sys.exit(1)
    
    file_path = sys.argv[1]
    command = sys.argv[2]

    analyze_python_module(file_path)
    execute_command(command)

if __name__ == "__main__":
    main()