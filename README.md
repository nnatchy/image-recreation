# image-recreation

## Contributors

This project was developed by the following contributors:

- [Jirawat Lengnoi](https://github.com/nnatchy) (ID: 6431307421)
- [Chanagun Viriyasathapornpong](https://github.com/guncv) (ID: 6431309721)
- [Pirayan Rananand](https://github.com/pirayan20) (ID: 6431334321)

Each contributor played a significant role in the development and success of this project.

# Class Overview

# Individual

## `Individual` Class Overview

The `Individual` class is central to the genetic algorithm and represents one possible solution in the evolving population. Each instance of the class corresponds to an image that undergoes mutation and crossover operations.

### Attributes

The `Individual` class has the following attributes:

1. **`l` and `w`**:

   - Represent the dimensions (length and width) of the individual's image.

2. **`fitness`**:

   - A numerical measure of how closely the individual's image resembles the target image.
   - Lower fitness indicates higher similarity to the target.

3. **`array`**:

   - A NumPy array representation of the individual's image.
   - Useful for efficient pixel manipulation and computation.

4. **`image`**:
   - A PIL (Python Imaging Library) `Image` object that represents the individual's image in a visual format.

---

### Methods

The `Individual` class provides several methods to initialize, manipulate, and evaluate the candidate solutions:

#### 1. `__init__`

- Initializes an individual with random attributes, including the dimensions, fitness, and a randomly generated image.

#### 2. `rand_color`

- Generates a random color in hexadecimal format.
- Useful for creating visually diverse random images.

#### 3. `create_one_color`

- Creates an image filled with a single random color.
- Useful for initial population generation or testing.

#### 4. `create_random_image_array`

- Generates an image with random polygons.
- Adds stochasticity and potential detail to the candidate solutions.

#### 5. `create_random_image_array_2`

- Creates a random image using a NumPy array filled with random pixel values.
- Another approach for generating initial diversity in the population.

#### 6. `add_shape`

- Adds a random polygon to the existing image.
- Facilitates incremental modifications during mutation operations.

#### 7. `to_image` and `to_array`

- Convert between PIL `Image` and NumPy array formats.
- Ensure compatibility between computational operations and visualization.

#### 8. `get_fitness`

- Calculates the fitness of the individual by comparing its image to the target image.
- Uses color difference metrics to evaluate similarity.

#### 9. `get_fitness_euclidean`

- An alternative method for fitness calculation.
- Uses Euclidean distance between pixel values to quantify the similarity to the target image.

## How the `Individual` Class Fits Into the Genetic Algorithm

1. **Initialization**:

   - Each `Individual` starts with random attributes and a random image.

2. **Evolution**:

   - Through crossover and mutation, individuals evolve to improve their fitness scores.

3. **Fitness Evaluation**:

   - The `get_fitness` or `get_fitness_euclidean` methods determine how well an individual matches the target image.

4. **Population Dynamics**:
   - Higher-fitness individuals are more likely to be selected for reproduction, ensuring the population converges towards the target image over generations.

## `GP` Class Overview

The `GP` class orchestrates the overall genetic algorithm process, managing the evolution of the population to find the closest match to the target image.

### Attributes

1. **`target_image`**:

   - The image the algorithm is attempting to recreate.

2. **`l` and `w`**:

   - Dimensions (length and width) of the target image.

3. **`target_image_array`**:
   - A NumPy array representation of the target image for efficient fitness evaluation.

---

### Methods

The `GP` class provides the following methods to drive the genetic algorithm:

#### 1. `__init__`

- Initializes the genetic algorithm with a target image.
- Converts the target image into a NumPy array for comparison.

#### 2. `run_gp`

- The main driver of the genetic algorithm.
- Steps:
  1. Initializes a population of `Individual` objects with random images.
  2. Evolves the population over a specified number of generations.
  3. Evaluates fitness for each individual in each generation.
  4. Returns the fittest individual after all generations.

#### 3. `tournament_select`

- Selects the fittest individual from a randomly sampled subset of the population.
- Ensures that the most promising candidates are chosen for reproduction.

#### 4. `crossover`, `crossover_2`, `crossover_3`

- Different strategies for combining two parent individuals to create a child:
  - **`crossover`**: Blends pixel values from two parents.
  - **`crossover_2`**: Combines regions of parent images.
  - **`crossover_3`**: Introduces novel strategies for merging parent traits.

#### 5. `mutate`, `mutate_2`

- Introduces random variations to an individual's image:
  - **`mutate`**: Adds random polygons or shapes.
  - **`mutate_2`**: Alters pixel values directly.
- Maintains genetic diversity in the population to avoid premature convergence.

---

## How the `GP` Class Works

### 1. Initialization

- The `GP` class is initialized with the target image.
- A population of `Individual` objects is created, each representing a randomly generated image.

### 2. Evolution

- The **`run_gp`** method evolves the population over multiple generations:
  1. Individuals are **selected** for reproduction using **`tournament_select`**.
  2. **Children** are generated using one of the **crossover** methods.
  3. Some individuals are **mutated** to introduce variation.

### 3. Fitness Evaluation

- Each individual's fitness is calculated by comparing its image to the target image.
- The algorithm aims to minimize the fitness value, meaning the image gets closer to the target.

### 4. Selection of the Fittest

- After evolving for a specified number of generations, the individual with the best fitness score is returned as the final solution.

---

## How the `GP` and `Individual` Classes Work Together

- The `GP` class **manages** the population and drives the evolutionary process.
- The `Individual` class **represents** the candidate solutions and provides methods for mutation and fitness evaluation.
- Together, they form the core components of the genetic algorithm.

---

## Application

This setup uses genetic algorithms to recreate a target image by evolving a population of images through generations. You can experiment with:

- **Population size**: Larger populations can explore the solution space more effectively but might lack in `stochasticity`.
- **Number of generations**: More generations allow for further refinement.
- **Mutation rates**: Higher mutation rates increase diversity but may slow convergence.

---

## Experimentation

This is the hyperparmeters that worked best for us:

- Initial Population
  - Size of 100
  - Each with [3, 6] shapes of random color
- Fitness Function
  - Only Delta_E
- Selection
  - Tournament size of 6
- Repopulation
  - Crossover
    - Using a probabilistic mix of 30% crossover 1 (blending) and 60% crossover 2 (crossover)
  - Mutation
    - Using a 10% chance for mutation 1 (adding shape)
- Number of generations
  - Anywhere between 5,000 and 10,000

---

## How to use our Streamlit interactive demo

- prerequisite
  - `streamlit`
  - `python >3.10`
  - `poetry`

```bash
# install dependencies
poetry install

# run the application
cd app
streamlit run streamlit.py
```
