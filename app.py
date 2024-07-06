import src.data_fetcher as data_fetcher
import src.npv as npv
import src.risk_analysis as risk


def main():
    company = input("Enter the company ticker symbol: ")
    
    # Fetch cashflows
    cashflows = data_fetcher.fetch_cashflow(company)
    print(f"Annual Cashflows: {cashflows}")

    # Fetch CAPM data
    expected_return = data_fetcher.fetch_capm(company)
    print(f"Expected Rate of Return (CAPM): {expected_return}")
    
    # Calculate NPV
    npv_value = npv.calculate_npv(cashflows, expected_return)
    print(f"NPV: {npv_value}")
    
    simulate = input("Run Monte Carlo simulation? (y/n): ")
    if simulate.lower() == 'y':
        args, npvs = npv.monte_carlo(cashflows, expected_return)
        
        
        stats = npv.summary_statistics(npvs)

        risk.risk_analysis(args)
        npv.print_summary_statistics(stats)
        npv.plot_simulation(company,npvs)
    
if __name__ == "__main__":
    main()
