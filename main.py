"""Sorting Algorithm Performance Analyzer - Team 36"""

import random
import time
import tracemalloc

from merge_sort import merge_sort
from quick_sort import quick_sort

dataset =[]
dataset_size =100_000
distribution = "Random"
results = {}
def generate_dataset(size, inputDistribution):

    if inputDistribution   == "Random":
        return [random.randint(0, size * 10) for _ in range(size)]
    
    if inputDistribution== "Already Sorted":
        return list(range(size))
    
    if inputDistribution ==  "Reverse-Sorted":
        return list(range(size, 0, -1))
    
    if inputDistribution == "Duplicate-Heavy":
        return [random.randint(0, 10) for _ in range(size)]
    
    raise ValueError( "Unknown input distribution.")

def run_algorithm(name, algorithm, values):
    tracemalloc. start()
    start_time =time.perf_counter()
    sorted_values, comparisons = algorithm(values.copy())
    elapsed_time  = time.perf_counter() - start_time
    _, peak_memory = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    result = {"time": elapsed_time, "comparisons":  comparisons, "memory":peak_memory / (1024 *1024),"correct": sorted_values == sorted(values),}
    results[name] = result
    return result

def print_header():
    print("=" * 58)

    print("              SORTING ALGORITHM")
    print("              PERFORMANCE ANALYZER" )
    print("                   TEAM 36")
    print("=" * 58)


def print_dataset_settings():
    status = "Generated" if dataset else "Not generated"

    print("\nCURRENT DATASET SETTINGS" )
    print("-" *  58 )

    print(f"Dataset size:{dataset_size:,} integers" )
    print(f"Input distribution: {distribution}")
    print(f"Dataset status:{status }" )

    print("-" * 58)

def print_menu():
    print_header()

    print("MAIN MENU")
    print("1. Generate Dataset" )
    print("2. Select Dataset Size")
    print("3. Select Input Distribution")
    print ("4. Run Merge Sort")

    print("5. Run Quick Sort" )
    print("6. Compare Results")
    print("7. Exit")
    print_dataset_settings()

def show_result(name, result):
    print(f"\n{name} RESULTS")

    print("-" * 45)
    print(f"Execution time:       {result['time']:.6f} seconds" )
    print(f"Element comparisons:  {result['comparisons']:,}")
    print(f"Peak traced memory:   {result['memory']:.2f} MB ") 
    print(f"Sorting correct:      {'Yes' if result['correct'] else 'No'} ")

    print("-" * 45)

def select_dataset_size():
    global dataset_size
    global dataset

    print( "\nSELECT DATASET SIZE" )
    print("1. 100,000")
    print("2. 250,000") 

    print("3. 500,000")
    print("4. 1,000,000")
    choices = {"1": 100_000, "2": 250_000, "3": 500_000, "4": 1_000_000}

    choice = input("Select a size (1-4): ").strip()

    if choice in  choices:
        dataset_size =choices[choice]
        dataset =[]
        results.clear()
        print (f"Dataset size set to {dataset_size:,}. Generate a new dataset." )

    else:

        print("Invalid selection. Dataset size was not changed.")

def select_distribution():
    global distribution
    global  dataset

    print("\nSELECT INPUT DISTRIBUTION" )
    print( "1. Random") 
    print("2. Already Sorted")
    print("3. Reverse-Sorted")
    print ("4. Duplicate-Heavy")
    choices = {

        "1": "Random",
        "2": "Already Sorted",
        "3": "Reverse-Sorted",
        "4": "Duplicate-Heavy",
    }
    choice = input("Select a distribution (1-4): " ).strip()
    if choice in choices :
        distribution =choices[choice]
        dataset= []
        results.clear()
        print(f"Input distribution set to {distribution}. Generate a new dataset.")

    else:
        print("Invalid selection. Distribution was not changed.")

def generate_current_dataset():
    global dataset

    print(f"\nGenerating {dataset_size:,}{distribution.lower() } values..." )
    dataset = generate_dataset( dataset_size, distribution)
    results.clear()

    print("Dataset generated successfully.")

def run_merge_sort():
    if not dataset:
        print("\nPlease generate a dataset first (option 1)." )
        return
    
    print("\nRunning Merge Sort..." )
    result = run_algorithm("Merge Sort", merge_sort,dataset)
    show_result("MERGE SORT", result )

def run_quick_sort():
    if not dataset:
        print( "\nPlease generate a dataset first (option 1).")
        return
    
    print("\nRunning Quick Sort...")
    result = run_algorithm("Quick Sort", quick_sort, dataset )
    show_result("QUICK SORT", result)

def compare_results() :
    if "Merge Sort" not in results or "Quick Sort" not in results:
        print("\nRun both Merge Sort and Quick Sort on the current dataset first.")
        return

    merge = results["Merge Sort" ]
    quick = results["Quick Sort"]

    print("\n" + "=" * 67)
    print("                    PERFORMANCE COMPARISON")

    print( "=" *  68)
    print(f"{'Metric':<25}{'Merge Sort':>20}{'Quick Sort':>20}" )
    print("-" * 67)
    print(f"{'Execution time (sec)':<25} {merge['time']:>20.6f}{quick['time' ]:>20.6f}")
    print(f"{'Comparisons':<25}{merge ['comparisons']:>20,}{quick ['comparisons']:>20,}")

    print(f"{'Peak memory (MB)' :<25}{merge['memory'] :>20.2f}{quick[ 'memory']:>20.2f}")
    print( f"{'Sorting correct':<25}{str(merge['correct']):>20}{str(quick['correct']):>20}" )
    print("=" * 67)
    if merge[ "time"] <quick["time"]:
        faster =  "Merge Sort"  
    else : 
         "Quick Sort"
    if merge[ "comparisons"] <quick["comparisons"]:
        fewer = "Merge Sort"  
    else:
        "Quick Sort"
    print(f"Faster algorithm: {faster}" )
    print(f"Fewer comparisons: {fewer}")
    print("\nNote: Memory is peak Python-traced allocation during each run.")
    print("Timing and memory measurements can vary between runs.")

def main():
    while True:
        print_menu()
        choice = input("\nSelect an option (1-7): " ).strip()

        if choice == "1":
            generate_current_dataset()

        elif choice ==  "2":
            select_dataset_size()

        elif choice == "3":
            select_distribution()
        elif choice == "4":
            run_merge_sort()

        elif choice == "5":
            run_quick_sort()
        elif choice == "6":
            compare_results()

        elif choice == "7":
            print("\nThank you for using the Sorting Algorithm Performance Analyzer!")
            break

        else:
            print("\nInvalid option. Please enter a number from 1 to 7." )


        input("\nPress Enter to return to the main menu...")


if __name__ == "__main__":
    main()
