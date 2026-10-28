# RentalEngine HQ - Core Operational Calculation Array Matrix
def calculate_system_metrics(gross_sales, royalty_rate):
    franchise_fee_due = float(gross_sales) * float(royalty_rate)
    net_corporate_disbursement = float(gross_sales) - franchise_fee_due
    return franchise_fee_due, net_corporate_disbursement
