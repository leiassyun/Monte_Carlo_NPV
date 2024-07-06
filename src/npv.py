import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Pool
import src.data_fetcher as data_fetcher

def calculate_npv(cashflows, capm):
    npv = 0
    for t, cashflow in enumerate(cashflows):
        discount_rate = max(capm[t], 0.01)  # Floor to 0.01 to handle negative rates
        present_value = cashflow / (1 + discount_rate) ** (t + 1)
        npv += present_value
    return npv

def monte_carlo(cashflows, discount_rates, iterations=5000, num_processes=4):
    pool = Pool(processes=num_processes)

    cashflow_mean = np.mean(cashflows)
    cashflow_std = np.std(cashflows)

    args = []
    for _ in range(iterations):
        simulated_cashflows = np.random.normal(cashflow_mean, cashflow_std, len(cashflows))
        args.append((simulated_cashflows, discount_rates))

    npvs = pool.starmap(calculate_npv, args)
    pool.close()
    pool.join()

    return args, npvs


def plot_simulation(company, npvs, bins=50):
   
    company_name = data_fetcher.fetch_data(company).info['longName']
    plt.hist(npvs, bins=bins)
    plt.xlabel('NPV')
    plt.ylabel('Frequency')
    plt.title(f'Monte Carlo Simulation of NPV of {company_name}')
    plt.show()
    plt.close()



def summary_statistics(npvs):
    stats = {
        'mean': np.mean(npvs),
        'median': np.median(npvs),
        'std_dev': np.std(npvs),
        'min': np.min(npvs),
        'max': np.max(npvs),
        '25th_percentile': np.percentile(npvs, 25),
        '75th_percentile': np.percentile(npvs, 75)
    }
    return stats


def print_summary_statistics(stats):
    print("\nSummary Statistics:")
    print("-------------------")
    for key, value in stats.items():
        print(f"{key:20}: {value:.2f}")

