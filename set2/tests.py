from main import binary_to_decimal, hex_to_decimal, decimal_to_binary, decimal_to_hex, binary_to_hex, binary_to_hex, hex_to_binary

tests = [
    {
        'function': binary_to_decimal,
        'input': "00001010",
        'output': 10
    },
    {
        'function': decimal_to_binary,
        'input': 10,
        'output': '1010'
    },
    {
        'function': hex_to_decimal,
        'input': 'f32f56',
        'output': 15937366
    },
    {
        'function': decimal_to_hex,
        'input': 15937366,
        'output': 'f32f56'
    },
    {
        'function': binary_to_hex,
        'input': "101010111100110111101111",
        'output': "abcdef"
    },
    {
        'function': hex_to_binary,
        'input': "abcdef",
        'output': "101010111100110111101111"
    }
]

num_successes = 0
num_failures = 0

for test in tests:
    function = test['function']
    test_input = test['input']
    desired_output = test['output']
    actual_output = function(test_input)

    if actual_output == desired_output:
        num_successes += 1
    else:
        num_failures += 1 
        function_name = function.__name__
        print('')
        print(f'{function_name} failed on input {test_input}')
        print(f'\tActual output: {actual_output}')
        print(f'\tDesired output: {desired_output}')

print(f'Testing complete: {num_successes} successes and {num_failures} failures.')