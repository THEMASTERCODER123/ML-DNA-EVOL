import math

def predict_time(target):
    target_length = len(target)

    population_size = 100
    mutation_rate = 0.01
    characters = 53  # a-z, A-Z, space

    # Rough difficulty estimate
    expected_mutations_per_generation = (
        population_size * target_length * mutation_rate
    )

    # Longer strings become progressively harder
    estimated_generations = (
        characters
        * target_length
        / max(expected_mutations_per_generation, 0.0001)
    ) * math.log(target_length + 1)

    # Change this after measuring your actual program
    generations_per_second = 50

    estimated_seconds = estimated_generations / generations_per_second

    return estimated_generations, estimated_seconds


target = input("Target: ")

generations, seconds = predict_time(target)

print("Target length:", len(target))
print("Estimated generations:", round(generations))
print("Estimated time:", round(seconds, 2), "seconds")