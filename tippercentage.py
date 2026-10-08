def total_calc(bill_Amount, tip_perc):

    total = bill_Amount*(1 + 0.01 * tip_perc)
    total = round(total,2)
    print(f"Please pay ${total}")



total_calc(150,20)