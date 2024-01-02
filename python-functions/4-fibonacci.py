def fibonacci_sequence(n):
    sequence = []
    a,b=0,1
    while len(sequence)<n:
        sequence.append(a)
        a,b=b,a+b
    return sequence
print(fibonacci_sequence(6))
print(fibonacci_sequence(1))
print(fibonacci_sequence(0))
print(fibonacci_sequence(20))
