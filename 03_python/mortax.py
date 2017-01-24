# This program allows one to calculate the monthly payments associated with a given home or auto loan amount. They can then see if they can afford those payments based on net income after taxes.

print('Hello! I am so glad to be able to help you today! To determine the monthly cost of your desired home or auto loan, type "home()" or "car()" respectively, and follow the instructions. To find your net income after taxes in order to see if your desired mortgage is in your price range, type "taxmarried()","taxsingle()" or "taxhoh()" depending on you tax status and follow the instructions. Thank you!')

# mortgage calculator

def home():

    # Obtain principal value

    principal=int(input('Enter your loan amount: '))
    while principal < 10000 or principal >10000000:
        print('Mortgage amount is not legal. Home loans cannot be less than $10,000 or exceed $10,000,000. Please enter a legal value.')
        principal = int(input('Enter your loan amount: '))

    # Obtain Annual Interest Rate
    apr=float(input('Enter you annual pertcentage rate: '))
    while apr <1 or apr>10:
        print('Annual interest rate is not legal. Home loan interest rates cannot be less than %1 or exceed 10%. Please enter a legal value.')
        apr=float(input('Enter you annual pertcentage rate: '))

    # Obtain loan term
    term=int(input('Enter the length of the loans term in years: '))
    while term < 1 or term > 30:
        print('Loan term is not legal. Home loan terms cannot be less than 1 year or exceed 30 years. Please enter a legal term.')
        term=int(input('Enter the length of the loans terms in years: '))

    # Obtain property tax rate
    prop_tax = float(input('Enter the property tax rate for the county in which you plan to buy the home: '))
    while prop_tax > 3:
        print('Wow! That is an extremely high rate! You should consider moving somewhere else. If you would like to try a lower property tax rate please enter it below.')
        prop_tax = int(input('Please enter a lower property tax rate: '))

    #Obtain home owner's insurance
    owners_insur = (input('Would you like us to include a ballpark figure for home owners insurance in your monthly payments estimate?: '))
    if owners_insur == 'yes':
        owners_insur = ((principal*35)/100000)
    else:
        owners_insur = 0

    # Obtain mortgage insurnce amount
    mort_insur = float(input('Enter mortgage insurance amount (typical amounts range from 0.3% to 1.5% depending on your credit score): '))
    while mort_insur > 1.5:
        print('This value is not within the accepted range. Please enter a value between 0% and 1.5%.')
        mort_insur = int(input('Please enter another mortgage insurance percentage: '))

    # Obtain HOA fees
    hoa = int(input('Enter your monthly hoa fee: '))
    while hoa > 1500:
        print('Your HOA fee is astronomical. Please move somewhere else or re-enter another value')
        hoa = int(input('Please enter another monthly HOA fee amount: '))

    # Calculations
    monthly_payments = (principal*apr/1200)/((1-(1+apr/1200)**(-term*12)))
    monthly_payment_with_fees = monthly_payments + hoa + (mort_insur*principal/1200) + (prop_tax*principal/1200) + owners_insur
    total_loan = monthly_payments*term*12
    necessary_salary = monthly_payment_with_fees*30
    total_interest = total_loan-principal
    fees = monthly_payment_with_fees-monthly_payments

    # Informing debtor of the values
    print('The total value of your loan is $' + str(round(total_loan)) + '.')
    print('The total amount of interest you would pay is $' + str(round(total_interest)) + '.')
    print('Your monthly payments without fees would be $' + str(round(monthly_payments)) + '.')
    print('Your monthly payments with fees would be $' + str(round(monthly_payment_with_fees)) + '.')
    print('Your total fees per month would be $' + str(round(fees)) + '.')
    print('You would need to make $' + str(round(necessary_salary)) + ' a year after taxes to afford such a home.')



# Auto loan calculator

def car():

    # Obtain principal value

    principal=int(input('Enter your loan amount: '))
    while principal < 5000 or principal >2500000:
        print('Loan amount is not available. Auto loans are usually not less than $5,000 or in excess of $2,500,000. Please enter a valid value.')
        principal = int(input('Enter your loan amount: '))

    # Obtain Annual Interest Rate
    apr=float(input('Enter you annual pertcentage rate: '))
    while apr <1 or apr>20:
        print('Annual interest rate is not normal. Auto loan interest rates are rarley less than %1 or in excess of 20%. Please enter a valid value.')
        apr=float(input('Enter you annual pertcentage rate: '))

    # Obtain loan term
    term=int(input('Enter the length of the loans term in years: '))
    while term < 3 or term > 7:
        print('Loan term is not available. Auto loan terms are rarely less than 3 years or in excess of 7 years. Please enter a valid term.')
        term=int(input('Enter the length of the loans terms in years: '))


    # Calculations
    monthly_payments = (principal*apr/1200)/((1-(1+apr/1200)**(-term*12)))
    total_loan = monthly_payments*term*12
    necessary_salary = monthly_payments*160
    total_interest = total_loan-principal

    # Informing debtor of the values
    print('The total value of your loan is $' + str(round(total_loan)) + '.')
    print('The total amount of interest you would pay is $' + str(round(total_interest)) + '.')
    print('Your monthly payments would be $' + str(round(monthly_payments)) + '.')
    print('You would need to make $' + str(round(necessary_salary)) + ' a year after taxes to responsibly afford such a vehicle.')



# Married peron tax calculator

