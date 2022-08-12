from main import check_if_symmetric, convert_to_num

tests = [
    # {
    #     'function': check_if_symmetric,
    #     'input': '!21321s12312!',
    #     'output': True
    # },
    # {
    #     'function': check_if_symmetric,
    #     'input': 'batman',
    #     'output': False
    # }
    {
        'function': convert_to_num,
        'input': "a b c d e f g",
        'output': [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6]
    },
    {
        'function': convert_to_num,
        'input': "zZzZzZzZz",
        'output': [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6]
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

