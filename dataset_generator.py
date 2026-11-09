import random

def generate_dataset(size,distribution='random', seed=36 ):
    if size <0:
        raise ValueError('Dataset size cannot be negative' )
    
    rng =random.Random(seed )
    if distribution == 'random':
        return [rng.randint(0, size * 10 + 1) for _ in range(size)]
    
    if distribution == 'sorted':
        return list(range(size))
    
    if distribution == 'reverse' :
        return list(range(size,0, -1 ))
    
    if distribution == 'duplicates':
        return [ rng.randint(0,  9) for _ in range(size)]
    
    raise ValueError('Unknown distribution')
