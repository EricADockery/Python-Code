import pygame, time, random

#Size of next generation, change number at the end if needed
resize_rate = 1.005
#Controls crossover appearence
cross_rate = 0.7
#Controls number of chromosomes created at the start, exponential
exponent = 4

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

genes = []

def draw_background(screen):
    screen.fill(white)
def draw_connection(screen, pointlist):
    pygame.draw.lines(screen, black, True, pointlist, 1)
def draw_best_connection(screen, pointlist):
    pygame.draw.lines(screen, red, True, pointlist, 2)

def create_random_chromosomes(genes):
    temp_chromosomes = []
    chromosomes = []
    for i in range(len(genes)**exponent):
        genes_copy = genes[:]
        random.shuffle(genes_copy)
        temp_chromosomes.append(genes_copy)
    for element in temp_chromosomes:
        if element not in chromosomes:
            chromosomes.append(element)
    print(str(len(chromosomes)) + " random chromosomes created")
    return chromosomes

def calculate_distance(chromosome):
    distances = []
    total_distance = 0
    for i in range(len(chromosome)):
        if i < (len(chromosome)-1):
            distance_A_B = (((chromosome[i+1][0]-chromosome[i][0])**2)+(chromosome[i+1][1]-chromosome[i][1])**2)**0.5
            distances.append(distance_A_B)
        else:
            distance_A_B = (((chromosome[i][0]-chromosome[0][0])**2)+(chromosome[i][1]-chromosome[0][1])**2)**0.5
            distances.append(distance_A_B)
    for i in range(len(distances)):
        total_distance += distances[i]
    return total_distance

def calculate_fitness(chromosomes):
    fitness_scores = []
    for i in range(len(chromosomes)):
        fitness = 0
        fitness = 1/calculate_distance(chromosomes[i])
        fitness_scores.append(fitness)
    return fitness_scores

def build_chromosome_fitness_dict(chromosomes, fitness_scores):
    chrom_fit_dict = {}
    for i in range(len(chromosomes)):
        chrom_fit_dict[fitness_scores[i]] = chromosomes[i]
    return chrom_fit_dict

def roulette_selection(chromosomes, fitnesses, new_size):
    sum_fitness = sum(fitnesses)
    rel_fitness = [fitness/sum_fitness for fitness in fitnesses]
    #Generate probability intervals for each chromosome
    probabilities = [sum(rel_fitness[:i+1]) for i in range(len(rel_fitness))]
    #Select chromosomes
    selected_chromosomes = []
    for n in range(new_size):
        r = random.random()
        for (i, chromosome) in enumerate(chromosomes):
            if r <= probabilities[i]:
                selected_chromosomes.append(chromosome)
                break
    return selected_chromosomes

def find_closest(cities):
    dist_a = (((cities[0][0]-cities[1][0])**2)+(cities[0][1]-cities[1][1])**2)**0.5
    dist_b = (((cities[0][0]-cities[2][0])**2)+(cities[0][1]-cities[2][1])**2)**0.5
    if dist_a < dist_b:
        return cities[1]
    else:
        return cities[2]

#Greedy crossover selects the first city of one parent,
#compares the cities leaving that city in both parents,
#and chooses the closer one to extend the tour.
#If one city has already appeared in the tour, we choose the other city.
#If both cities have already appeared, we randomly select a non-selected city.    
def crossover(chromosomes, rate):
    new_chromosomes = []
    #len -1 because index out of range error might occur otherwise
    for i in range(len(chromosomes)-1):
        #Crossover T/F
        if random.random() < rate:
            #Take 2 chromosomes
            a = chromosomes[i]
            b = chromosomes[i+1]
            #Randomly select crossover location
            cross_location = random.randint(1, len(chromosomes[i]))
            #Create parts
            c = a[:cross_location]
            for i in range((len(a)-len(c))):
                #City to start from
                start_pos = c[-1]
                #2 most plausible targets
                target_0 = a[cross_location+i]
                target_1 = b[cross_location+i]
                #Determine if targets already appear in c and add correct city
                if target_0 in c:
                    if target_1 in c:
                        not_yet_selected = []
                        for city in genes:
                            if city not in c:
                                not_yet_selected.append(city)
                        c.append(not_yet_selected[random.randint(0,(len(not_yet_selected)-1))])
                    else:
                        c.append(target_1)
                elif target_1 in c:
                    c.append(target_0)
                else:
                    cities = [start_pos, target_0, target_1]
                    closest = find_closest(cities)
                    c.append(closest)
            new_chromosomes.append(c)
        else:
            new_chromosomes.append(chromosomes[i])
    return new_chromosomes

pygame.init()
screen = pygame.display.set_mode((640,340))
clock = pygame.time.Clock()
done = False
first = True
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if genes != []:
                    #Start Genetic Algorithm
                    print('Creating initial solutions')
                    chromosomes = create_random_chromosomes(genes)
                    #Draw most possible solutions
                    for i in range(len(chromosomes)):
                        draw_connection(screen, chromosomes[i])
                    #Main Logic Loop
                    print('Starting calculations')
                    while len(chromosomes) > 10:
                        print(str(len(chromosomes)) + ' chromosomes left')
                        new_size = int(len(chromosomes)/resize_rate)
                        #Calculate fitness scores
                        fitness_scores = calculate_fitness(chromosomes)
                        #Build dictionary to preserve order
                        chrom_fit_dict = build_chromosome_fitness_dict(chromosomes, fitness_scores)
                        #Roulette selection - select chromosomes for next generation
                        selected_chromosomes = roulette_selection(chromosomes, fitness_scores, new_size)
                        #Adopt newly selected chromosomes as population
                        chromosomes = selected_chromosomes
                        #Apply crossover mutation
                        mutated_chromosomes = crossover(chromosomes, cross_rate)
                        #Adopt mutated chromosomes as population
                        chromosomes = mutated_chromosomes
                    best_chrom = fitness_scores.index(max(chrom_fit_dict))
                    draw_best_connection(screen, chromosomes[best_chrom])
            if event.key == pygame.K_c:
                draw_background(screen)
                genes = []
    if first == True:
        draw_background(screen)
        first = False
    #Get points
    if pygame.mouse.get_pressed() == (1, 0, 0):
        mouse_pos = pygame.mouse.get_pos()
        genes.append(mouse_pos)
        pygame.draw.rect(screen, black, [mouse_pos[0], mouse_pos[1], 2, 2], 1)
        genes = list(set(genes))
    pygame.display.flip()
    clock.tick(30)
pygame.quit()