def taxmarried():

    # Obtain income
    gross_income = int(input('Enter your gross yearly income: '))

    # Obtain deductions
    deductions = int(input('If you would like to include any deductions besides the standard deduction please enter the value of those deductions here: '))
    if deductions < 12600:
        deductions = 12600
    else:
        deductions = deductions

    # Tax calculations
    taxable_income = gross_income - deductions
    if taxable_income < 0:
        net_income = 0
        print('You owe zero taxes this year! Hurray!')
    elif taxable_income > 0 and taxable_income <= 18550:
        net_income = (taxable_income*0.9)
    elif taxable_income > 18550 and taxable_income <= 75300:
        net_income = (taxable_income-(1855 + (taxable_income - 18550)*0.15))
    elif taxable_income > 75300 and taxable_income <= 151900:
        net_income = (taxable_income-(10368 + (taxable_income -75300)*0.25))
    elif taxable_income > 151900 and taxable_income <= 231450:
        net_income = (taxable_income-(29518 + (taxable_income -151900)*0.28))
    elif taxable_income > 231450 and taxable_income <= 413350:
        net_income = (taxable_income-(51792 + (taxable_income -231450)*0.33))
    elif taxable_income > 413350 and taxable_income <= 466950:
        net_income = (taxable_income-(111819 + (taxable_income -413350)*0.35))
    else:
        net_income = (taxable_income-(130579 + (taxable_income -466950)*0.396))

    net_income = net_income + deductions

    # Total percentage and amount of taxes paid calculations
    amount_paid_gross = gross_income - net_income
    percent_paid_gross = ((gross_income - net_income)*100)/gross_income

    # Information given to viewer
    print('Your net income after taxes is $' + str(round(net_income)) + '.')
    print('The total amount of tax money you paid to Uncle Sam is $' + str(round(amount_paid_gross)) + '.')
    print('The actual percentage of your income you paid in taxes is %' + str(round(percent_paid_gross, 2)) + '.')



# Single person tax calculator

def taxsingle():

    # Obtain income
    gross_income = int(input('Enter your gross yearly income: '))

    # Obtain deductions
    deductions = int(input('If you would like to include any deductions besides the standard deduction please enter the value of those deductions here: '))
    if deductions < 6300:
        deductions = 6300
    else:
        deductions = deductions

    # Tax calculations
    taxable_income = gross_income - deductions
    if taxable_income < 0:
        net_income = 0
        print('You owe zero taxes this year! Hurray!')
    elif taxable_income > 0 and taxable_income <= 9275:
        net_income = (taxable_income*0.9)
    elif taxable_income > 9275 and taxable_income <= 37450:
        net_income = (taxable_income-(928 + (taxable_income - 9225)*0.15))
    elif taxable_income > 37650 and taxable_income <= 91150:
        net_income = (taxable_income-(5184 + (taxable_income -37650)*0.25))
    elif taxable_income > 91150 and taxable_income <= 190150:
        net_income = (taxable_income-(18559 + (taxable_income -91150)*0.28))
    elif taxable_income > 190150 and taxable_income <= 413350:
        net_income = (taxable_income-(46279 + (taxable_income -190150)*0.33))
    elif taxable_income > 413350 and taxable_income <= 415050:
        net_income = (taxable_income-(119935 + (taxable_income -413350)*0.35))
    else:
        net_income = (taxable_income-(120530 + (taxable_income -415050)*0.396))

    net_income = net_income + deductions

    # Total percentage and amount of taxes paid calculations
    amount_paid_gross = gross_income - net_income
    percent_paid_gross = ((gross_income - net_income)*100)/gross_income

    # Information given to viewer
    print('Your net income after taxes is $' + str(round(net_income)) + '.')
    print('The total amount of tax money you paid to Uncle Sam is $' + str(round(amount_paid_gross)) + '.')
    print('The actual percentage of your income you paid in taxes is %' + str(round(percent_paid_gross, 2)) + '.')



# Head of Household tax calculator

def taxhoh():

    # Obtain income
    gross_income = int(input('Enter your gross yearly income: '))

    # Obtain deductions
    deductions = int(input('If you would like to include any deductions besides the standard deduction please enter the value of those deductions here: '))
    if deductions < 9300:
        deductions = 9300
    else:
        deductions = deductions

    # Tax calculations
    taxable_income = gross_income - deductions
    if taxable_income < 0:
        net_income = 0
        print('You owe zero taxes this year! Hurray!')
    elif taxable_income > 0 and taxable_income <= 13250:
        net_income = (taxable_income*0.9)
    elif taxable_income > 13250 and taxable_income <= 50400:
        net_income = (taxable_income-(1325 + (taxable_income - 13250)*0.15))
    elif taxable_income > 50400 and taxable_income <= 130150:
        net_income = (taxable_income-(6898 + (taxable_income -50400)*0.25))
    elif taxable_income > 130150 and taxable_income <= 210800:
        net_income = (taxable_income-(26835 + (taxable_income -130150)*0.28))
    elif taxable_income > 210800 and taxable_income <= 413350:
        net_income = (taxable_income-(49417 + (taxable_income -210800)*0.33))
    elif taxable_income > 413350 and taxable_income <= 441000:
        net_income = (taxable_income-(116259 + (taxable_income -413350)*0.35))
    else:
        net_income = (taxable_income-(125936 + (taxable_income -441000)*0.396))

    net_income = net_income + deductions

    # Total percentage and amount of taxes paid calculations
    amount_paid_gross = gross_income - net_income
    percent_paid_gross = ((gross_income - net_income)*100)/gross_income

    # Information given to viewer
    print('Your net income after taxes is $' + str(round(net_income)) + '.')
    print('The total amount of tax money you paid to Uncle Sam is $' + str(round(amount_paid_gross)) + '.')
    print('The actual percentage of your income you paid in taxes is %' + str(round(percent_paid_gross, 2)) + '.')
